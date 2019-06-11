# https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input())
a = [0 for _ in range(n)]
b = list(map(int, input().split()))

for c in range(n):
    a[c] = b[c]

d = hash(tuple(a))
print(d)


