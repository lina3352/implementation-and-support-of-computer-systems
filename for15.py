#for15. Дано вещественное число A и целое число N (> 0).
#Найти A в степени N: A N = A · A · ... · A (число A перемножается N раз).
a = float(input())
n = int(input())
p = 1
for i in range(n):
    p *= a
print(p)