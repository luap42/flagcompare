def print_text_report(report):
    keys = sorted(report.keys())

    for key in keys:
        value = int(report[key] * 1000) / 10
        print(f"{key}\t{value}%")