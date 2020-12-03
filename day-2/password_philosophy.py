import re

def parse_input():
    lines = []
    with open("./input.txt", "r") as f:
        for line in f.readlines():
            lines.append(line)
    return lines

# Part 1
def check_valid_password_by_count(min_num, max_num, character, password):
    return min_num <= password.count(character) <= max_num

# Part 2
def check_valid_password_by_position(pos1, pos2, character, password):
    if password[pos1 - 1] == character: 
        return password[pos2 - 1] != character
    if password[pos2 - 1] == character:
        return password[pos1 - 1] != character
    return False

format_string = r"(\d+)\-(\d+) (\w)\: (\w+)"
input_lines = parse_input()

valid_passwords_count = 0
valid_passwords_pos = 0
for line in input_lines:
    num1, num2, character, password = re.match(format_string, line).groups()
    if check_valid_password_by_count(int(num1), int(num2), character, password):
        valid_passwords_count += 1
    try:
        if check_valid_password_by_position(int(num1), int(num2), character, password):
            valid_passwords_pos += 1
    except:
        continue

print("Part 1 count: {}".format(valid_passwords_count))
print("Part 2 count: {}".format(valid_passwords_pos))
