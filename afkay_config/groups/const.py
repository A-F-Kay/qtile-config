from typing import List
from . import GroupSpec


groups: List[GroupSpec] = [
  GroupSpec(name='WWW', description='Browser / Internet', executables=['chromium']),
  GroupSpec(name='CODE', description='IDE / Code editor', executables=['code']),
  GroupSpec(name='SH', description='Shell', executables=['alacritty']),
  GroupSpec(name='DOC', description='Browser for docs / Docs'),
  GroupSpec(name='COM', description='Communication (Discord, Telegram, etc)', executables=['telegram-desktop', 'discord']),
  GroupSpec(name='FUN', description='Videos / Music / Browser'),
]