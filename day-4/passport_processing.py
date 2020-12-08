import re

passport_format = r"([\w\d]+)\:([\w\d\#]+)"

def parse_passports():
    passports = []
    with open("./input.txt", "r") as f:
        passport = {}
        for line in f.readlines():
            if(line == "\n"):
                passports.append(passport)
                #print(passport)
                passport = {}
            else:
                fields = re.findall(passport_format, line.strip())
                for field in fields:
                    passport[field[0]] = field[1]
    return passports

passport_tests = {
    "byr": lambda a : 1920 <= int(a) <= 2002,
    "iyr": lambda a : 2010 <= int(a) <= 2020,
    "eyr": lambda a : 2020 <= int(a) <= 2030,
    "hgt": lambda a : (a.endswith("cm") and (150 <= int(a[:-2]) <= 193)) or 
                      (a.endswith("in") and ( 59 <= int(a[:-2]) <=  76)),
    "hcl": lambda a : re.fullmatch(r"\#[\da-f]{6}", a) != None,
    "ecl": lambda a : a in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda a : re.fullmatch(r"\d{9}", a) != None
}

# Part 1
def check_valid_passport(passport, required_fields):
    return set(required_fields).issubset(set(passport.keys()))

# Part 2
def check_valid_values(passport):
    for key, value in passport.items():
        if key != "cid" and not passport_tests[key](value.strip()):
            return False
    return True

passports = parse_passports()

valid_count = 0
valid_values = 0

for passport in passports:
    if (check_valid_passport(passport, passport_tests.keys())):
        valid_count += 1
        if (check_valid_values(passport)):
            valid_values += 1

print("Part 1 count: {}".format(valid_count))
print("Part 2 count: {}".format(valid_values))