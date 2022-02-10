from email.headerregistry import Group
from typing import List


class GroupSpec:
    # Will be displayed on widgets bar
    name: str
    description: str
    # List of executables to bind to specific group
    executables: List[str]

    _all_groups: List['GroupSpec'] = []
  
    def __init__(self, *, name: str, description: str, executables: List[str] = None) -> 'GroupSpec':
        self.name = name
        self.description = description
        self.executables = [ex for ex in (executables if executables else [])]

        GroupSpec._all_groups.append(self)

    @staticmethod
    def get_group_for_executable(ex: str) -> 'GroupSpec':
        for group in GroupSpec._all_groups:
            if ex in group.executables:
                return group
