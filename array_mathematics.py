# https://www.hackerrank.com/challenges/np-array-mathematics/problem
import numpy

# numbers = [int(n) for n in input().split()]
# print(numbers)
# print(numbers[0])
# print(numbers[1])

# numbers = list(map(int, input().split(' ')))
# print(numbers)
# print(numbers[0])
# print(numbers[1])

# s = input()
# numbers = list(map(int, s.split()))
# print(numbers[0])
# print(numbers[1])

# s = input()
# n,m = list(map(int, s.split()))
# print(n)
# print(m)

# # get dimensions of array
# n, m = list(map(int, input().split()))

# # get first row of inputs
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# # a1[0] = a
# # a1[1] = b

# a = numpy.array([a])
# b = numpy.array([b])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(a ** b)


# answer from discussion
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')