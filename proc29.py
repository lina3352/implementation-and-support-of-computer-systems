#Функция digit_count(k) возвращает количество цифр k (> 0). Найти количество цифр пяти чисел
def digit_count(k):
    return len(str(k))
for i in range(5):
    k = int(input())
    print(digit_count(k))