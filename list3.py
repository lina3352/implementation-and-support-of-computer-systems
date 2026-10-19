#Дан список A из N чисел. Вывести сумму элементов и произведение элементов с чётными
#индексами (0, 2, 4...)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
p = 1
for x in a[::2]:
    p *= x
print(sum(a))
print(p)