# https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# get n, create empty list
n = int(input())
# n=4
arr = [[0 for _ in range(2)] for _ in range(n)]

# test inputs
# arr[0][0]= "sona"
# arr[0][1]= -25.001
# arr[1][0]= "mona"
# arr[1][1]= -25.0001
# arr[2][0]= "mini"
# arr[2][1]= -25.000
# arr[3][0]= "rita "
# arr[3][1]= -25.0
# arr[4][0]= "Vikas"
# arr[4][1]= 21

# loop to get inputs
count = 0
while count < n and 2 <= n <= 5: 
    arr[count][0] = input()
    arr[count][1] = input()
    count+=1

# sort ascending
arr.sort(key=lambda x: x[1])

# remove min value(s)
removes = []
min1 = arr[0]

arr.remove(arr[0])

for x in range(len(arr)):
    if min1[1] == arr[x][1]:
        removes.append(x)
  
for y in range(len(removes)):
    arr.remove(arr[removes[0]])

# store second min, then remove it
min2 = arr[0]
arr.remove(arr[0])

# store matching values
store=[]
# for x in range(n-2):
for x in range(n - (len(removes)+2)):
    if min2[1] == arr[x][1]:
        store.append(arr[x])
    
if not store:
    print(min2[0])
else:
    newlist=[min2[0],store[0][0]]
    newlist.sort()
    for x in range(len(newlist)):
        print(newlist[x])


# solution from discussion
# marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))