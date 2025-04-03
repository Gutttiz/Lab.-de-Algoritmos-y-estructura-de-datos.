
rios = {
    'Nilo': 'Egipto',
    'Amazonas': 'Brasil',
    'Misisipi': 'Estados Unidos'}

for rio, pais in rios.items():
    print(f"El {rio} pasa por {pais}.")

for rio in rios.keys():
    print(rio)
    
for pais in rios.values():
    print(pais)
