# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

# calculadora Miri 
# declaracion de variables 

numero_1 = input("ingrese un numero: ")
nuemro_2 = input("ingrese otro numero: ")

suma = float(numero_1) + float(nuemro_2)
print("el resultado es",suma)

resta = float(numero_1) - float(nuemro_2)
print("el resultado de la resta es",resta)

multipli = float(numero_1) * float(nuemro_2)
print("el resultado de la multiplicacion es",multipli)

divi = float(numero_1) / float(nuemro_2)
print("el resultado de la division es",divi)

exponente = float(numero_1) ** float(nuemro_2)
print("el resultado de la potencia es",exponente)

print(" ""Gracias por Participar")