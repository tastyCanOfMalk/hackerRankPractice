# https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
grades = [[0 for _ in range(4)] for _ in range(n)]

if 2 <= n <= 10:
    for x in range(n):
        a,b,c,d = input().split()
        grades[x][0] = a
        grades[x][1] = float(b)
        grades[x][2] = float(c)
        grades[x][3] = float(d)
    lookup = input()

for x in range(n):
    if lookup == grades[x][0]:
        avg = (grades[x][1]+grades[x][2]+grades[x][3])/3.00
        print("%.2f" % avg)

# discussion solution
# if __name__ == '__main__':
#     n = int(raw_input())
#     student_marks = {}
#     for _ in range(n):
#         line = raw_input().split()
#         name, scores = line[0], line[1:]
#         scores = map(float, scores)
#         student_marks[name] = scores
#     query_name = raw_input()
#     query_scores = student_marks[query_name]
#     print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))

# another
# marks = {}
# for _ in range(int(input())):
#     line = input().split()
#     marks[line[0]] = list(map(float, line[1:]))
# print('%.2f' %(sum(marks[input()])/3))