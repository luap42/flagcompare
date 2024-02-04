import os

def get_all_flags():
    return ['en']

def open_flag(fn):
    return _read_flag(os.path.join('./world_flags', f"{fn}.png"))

def get_base_flag():
    return _read_flag('base_flag.png')

def _read_flag(fp):
    pass