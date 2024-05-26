from typing import Dict, Any

from .base import get_item_base, save_data
from models.character import EncoreAvatar, EncoreAvatars


async def get_characters():
    return await get_item_base("character", EncoreAvatars)


async def fix_character(data: Dict[str, Any]) -> Dict[str, Any]:
    data["Name"] = data["Name"]["Content"]
    return data


async def get_character(character_id: int):
    return await get_item_base(f"character/{character_id}", EncoreAvatar, fix_func=fix_character)


async def main():
    characters = await get_characters()
    data = [await get_character(character.Id) for character in characters.roleList]
    save_data("character", data)
