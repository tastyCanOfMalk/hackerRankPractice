# https://www.hackerrank.com/challenges/matrix-script/problem

# # get dimensions
n, m = map(int, input().split())

# # create empty array
arr = [[0 for _ in range(m)] for _ in range(n)]

# get matrix code
for x in range(n):
    a = input().split()
    for y in range(m):
        arr[x][y] = a[y]    



# # test
# n = 7
# m = 3
# arr = [[0 for _ in range(m)] for _ in range(n)]
# for word in arr:
#     print(word)

# # get matrix input
# arr[0] = ['T', 's', 'i']
# arr[1] = ['h', '%', 'x']
# arr[2] = ['i', ' ', '#']
# arr[3] = ['s', 'M', ' ']
# arr[4] = ['$', 'a', ' ']
# arr[5] = ['#', 't', '%']
# arr[6] = ['i', 'r', '!']


# discussion answer
# import re

# n, m = map(int, input().split())
# a, b = [], ""
# for _ in range(n):
#     a.append(input())

# for z in zip(*a):
#     b += "".join(z)

# print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", b))