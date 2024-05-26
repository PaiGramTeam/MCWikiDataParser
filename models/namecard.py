from typing import List

from pydantic import BaseModel, Field


class NamecardListItem(BaseModel):
    Id: int
    CardPath: str
    Icon: str
    IconMiddle: str
    IconSmall: str
    Name: str


class EncoreNameCards(BaseModel):
    namecardList: List[NamecardListItem]


class EncoreNameCard(BaseModel):
    Id: int
    QualityId: int
    SortIndex: int
    LongCardPath: str
    CardPath: str
    FunctionViewCardPath: str
    Icon: str
    IconMiddle: str
    IconSmall: str

    name: str = Field(alias="Title")
    desc: str = Field(alias="AttributesDescription")

    ObtainedShowDescription: str
    TypeDescription: str
    BgDescription: str
    Tips: str
    ShowInBag: bool
    RedDotDisableRule: int
