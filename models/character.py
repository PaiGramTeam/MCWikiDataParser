from typing import List

from pydantic import BaseModel, Field

from .enums import Element


class RoleListItem(BaseModel):
    Id: int
    RoleHeadIcon: str
    Name: str


class EncoreAvatars(BaseModel):
    roleList: List[RoleListItem]


class EncoreAvatar(BaseModel):
    id: int = Field(alias="Id")
    """ 角色ID """
    name: str = Field(alias="Name")
    """ 名称 """
    rank: int = Field(alias="Priority")
    """ 星级 """
    element: Element = Field(alias="ElementName")
    """ 属性 """
    RoleHeadIconCircle: str
    RoleHeadIconLarge: str
    RoleHeadIconBig: str
    Card: str
    RoleHeadIcon: str
    FormationRoleCard: str
    RoleStand: str
    RolePortrait: str

    @property
    def big_gacha(self) -> str:
        return self.RoleStand

    @property
    def gacha(self) -> str:
        return self.FormationRoleCard

    @property
    def square(self) -> str:
        return self.Card

    @property
    def normal(self) -> str:
        return self.RoleHeadIconLarge
