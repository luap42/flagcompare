import os
from PIL import Image

TARGET_SIZE = (100, 100)

def get_all_flags():
    return ['de']

def open_flag(fn):
    print(os.path.abspath(os.path.join('world_flags', f"{fn}.png")))
    return _read_flag(os.path.join('world_flags', f"{fn}.png"))

def get_base_flag():
    return _read_flag('base_flag.png')

def _read_flag(fp):
    im = Image.open(fp)
    im = im.resize(TARGET_SIZE)
    im = im.convert('RGB')
    return im