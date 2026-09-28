#begin28. Дано число A. Вычислить A15, используя две вспомогательные переменные и пять операций умножения. 
#Для этого последовательно находить A2, A3, A5, A10, A15. Вывести все найденные степени числа A.
a = float(input())
temp = a * a
print(temp)
temp1 = temp * a 
print(temp1)
temp1 = temp1 * temp
print(temp1)
temp = temp1 * temp1
print(temp)
temp1 = temp1 * temp
print(temp1)
