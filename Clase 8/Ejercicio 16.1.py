glosario = {
    "variable": "Guarda un valor.",
    "función": "Hace una tarea.",
    "bucle": "Repite alguna cosa.",
    "lista": "Guarda cosas.",
    "condicional": "Si se cumple una condición, hace algo."
}

for palabra, significado in glosario.items():
    print(palabra, ":", significado)

glosario["Tupla"] = "Si bien no se puede cambiar el contenido de una tupla, sí se las puede redefinir."
glosario["Conjunto"] = "Colección que no esta ordenada."
glosario["Cadena"] = "Secuencia de letras o numeros."
glosario["Diccionario"] = "Permiten almacear datos rapidamente."
glosario["Módulo"] = "Archivo que contiene definiciones."

for palabra, significado in glosario.items():
    print(f"{palabra} : {significado}")
