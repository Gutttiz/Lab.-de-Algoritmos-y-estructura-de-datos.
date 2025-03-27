usuarios_actuales = ["ana", "juani", "marcela", "luis", "pedro"]

usuarios_nuevos = ["juani", "Luis", "maria", "PEDRO", "juan"]

for nuevo_usuario in usuarios_nuevos:
    if nuevo_usuario.lower() in [usuario.lower() for usuario in usuarios_actuales]:
        print(f"El nombre de usuario '{nuevo_usuario}' ya está en uso. Por favor, elegi otro.")
    else:
        print(f"El nombre de usuario '{nuevo_usuario}' está disponible.")
