import asyncio

from .base import get_item_base, save_data
from models.namecard import EncoreNameCard, EncoreNameCards


async def get_namecards():
    return await get_item_base("namecard", EncoreNameCards)


async def get_namecard(namecard_id: int):
    return await get_item_base(f"namecard/{namecard_id}", EncoreNameCard)


async def main():
    namecards = await get_namecards()
    tasks, data = [], []
    for namecard in namecards.namecardList:
        tasks.append(get_namecard(namecard.Id))
        if len(tasks) == 5:
            data.extend(await asyncio.gather(*tasks))
            tasks = []
    if tasks:
        data.extend(await asyncio.gather(*tasks))
    save_data("namecard", data)
