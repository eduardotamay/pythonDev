#Nos permite crear una sublista a partir de la lista actual

#Ejemplo
#                  0        1      2      3     4
lenguajesProg = ['Python','Ruby','PHP','Java','Rust']

#Obtener elementos a partir del 2 hasta el 5 [start:end]
sublitaProg = lenguajesProg[2:5]

#Considera el indice[3] hasta el ultimo [start:end]
sublitaProgLast = lenguajesProg[3:]

#Considera el primero hasta el indice [3] [start:end]
sublistaPrincipio = lenguajesProg[:3]

#Sublistas con saltod dentro de la lista actual [start:end:skip]
sublistaConSalto = lenguajesProg[1:5:2]

#Sublista al inverso
sublistaInverso = lenguajesProg[::-1]

#Lenguajes completos
print(lenguajesProg)

print(sublitaProg)

print(sublitaProgLast)

print(sublistaPrincipio)

print(sublistaConSalto);

print(sublistaInverso);