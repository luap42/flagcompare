from _flags import *
from _compare import *
from _report import *


flag_results = {}
base_flag = get_base_flag()

for flag in get_all_flags():
    flag_image = open_flag(flag)
    flag_results[flag] = compare(base_flag, flag_image)


print_text_report(flag_results)