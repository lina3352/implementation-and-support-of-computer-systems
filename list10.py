#Дан список из N строк. Вывести самую длинную и самую короткую строку (первую из
#встретившихся) и их длины
n = int(input())
a = []
for i in range(n):
    a.append(input())
longest = a[0]
shortest = a[0]
for s in a:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s
print(longest)
print(shortest)
print(len(longest))
print(len(shortest))