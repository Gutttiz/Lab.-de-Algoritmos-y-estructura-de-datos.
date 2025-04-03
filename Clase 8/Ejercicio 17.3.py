lugares_favoritos = {
    'Lasche': ['París', 'Nueva Jersey', 'Nueva York'],
    'Guti': ['La plata', 'Salta'],
    'Leo': ['Tuseño', 'Tuco', 'Suslo'] #Estas respuestas las puso Leonardo Borgo
}

for persona, lugares in lugares_favoritos.items():
    print(f"Lugares favoritos de {persona}:")
    for lugar in lugares:
        print(f"{lugar}")
    print() 

