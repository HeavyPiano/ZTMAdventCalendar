# import re whats regex lol
f = open('data.txt', 'r')
passport_data = f.readlines()
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def passport_splitter(data):  # returns individual passports
    passport_stack = []
    passport = []
    for i in data:
        if i == '\n':
            passport_stack.append(passport)
            passport = []
        else:
            passport.append(i)
    passport_stack.append(passport)
    # print(passport_stack)
    return passport_stack


def passport_formatter(stack):  # remove newline
    passport_formatted = []
    for lines in stack:
        formatted_list = [i.strip() for i in lines]
        formatted_list = [i.split() for i in formatted_list]
        def flattened_list(formatted_list): return [
            item for sublist in formatted_list for item in sublist]
        passport_formatted.append(flattened_list(formatted_list))
    return passport_formatted


def passport_validator(passport):
    def byr_check(value):
        if 1920 <= int(value) <= 2002:
            # print(value)
            return True
        return False

    def iyr_check(value):
        if 2010 <= int(value) <= 2020:
            return True
        return False

    def eyr_check(value):
        if 2020 <= int(value) <= 2030:
            return True

        return False

    def hgt_check(value):
        if 'cm' in value:
            if 150 <= int(value.strip('cm')) <= 193:
                return True
        elif 'in' in value:
            if 59 <= int(value.strip('in')) <= 76:
                return True
        return False

    def hcl_check(value):
        accepted_values = ['0', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        if value[0] == '#':
            value = value.strip('#')
            if len(value) != 6:
                return False
            else:
                for i in value:
                    if i not in accepted_values:
                        return False
                return True
        return False

    def ecl_check(value):
        accepted_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if len(value) != 3:
            return False
        elif len(value) == 3:
            if value in accepted_colours:
                return True
            return False
        return False

    def pid_checker(value):
        if len(value) == 9 and value.isdigit():
            # print(value)
            return True
        return False

    byr_value = passport.get('byr')
    if byr_check(byr_value) == False:
        return False

    iyr_value = passport.get('iyr')
    if iyr_check(iyr_value) == False:
        return False

    eyr_value = passport.get('eyr')
    if eyr_check(eyr_value) == False:
        return False

    hgt_value = passport.get('hgt')
    if hgt_check(hgt_value) == False:
        return False

    hcl_value = passport.get('hcl')
    if hcl_check(hcl_value) == False:
        return False

    ecl_value = passport.get('ecl')
    if ecl_check(ecl_value) == False:
        return False

    pid_value = passport.get('pid')
    if pid_checker(pid_value) == False:
        return False
    # print(passport)
    return True


def passport_checker(formatted):
    valids_counter = 0
    passport_counted = 0
    for passport in formatted:
        passport_dict = {}
        for pair in passport:
            key_value = pair.split(':')
            passport_dict[key_value[0]] = key_value[1]

        if all(i in passport_dict.keys() for i in required_fields):
            passport_counted += 1
            if passport_validator(passport_dict):
                valids_counter += 1
    print(valids_counter, passport_counted)


passport_checker(passport_formatter(passport_splitter(passport_data)))
