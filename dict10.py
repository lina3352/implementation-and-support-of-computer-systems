n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    d[name] = price
for name, price in d.items():
    print(f"{name}: {price}")