#Функция invert_digits(k) возвращает число с обратным порядком цифр. Перевернуть пять данных чисел
def invert_digits(k):
    return int(str(k)[::-1])
for i in range(5):
    k = int(input())
    print(invert_digits(k))