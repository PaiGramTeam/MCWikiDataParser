from func.character import main as main_character
from func.weapon import main as main_weapon
from func.namecard import main as main_namecard


async def main():
    print("========  请求角色数据  ========")
    await main_character()
    print("========  请求武器数据  ========")
    await main_weapon()
    print("========  请求名片数据  ========")
    await main_namecard()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
