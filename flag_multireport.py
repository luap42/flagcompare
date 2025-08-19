import os
import shutil

# step 1: delete multireport repository

shutil.rmtree('./multireport')
os.mkdir('./multireport')
open('./multireport/.keep', 'a').close()

# step 2: copy over world flags to multireport

shutil.copytree("./world_flags", "./multireport/world_flags")

# step 3: find all test cases

test_cases = os.listdir("./test_cases")

# step 4: run generator for each test case and copy over report file

for test_case in test_cases:
    os.system(f"python3 flag_compare.py {test_case}")

    # read report
    with open(f"test_cases/{test_case}/report.html") as f:
        report = f.read()
    
    # fix urls
    report = report.replace("../../world_flags/", "/world_flags/")
    report = report.replace("flagmod.png", f"{test_case}-flagmod.png")
    report = report.replace("<!-- {backlink} -->", '<a href="/" class="backlink">back to index page</a>')

    # write report in multireport
    with open(f"multireport/{test_case}.html", 'w') as f:
        f.write(report)

    # copy over flagmod.png
    shutil.copy(f"test_cases/{test_case}/flagmod.png", f"multireport/{test_case}-flagmod.png")

# step 5: write template

with open('html_templates/multireport.html') as f:
    template = f.read()

test_case_links = '\n'.join([
    f'<li>Compare for: <a href="{test_case}.html">{test_case}</a></li>' for test_case in test_cases
])

template = template.replace('{test_cases}', test_case_links)

with open('multireport/index.html', 'w') as f:
    f.write(template)