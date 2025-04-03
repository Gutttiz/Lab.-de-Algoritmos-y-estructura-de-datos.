mascota1 = {
    "tipo": "Perro",
    "nombre": "Ciro",
    "dueño": "Gutti"
}

mascota2 = {
    "tipo": "Gato",
    "nombre": "Campanita",
    "dueño": "Ana"
}

mascota3 = {
    "tipo": "Loro",
    "nombre": "Roberto",
    "dueño": "Facundo Lasche"
}

mascota4 = {
    "tipo": "Tucan",
    "nombre": "Granes",
    "dueño": "Vigna"
}

mascotas = [mascota1, mascota2, mascota3, mascota4]

for mascota in mascotas:
    print(f"Tipo de animal: {mascota['tipo']}")
    print(f"Nombre: {mascota['nombre']}")
    print(f"Dueño: {mascota['dueño']}")
    print()
