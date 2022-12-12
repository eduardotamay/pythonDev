misCursos  = ['Python','Java','PHP','Javascript','Python']
misCursosPremium = ['Docker','Rails','AWS','Node js']

#Me permite agregar nuevos elemento a mi lista
misCursos.append('MongoDB')
print(misCursos)

#Me permite conocer la longiyud de mi lista
totalCursos = len(misCursos)
print(totalCursos)

#Me permite insertar un elemento en un indice en concreto
misCursos.insert(3,'Laravel')
misCursos.insert(0,'Django')
print(misCursos)

#Permite que mi lista se extienda a partir de otra lista
#Se unifican
misCursos.extend(misCursosPremium)
print(misCursosPremium)
print(misCursos)

#Permite eliminar elementos dentro de mi lista
misCursos.remove('Laravel')
#Permite eliminar con indices
del misCursos[3]
print(misCursos)

#permite limpiar mi lista
misCursos.clear()
print(len(misCursos))