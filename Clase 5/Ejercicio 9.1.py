import os 
os.system ("cls")
lugares = ("Italia", "Grecia", "España", "Portugal", "Letonia")
print (f"Lista en forma original: {lugares}")
print(f"Lista en orden alfabetico:{sorted(lugares)}")
print (f"La lista sigue en forma original: {lugares}")

lugaresalreves = sorted(lugares)
lugaresalreves.reverse()
print(lugaresalreves)

lugaresalreves.reverse()
print(f"Lista en orden alfabetico: {lugaresalreves}")

print(f"La lista sigue en forma original: {lugares}")
print(f"Lista en orden alfabetico:{sorted(lugares)}")
lugaresalreves.reverse()
print(f"Lista en orden alfabetico: {lugaresalreves}")

