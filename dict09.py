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
common = input()
a.update(b)
print(len(a))
print(a[common])