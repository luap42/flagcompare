import os
from PIL import Image

TARGET_SIZE = (100, 100)

def get_all_flags():
    flags = []
    for flag in os.scandir('world_flags'):
        flags.append(flag.name.split(".")[0])
    
    return flags

def open_flag(fn):
    return _read_flag(os.path.join('world_flags', f"{fn}.png"))

def get_base_flag(test_case):
    return _read_flag(os.path.join('test_cases', test_case, 'base_flag.png'))

def _read_flag(fp):
    im = Image.open(fp)
    im = im.resize(TARGET_SIZE)
    im = im.convert('RGB')
    return im