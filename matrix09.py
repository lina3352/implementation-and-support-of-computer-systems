m = int(input())
n = int(input())
a = []
for i in range(m):
    a.append([int(x) for x in input().split()])
for row in a[1::2]:
    print(row)