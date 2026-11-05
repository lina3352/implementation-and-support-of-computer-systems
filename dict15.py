n = int(input())
a = {}
for i in range(n):
    key = input()
    value = int(input())
    a[key] = value
m = int(input())
b = {}
for i in range(m):
    key = input()
    value = int(input())
    b[key] = value
ignored = 0
for key, value in b.items():
    if key in a:
        ignored += 1
    else:
        a[key] = value
print(len(a))
print(ignored)