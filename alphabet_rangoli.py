# https://www.hackerrank.com/challenges/alphabet-rangoli



def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    middle_for = alphabet[:size]
    middle_rev = middle_for[::-1]
    middle_rev = middle_rev[:size-1]
    middle = middle_rev + middle_for
    middle = '-'.join(middle)

    m = len(middle)//2
    k = middle
    l=''

    for row in range(size-1):
        k = k[0:m-2] + k[m+2:]
        k = k.center(len(middle),'-')
        l += k
        l += '\n'
        
    print(l[::-1])
    print(middle)
    print(l)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# solution not accepted for some reason
# discussion solution:
# import string
# alpha = string.ascii_lowercase

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))