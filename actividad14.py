equipos_lista = []
salida=""

while salida != "fin":
    nombre_equipo = input("introduce el nombre del equipo: ")
    equipos_lista.append(nombre_equipo)
    salida = input("has terminado, introduzca fin para acabar")

print("equipos introducidos:")
print(equipos_lista)
print(len(equipos_lista))