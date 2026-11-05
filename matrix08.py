m = int(input())
n = int(input())
a = []
for i in range(m):
    a.append([int(x) for x in input().split()])
k = int(input())
print([row[k - 1] for row in a])