https://www.hackerrank.com/challenges/designer-door-mat

n,m = map(int, input().split())

pattern = '.|.'
top=''

for x in range(int(n//2)):
    top+=((pattern*(2*x+1)).center(m,'-'))
    top+='\n'
    
rug_center = 'WELCOME'.center(m,'-')

print(top+rug_center+top[::-1])


# from discussion:
# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))