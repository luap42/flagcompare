def print_text_report(report):
    keys = sorted(report.keys())

    print("Raw data:")

    for key in keys:
        value = int(report[key] * 1000) / 10
        print(f"{key}\t{value}%")
    
    print()
    print("Worst results:")

    items = report.items()
    items = sorted(items, key=lambda i: i[1])

    for i in range(5):
        value = int(items[i][1] * 1000) / 10
        print(f"{len(items) - i}.\t{items[i][0]}\t{value}%")

    print()
    print("Top results:")
    items.reverse()

    for i in range(5):
        value = int(items[i][1] * 1000) / 10
        print(f"{i+1}.\t{items[i][0]}\t{value}%")