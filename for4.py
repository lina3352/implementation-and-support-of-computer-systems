#for4. Дано вещественное число — цена 1 кг конфет. 
#Вывести стоимость 1, 2, ..., 10 кг конфет.
money = float(input())
for i in range(1, 11):
    print(i * money)