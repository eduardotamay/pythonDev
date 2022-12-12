#Las listas es un tipo de dato almacenados dentro del lenguaje python
# son parecidas a arrays en otros lenguajes.
# recomendable crear un solo tipo de dato dentro de la lista

listNames = ['Jose','Juan','Karina','Maria']

#agrega un nuevo elemento dentro de la lista
listNames.append('Alberto')

#imprime la ubicacion de este elemento
print(listNames.index('Juan'))

#elimina el elemento
listNames.remove('Karina')

#crea una lista a partir de la otra sin modificar el original
print(sorted(listNames,reverse=True))

#los ordena de forma alfabetico
listNames.sort();

#Actualizar un valor dentro del listado
listNames[2] = 'Carlos'

print(listNames)