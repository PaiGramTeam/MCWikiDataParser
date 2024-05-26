from typing import Dict, Any

from .base import get_item_base, save_data
from models.weapon import EncoreWeapon, EncoreWeapons


async def get_weapons():
    return await get_item_base("weapon", EncoreWeapons)


def get_url_ext(url: str) -> str:
    return url.split(".")[-1]


def replace_url_ext(url: str, ext: str) -> str:
    return ".".join(url.split(".")[:-1]) + f".{ext}"


async def fix_weapon_icon(data: Dict[str, Any]) -> Dict[str, Any]:
    for k in ["Icon", "IconMiddle", "IconSmall"]:
        if data[k] and data[k].startswith("/"):
            data[k] = f"https://api.encore.moe/resource/Data{data[k]}"
        if get_url_ext(data[k]) == "png":
            continue
        new_url = replace_url_ext(data[k], "png")
        data[k] = new_url
    return data


async def get_weapon(weapon_id: int):
    return await get_item_base(f"weapon/{weapon_id}", EncoreWeapon, fix_func=fix_weapon_icon)


async def main():
    weapons = await get_weapons()
    data = [await get_weapon(weapon.Id) for weapon in weapons.weapons]
    save_data("weapon", data)
