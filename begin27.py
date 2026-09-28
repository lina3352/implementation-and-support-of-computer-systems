#begin27. Дано число A. Вычислить A8, используя вспомогательную переменную и три операции умножения. 
#Для этого последовательно находить A2, A4, A8. Вывести все найденные степени числа A.
a = float(input())
temp = a * a 
print(temp)
temp = temp * temp
print(temp)
temp = temp * temp
print(temp)
