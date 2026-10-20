#Функция triangle_p(a, h) возвращает периметр равнобедренного треугольника по основанию a
#и высоте h к основанию; боковая сторона b2 = (a/2)2 + h2. Найти периметры трёх треугольников
import math
def triangle_p(a, h):
    b = math.sqrt((a / 2) ** 2 + h ** 2)
    return a + 2 * b
for i in range(3):
    a = float(input())
    h = float(input())
    print(triangle_p(a, h))