# https://www.hackerrank.com/challenges/text-wrap/

def wrap(string, max_width):
    q = ''
    if 0 < len(string) < 1000 and 0 < max_width < len(string):
        lis = range(0,len(string),max_width)
        for letter in lis:
            q+=(string[letter:letter+max_width])
            q+='\n'
        return q

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)