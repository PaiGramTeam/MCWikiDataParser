import json

from typing import Type, List

from httpx import AsyncClient
from pydantic import BaseModel
from pathlib import Path

BASE_URL = "https://api.encore.moe/zh-Hans"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}
client = AsyncClient(timeout=60.0, headers=headers)
data_path = Path("data")
data_path.mkdir(exist_ok=True)


async def get_item_base(item_path: str, item_type: Type[BaseModel], fix_func=None):
    req = await client.get(f"{BASE_URL}/{item_path}")
    req.raise_for_status()
    data = await fix_func(req.json()) if fix_func else req.json()
    item_data = item_type(**data)
    return item_data


def save_data(item_path: str, item_datas: List[BaseModel]):
    path = data_path / f"{item_path}.json"
    item_data = [i.dict(by_alias=True) for i in item_datas]
    with path.open("w", encoding="utf-8") as f:
        json.dump(item_data, f, ensure_ascii=False, indent=4)


async def have_url(url: str) -> bool:
    req = await client.head(url)
    return req.status_code == 200
