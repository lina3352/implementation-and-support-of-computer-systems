#Дан список A из N чисел. Генератором вывести элементы, большие среднего, и само среднее
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
avg = sum(a) / n
big = [x for x in a if x > avg]
print(big)
print(avg)