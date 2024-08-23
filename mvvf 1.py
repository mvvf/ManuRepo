# Operadores de lenguaje Python
print(" ")

# Operadores aritméticos

print("Ejercios con operaciones atirméticas, por ejemplo:")
print(" ")
print(f"Suma: 10 + 3 = {10 + 3}")
print(" ")
print(f"Resta: 10 - 3 = {10 - 3}")
print(" ")
print(f"Multiplicación: 10 * 3 = {10 * 3}")
print(" ")
print(f"División: 10 / 3 = {10 / 3}")
print(" ")
print(f"Módulo: 10 % 3 = {10 % 3}")
print(" ")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(" ")
print(f"División entera: 10 // 3 = {10 // 3}")
print("""

a = 10
b = 3


suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000
""")




# Operadores de comparación

print(" ")
print(" ")
print("Operadores de comparación, por ejemplo: ")
print(" ")
print(f"Igualdad: 10 == 3 es {10 == 3}") #Indica si 10 es igual a 3
print(" ")
print(f"Desigualdad: 10 != 3 es {10 != 3}") #Indica que 10 no es igual a 3
print(" ")
print(f"Mayor que: 10 > 3 es {10 > 3}") #Indica si 10 es mayor que 3
print(" ")
print(f"Menor que: 10 < 3 es {10 < 3}") #Indica si 10 es menor que 3
print(" ")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}") #Indica si 10 es igual o mayor que 3
print(" ")
print(f"Menor o igual que: 10 <= 3 es {10 <= 3}") #Indica si 10 es igual o menor que 3
print(" ")
print(" ")

# Operadores lógicos
print("Ejercicios con operadores lógicos ")
print(f"AND : 10 + 3 = 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR : 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 13 or 5 - 1 == 4}")
print(f"NOT : 10 + 3 == 14 es { not 10 + 3 == 14}")
print("""

a = 10
b = 3

igual = a == b   # False
diferente = a != b   # True
mayor que = a > b   # True
menor que = a < b   # False
mayor o igual = a >= b   # True
menor o igual = a <= b   # False""")
print(" ")




# Operadores de asignación

print("Ejercicios con operadores de asignación ")
my_number = 11  # asignación

print ("El número es inicial es 11")

my_number += 1   # suma cualquier cantidad al número asignado
print (my_number)
my_number -= 1   # resta cualquier cantidad al número asignado
print(my_number)
my_number *= 2   # multiplica por cualquier cantidad al número asignado
print (my_number)
my_number /= 2  # divide en cualquier cantidad al número asignado
print(my_number)
my_number %= 2 # (módulo) determina la diferencia o restante en la división al número asignado
print (my_number)

# Operadores de identidad

my_new_number = 1.0

print(f"my_number is my_new_number es {my_number is my_new_number}")