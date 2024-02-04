import json, os

with open('world_countries.json', 'r') as f:
    COUNTRIES = json.load(f)

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
    items = sorted(items, key=lambda i: i[1])

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

def _country_abbrev_to_name(abbrev):
    return COUNTRIES[abbrev.upper()]