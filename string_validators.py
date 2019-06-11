# https://www.hackerrank.com/challenges/string-validators/problem

s = input()
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False

if 0 < len(s) < 1000:
    for char in s:
        if char.isalnum():
            flag1 = True
        if char.isalpha():
            flag2 = True
        if char.isdigit():
            flag3 = True
        if char.islower():
            flag4 = True
        if char.isupper():
            flag5 = True

print(flag1)
print(flag2)
print(flag3)
print(flag4)
print(flag5)


# from discussion
# str = raw_input()
# print any(c.isalnum() for c in str)
# print any(c.isalpha() for c in str)
# print any(c.isdigit() for c in str)
# print any(c.islower() for c in str)
# print any(c.isupper() for c in str)