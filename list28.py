#Дан список из N строк и буква. Генератором вывести строки, начинающиеся с этой буквы
#(первый символ строки)
n = int(input())
a = []
for i in range(n):
    a.append(input())
c = input()
print([s for s in a if s[0] == c])