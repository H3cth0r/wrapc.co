from __future__ import annotations
from pathlib import Path

def get_fw_include():
    import wrapcco
    resources_dir = str(Path(wrapcco.__file__).parent / 'resources')
    return resources_dir
