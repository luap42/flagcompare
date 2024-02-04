import json, os

with open('world_countries.json', 'r') as f:
    COUNTRIES = json.load(f)

def _country_abbrev_to_name(abbrev):
    if abbrev.upper() in COUNTRIES:
        return COUNTRIES[abbrev.upper()]
    
    return abbrev.upper()


def make_text_report(report, test_case):
    keys = sorted(report.keys())
    _text = ""

    with open(os.path.join('test_cases', test_case, 'question.txt')) as f:
        _text += f"What is the *{f.read().strip()}* country?\n\n"


    _text += ("Raw data:\n")

    for key in keys:
        value = int(report[key] * 1000) / 10
        _text += (f"{key}\t{value}%\n")
    
    _text += ("\nWorst results:\n")

    items = report.items()
    items = sorted(items, key=lambda i: (i[1], i[0]))

    for i in range(5):
        value = int(items[i][1] * 1000) / 10
        _text += (f"{len(items) - i}.\t{items[i][0]}\t{value}%\t({_country_abbrev_to_name(items[i][0])})\n")

    _text += ("\nTop results:\n")
    items.reverse()

    for i in range(5):
        value = int(items[i][1] * 1000) / 10
        _text += (f"{i+1}.\t{items[i][0]}\t{value}%\t({_country_abbrev_to_name(items[i][0])})\n")
    
    return _text

def print_text_report(report, test_case):
    print(make_text_report(report, test_case))

def save_text_report(report, test_case):
    report = make_text_report(report, test_case)
    with open(os.path.join('test_cases', test_case, 'report.txt'), 'w') as f:
        f.write(report)

def make_html_report(report, test_case):
    with open('html_templates/base.html') as f:
        template = f.read()
    
    with open('html_templates/detail.html') as f:
        detail_template = f.read()
    
    with open('html_templates/table.html') as f:
        table_template = f.read()
    
    with open(os.path.join('test_cases', test_case, 'question.txt')) as f:
        question = f.read().strip()
    
    with open(os.path.join('test_cases', test_case, 'attribute.txt')) as f:
        attribute = f.read().strip()

    template = template.replace('{question}', question)

    items = report.items()
    items = sorted(items, key=lambda i: (i[1], i[0]))

    worst5 = ""
    # Worst results
    for i in range(5):
        place = str(len(items) - i)
        perc = str(int(items[i][1] * 1000) / 10)
        code = items[i][0]
        name = _country_abbrev_to_name(code)
        country_flag_image = f'<img src="../../world_flags/{code}.png" alt="{code}">'

        worst5 += table_template.replace("{place}", place).replace("{perc}", perc).replace("{code}", code) \
                .replace("{name}", name).replace("{country_flag_image}", country_flag_image) + "\n"
    
    template = template.replace("{worst5}", worst5)

    items.reverse()

    best5 = ""
    # Best results
    for i in range(5):
        place = str(i + 1)
        perc = str(int(items[i][1] * 1000) / 10)
        code = items[i][0]
        name = _country_abbrev_to_name(code)
        country_flag_image = f'<img src="../../world_flags/{code}.png" alt="{code}">'

        best5 += table_template.replace("{place}", place).replace("{perc}", perc).replace("{code}", code) \
                .replace("{name}", name).replace("{country_flag_image}", country_flag_image) + "\n"
    
    template = template.replace("{best5}", best5)

    details = ""
    keys = sorted(report.keys())
    for key in keys:
        perc = str(int(report[key] * 1000) / 10)
        code = key
        name = _country_abbrev_to_name(code)
        country_flag_image = f'<img src="../../world_flags/{code}.png" alt="{code}">'

        details += detail_template.replace("{perc}", perc).replace("{attribute}", attribute).replace("{code}", code) \
                .replace("{name}", name).replace("{country_flag_image}", country_flag_image) + "\n"
    
    template = template.replace("{details}", details)
    
    return template

def print_html_report(report, test_case):
    print(make_html_report(report, test_case))

def save_html_report(report, test_case):
    report = make_html_report(report, test_case)
    with open(os.path.join('test_cases', test_case, 'report.html'), 'w') as f:
        f.write(report)