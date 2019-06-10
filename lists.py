# https://www.hackerrank.com/challenges/python-lists/problem

n = int(input())
k = []

for x in range(n):
    command = input().split()
    if command[0] == 'insert':
        k.insert(int(command[1]), int(command[2]))
    if command[0] == 'print':
        print(k)
    if command[0] == 'remove':
        k.remove(int(command[1]))
    if command[0] == 'append':
        k.append(int(command[1]))
    if command[0] == 'sort':
        k.sort()
    if command[0] == 'pop':
        k.pop()
    if command[0] == 'reverse':
        k.reverse()


# from discussion
# n = input()
# l = []
# for _ in range(n):
#     s = raw_input().split()
#     cmd = s[0]
#     args = s[1:]
#     if cmd !="print":
#         cmd += "("+ ",".join(args) +")"
#         eval("l."+cmd)
#     else:
#         print l