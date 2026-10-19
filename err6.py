#Та же задача, что Err5, но с двумя ветками: 
#нечисловой индекс — «Ошибка ввода», индекс вне границ — «Нет такого символа».
s = input()
try:
    i = int(input())
    print(s[i])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")