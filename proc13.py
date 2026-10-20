#Функция sort_dec3(a, b, c) возвращает три значения по убыванию. Упорядочить два набора
def sort_dec3(a, b, c):
    return sorted([a, b, c], reverse=True)
for i in range(2):
    a = float(input())
    b = float(input())
    c = float(input())
    a, b, c = sort_dec3(a, b, c)
    print(a, b, c)