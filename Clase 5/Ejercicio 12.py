import os, time
os.system ('cls')
lista = []
con = 1
for i in range (3):
    pizza = input (f"decime la {i+1} pizza: ")
    lista.append (pizza)

for pizza in lista:
    print(f"mi pizza favorita numero {con} es la de {pizza}")
    con = con +1

pizzas_amigo = lista [:]

lista.append(input("seleccione otro tipo de pizza: "))
pizzas_amigo.append(input("seleccione otro tipo de pizza para la otra lista: "))

print (f"lista original: {lista}")
print (f"lista secundaria: {pizzas_amigo}")
