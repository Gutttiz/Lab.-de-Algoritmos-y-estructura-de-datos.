
persona = {
    "nombre": "Juan",
    "apellido": "Pera",
    "edad": 30,
    "ciudad": "Buenos Aires"}
print(persona)

persona2 = {
    "nombre": "Pedro",
    "apellido": "Gonza",
    "edad": 80,
    "ciudad": "Madrid"                                                                                                                                                                                                      
}

persona3 = {
    "nombre": "Facundo",
    "apellido": "Laschera",
    "edad": 32,
    "ciudad": "Ciudad de México"
}
gente = [persona, persona2, persona3]

for persona in gente:
    print(f"Nombre: {persona['nombre']}")
    print(f"Apellido: {persona['apellido']}")
    print(f"Edad: {persona['edad']}")
    print(f"Ciudad: {persona['ciudad']}")
    print()
