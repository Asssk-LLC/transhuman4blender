import addon_utils
from pathlib import Path

def get_addon_root(addon_name):
  for mod in addon_utils.modules():
      name = mod.bl_info.get("name")
      if name == addon_name:
          path = Path(mod.__file__).parent
          return path
  return None
