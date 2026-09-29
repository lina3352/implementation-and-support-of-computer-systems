#begin34. Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей. 
#Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, 
#а также во сколько раз шоколадные конфеты дороже ирисок.
X = float(input())
A = float(input())
Y = float(input())
B = float(input())
price = A / X
price1 = B / Y 
ratio = price / price1
print(price)
print(price1)
print(ratio)
