def parse_report():
    report = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            report.append(int(line))
    return report

# Part 1
def find_product_of_two_by_sum(report, sum_to_find):
    for num in report:
        search_value = sum_to_find - num
        if search_value in report:
            return num * search_value
    return None

# Part 2
def find_product_of_three_by_sum(report, sum_to_find):
    for i, num in enumerate(report):
        for j in range(i + 1, len(report)):
            search_value = sum_to_find - num - report[j]
            if search_value in report:
                return num * search_value * report[j]
    return None

expense_report = parse_report()
print("Part 1 Answer: {}".format(find_product_of_two_by_sum(expense_report, 2020)))
print("Part 2 Answer: {}".format(find_product_of_three_by_sum(expense_report, 2020)))