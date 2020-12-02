password_quantity = []
password_bounds = []
password_key = []
passwords = []
valid_passwords = []
second_valid_passwords = []

f = open('data.txt', 'r')
for line in f:
    lines_stripped = line.strip()
    lines_split = lines_stripped.split()
    password_quantity.append(lines_split[0])
    password_bounds = [i.split('-') for i in password_quantity]
    password_key.append(lines_split[1])
    password_key = [i.strip(':') for i in password_key]
    passwords.append(lines_split[2])
f.close
# quantity // letter // password
# get range and key


def rules_setter(n):
    lower = int(password_bounds[n][0])
    upper = int(password_bounds[n][1])
    key = password_key[n]
    passkey = passwords[n]
    return lower, upper, key, passkey


def counter(rules):
    lower = rules[0]
    upper = rules[1]
    key = rules[2]
    passkey = rules[3]
    letter_count = int(passkey.count(key))
    if lower <= int(letter_count) and letter_count <= upper:
        valid_passwords.append(passkey)


def position_checker(rules):
    lower = rules[0] - 1
    upper = rules[1] - 1
    key = rules[2]
    passkey = rules[3]
    if bool(passkey[lower] == key) ^ bool(passkey[upper] == key):
        second_valid_passwords.append(passkey)


i = 0
while i < len(passwords):
    counter(rules_setter(i))
    position_checker(rules_setter(i))
    i += 1


print(f' 1st part: solution is {len(valid_passwords)}')
print(f' 2nd part: solution is {len(second_valid_passwords)}')
