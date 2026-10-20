#Функция add_left_digit(d, k) возвращает число k с приписанной слева цифрой d (1–9).
#Приписать к данному K слева D1 и D2, печатая каждый шаг
def add_left_digit(d, k):
    return int(str(d) + str(k))
k = int(input())
d1 = int(input())
d2 = int(input())
k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)