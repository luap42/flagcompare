from _flags import *
from _compare import *
from _report import *


flag_results = {}
base_flag = get_base_flag()

for flag in get_all_flags():
    flag_results[flag] = compare(base_flag, open_flag(flag))


print_text_report(flag_results)