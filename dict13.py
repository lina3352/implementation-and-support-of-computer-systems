n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    d[name] = [price, qty]
total = 0
best_name = ""
best_cost = -1
for name, values in d.items():
    price, qty = values
    cost = price * qty
    total += cost
    if cost > best_cost:
        best_cost = cost
        best_name = name
print(total)
print(best_name)