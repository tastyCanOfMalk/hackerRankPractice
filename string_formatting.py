# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(n):
    width = len(bin(n)[2:])
    if 1 <= n <= 99:
        for number in range(n):
            k = number+1
            dec = str(k)
            octal = str(oct(k))[2:]
            hexa = str(hex(k).upper())[2:]
            bina = str(bin(k))[2:]
            print(dec.rjust(width,' '),octal.rjust(width,' '),hexa.rjust(width,' '),bina.rjust(width,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)