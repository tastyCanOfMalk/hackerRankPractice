# https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge

def count_substring(string, sub_string):
    sub_len = len(sub)
    count=0
    for letter in range(len(string)):
        if string[letter:letter+sub_len] == sub_string:
            count+=1
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)