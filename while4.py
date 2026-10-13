#Дано целое число N (> 0). 
#Если оно является степенью числа 3, то вывести TRUE, если не является — вывести FALSE.
n = int(input())
while n % 3 == 0:
    n = n // 3
if n == 1:
    print("TRUE")
else:
    print("FALSE")