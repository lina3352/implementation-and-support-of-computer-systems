#Функция triangle_ps(a) возвращает периметр P = 3·a и площадь S = a2·√3/4 равностороннего
#треугольника. Найти P и S трёх данных сторон
import math
def triangle_ps(a):
    return 3 * a, a ** 2 * math.sqrt(3) / 4
for i in range(3):
    a = float(input())
    p, s = triangle_ps(a)
    print(p, s)