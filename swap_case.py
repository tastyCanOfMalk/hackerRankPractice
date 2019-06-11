# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    n=''
    for letter in s:
        if 0 < len(s) <= 1000:
            if letter.islower(): 
                n+=letter.upper()
            else:
                n+=letter.lower()        
    return(n)

swap_case('hYEYY')