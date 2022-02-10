from typing import List

from libqtile.config import Group

from . import groups, GroupSpec


def make_groups() -> List[GroupSpec]:
    return [Group(g.name, spawn=g.executables) for g in groups]
