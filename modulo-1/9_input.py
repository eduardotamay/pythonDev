#input sirve para obtener valores desde fuera
#Esta funcion recibe como argumento un mensaje especifico

edad = int(input("Ingresa tu edad: "))
print(edad)
altura = float(input("Ingresa tu altura: "))
print(altura)

acceso = input("¿Permites el acceso? (si/no)")
admin_acceso = acceso == 'si'
print(admin_acceso)