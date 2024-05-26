from typing import List

from pydantic import BaseModel, Field


class Weapon(BaseModel):
    Id: int
    Name: str
    Icon: str


class EncoreWeapons(BaseModel):
    weapons: List[Weapon]


class EncoreWeapon(BaseModel):
    id: int = Field(alias="ItemId")
    """"武器ID"""
    name: str = Field(alias="WeaponName")
    """名称"""
    description: str = Field(alias="BgDescription")
    """描述"""
    rank: int = Field(alias="QualityId")
    """稀有度"""
    IconBig: str = Field(alias="Icon")
    IconMiddle: str
    IconSmall: str
    Mesh: str

    @property
    def icon(self):
        return self.IconBig

    @property
    def big_pic(self):
        return self.IconMiddle
