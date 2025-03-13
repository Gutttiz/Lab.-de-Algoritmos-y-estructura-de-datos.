import random

#Crea una lista de 1 a 100
numeros = [random.randint(1, 100) for _ in range(10)]

#Ordeno la lista de menor a mayor
orden_ascendente = sorted(numeros)


#Mostrar en la pantalla
print("Lista original:", numeros)
print("Lista ordenada de menor a mayor:", orden_ascendente)

