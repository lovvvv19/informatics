import math 

x=float(input("Введите значение х: "))
y=float(input("Введите значение y: "))
z=float(input("Введите значение z: "))

a=sqrt(x**3/2)-math.sin(y)
b=(e**2/3)-math.cos(y)+z+math.log(y)

print(f"Получено значение функции a={a}")
print(f"Получено значение функции b={b}")
