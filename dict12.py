n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
reversed_d = {}
for key, value in d.items():
    reversed_d[value] = key
for value, key in reversed_d.items():
    print(value, key)