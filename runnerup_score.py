# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen

import numpy

n = int(input())
x = list(map(int, input().split()))
x.sort()
x = numpy.unique(x)

if 2 <= n <= 10 and all(-100 <= i <= 100 for i in x):
    print(x[-2])