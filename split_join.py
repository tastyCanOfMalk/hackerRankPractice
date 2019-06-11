# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    s_split = line.split()
    s_join = "-".join(s_split)
    return(s_join)

split_and_join("my testy string")