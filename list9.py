#Дан список A из N чисел. Вывести элементы, большие среднего арифметического всех
#элементов, и их количество
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
avg = sum(a) / n
big = []
for x in a:
    if x > avg:
        big.append(x)
print(big)
print(len(big))