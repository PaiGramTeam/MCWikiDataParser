from enum import Enum


class Element(str, Enum):
    """属性"""

    Wind = "气动"
    Fire = "热熔"
    Light = "衍射"
    Ice = "冷凝"
    Dark = "湮灭"
    Thunder = "导电"
