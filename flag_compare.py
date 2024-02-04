from _flags import *
from _compare import *
from _report import *

import sys

if len(sys.argv) != 2:
    print("Usage: python3 {sys.argv[0]} [test case]")
    sys.exit(1)

test_case = sys.argv[1]

flag_results = {}
base_flag = get_base_flag(test_case)

for flag in get_all_flags():
    flag_image = open_flag(flag)
    flag_results[flag] = compare(base_flag, flag_image)


save_text_report(flag_results, test_case)
save_html_report(flag_results, test_case)