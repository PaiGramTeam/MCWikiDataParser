from .base import get_item_base, save_data
from models.weapon import EncoreWeapon, EncoreWeapons


async def get_weapons():
    return await get_item_base("weapon", EncoreWeapons)


async def get_weapon(weapon_id: int):
    return await get_item_base(f"weapon/{weapon_id}", EncoreWeapon)


async def main():
    weapons = await get_weapons()
    data = [await get_weapon(weapon.Id) for weapon in weapons.weapons]
    save_data("weapon", data)
