lenguajesfavoritos = {'Juan': 'python', 'Sara': 'c', 'Eduardo': 'rust', 'Agustina': 'c#'}
personaspreguntar = ['Juan', 'Sara', 'Eduardo', 'Agustina', 'Carlos', 'Lucía']

for persona in personaspreguntar:
    if persona in lenguajesfavoritos:
        print(f"Gracias, {persona}, por responder la encuesta.")
    else:
        print(f"Hola {persona}, te invitamos a participar en la encuesta sobre lenguajes favoritos.")
