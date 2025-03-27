import asyncio
import json
import re

from typing import Type, List, TYPE_CHECKING, Optional

from playwright.async_api import async_playwright
from pydantic import BaseModel
from pathlib import Path

if TYPE_CHECKING:
    from playwright.async_api import Browser

BASE_URL = "https://api.encore.moe/zh-Hans"
headers = {}

client = async_playwright()
p = None
browser: Optional["Browser"] = None
START = False
data_path = Path("data")
data_path.mkdir(exist_ok=True)


def retry(times: int):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    print(e)
            raise Exception("Retry failed")

        return wrapper

    return decorator


async def start_playwright():
    global START, p, browser
    if START:
        return
    p = await client.start()
    browser = await p.chromium.launch()
    # page = await browser.new_page()
    START = True


async def get_content(url: str):
    page = await browser.new_page()
    try:
        # 导航到指定 URL
        print(url)
        await page.goto(url)
        # 等待页面加载完成（可选）
        await page.wait_for_load_state("networkidle")
        # 获取页面 HTML 内容
        html_content = await page.content()
        # parse json
        pre_contents = re.findall(r'<pre[^>]*>(.*?)</pre>', html_content, re.DOTALL)
        if pre_contents:
            return json.loads(pre_contents[0])
        print(html_content)
        raise Exception("No json content")
    except Exception as e:
        print(f"发生错误: {e}")
        return None
    finally:
        await page.close()


@retry(10)
async def get_item_base(item_path: str, item_type: Type[BaseModel], fix_func=None):
    await start_playwright()
    req = await get_content(f"{BASE_URL}/{item_path}")
    await asyncio.sleep(1)
    data = await fix_func(req) if fix_func else req
    item_data = item_type(**data)
    return item_data


def save_data(item_path: str, item_datas: List[BaseModel]):
    path = data_path / f"{item_path}.json"
    item_data = [i.model_dump(by_alias=True) for i in item_datas]
    with path.open("w", encoding="utf-8") as f:
        json.dump(item_data, f, ensure_ascii=False, indent=4)
