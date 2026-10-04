#if5. Даны три целых числа. Найти количество положительных и количество отрицательных чисел в исходном наборе.
a = int(input())
b = int(input())
c = int(input())
count = (a > 0) + (b > 0) + (c > 0)
count1 = (a < 0) + (b < 0) + (c < 0)
print(count)
print(count1)
