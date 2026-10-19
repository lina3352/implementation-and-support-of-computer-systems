#Прочитать целое число. При ошибке вывести текст исключения и его тип отдельными строками,
#пользуясь as e и type(e). При успехе вывести само число.
try:
    n = int(input())
except ValueError as e:
    print(e)
    print(type(e))
else:
    print(n)