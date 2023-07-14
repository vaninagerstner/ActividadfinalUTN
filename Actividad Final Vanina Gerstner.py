

#menú
def menu():
    print("\n")
    print ("a) Mostrar la lista ordenada de alumnos.")
    print ("b) Mostrar la lista ordenada de alumnos con sus notas.")
    print ("c) Mostrar la lista ordenada de alumnos con sus promedios.")
    print ("d) Mostrar la nota media de todos los alumnos.")
    print ("e) Mostrar la nota media de los alumnos aprobados.")
    print ("f) Mostrar la nota media de los alumnos suspendidos.")
    print ("g) Salir del programa")
    opcion = input("Elija una opción de las que verá a continuación: ")
    return opcion.lower()
     

# muestra nombres ("opcion a")
def alumnos_ordenados(alumnos):
    for alumno in sorted(alumnos): 
        print(alumno)
    print("\n")

# muestra lista de nombres y notas("opcion b")
def alumnos_ordenados_con_notas(alumnos): 
    for alumno in sorted(alumnos):
        notas = alumnos[alumno] 
        print(f"{alumno}: {notas}")
    print("\n")
        
# muestra lista ordenada de alumnos con sus promedios("opcion c")
def alumnos_ordenados_con_promedios(alumnos):
    for alumno in sorted(alumnos):
        notas = alumnos[alumno]
        promedio = sum(notas) / len(notas) 
        print(f"{alumno}: promedio: {round(promedio, 2)}")
    print("\n")

# muestra la nota media de todos los alumnos ("opcion d")
# lista para guardar todas las notas de todos los alumnos
def nota_media(alumnos):
    todas_las_notas = []
    for notas in alumnos.values():
        todas_las_notas.extend(notas)
    promedio_notas = sum(todas_las_notas) / len(todas_las_notas)
    print(f"El promedio de todas las notas es de {round(promedio_notas, 2)}.")
    print("\n")

# muestra la nota media de los alumnos aprobados("opcion e")
def nota_media_aprobados(alumnos):
    notas_aprobados = [] 
    for notas in alumnos.values():
        promedio = sum(notas) / len(notas) 
        if promedio >= 6:
            notas_aprobados.append(promedio)
    if notas_aprobados:
        promedio_notas_aprobadas = sum(notas_aprobados) / len(notas_aprobados)
        print(f"El promedio de todas las notas de alumnos probados es de {round(promedio_notas_aprobadas, 2)}.")
    else:
        print("No hay alumnos aprobados.")
    print("\n")
    
# muestra la nota media de los alumnos suspendidos("opcion f")
def nota_media_suspendidos(alumnos):
    notas_suspendidos = [] 
    for notas in alumnos.values():
        promedio = sum(notas) / len(notas) 
        if promedio < 6:
            notas_suspendidos.append(promedio)
    if notas_suspendidos:
        promedio_notas_suspendidos = sum(notas_suspendidos) / len(notas_suspendidos)
        print(f"El promedio de las notas de todos los alumnos suspendidos es de {round(promedio_notas_suspendidos, 2)}.")
    else:
        print("No hay alumnos suspendidos.")
    print("\n")

    

print("A continuación debe cargar los/as alumnos/as y las notas para luego poder filtrar según el menú de opciones.")

# diccionario
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos de su clase: "))
alumnos = {} 

for i in range(cantidad_alumnos):
    notas =[] 

    nombre_alumno = input("Ingrese el nombre completo del alumno: ")
    cant_notas = int(input("Ingrese la cantidad de notas (entre 3 y 6): "))

    while cant_notas < 3 or cant_notas > 6:
        print("Debe ingresar una cantidad mínima de 3 o máxima de 6 notas.")
        cant_notas = int(input("Ingrese la cantidad de notas (entre 3 y 6): "))

    for i in range(cant_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
        
    alumnos[nombre_alumno] = notas 
    print("\n")

opcion = menu()
while opcion != "g":
    if opcion == "a":
        print("\n")
        print("Lista ordenada de alumnos")
        alumnos_ordenados(alumnos)
    elif opcion == "b":
        print("\n")
        print("Lista ordenada de alumnos con las notas")
        alumnos_ordenados_con_notas(alumnos)
    elif opcion == "c":
        print("\n")
        print("Lista ordenada de promedios de alumnos")
        alumnos_ordenados_con_promedios(alumnos)
    elif opcion == "d":
        print("\n")
        print("Notas promedio")
        nota_media (alumnos)
    elif opcion == "e":
        print("\n")
        print("Promedio de notas de alumnos aprobados")
        nota_media_aprobados(alumnos)
    elif opcion == "f":
        print("\n")
        print("Promedio de notas de alumnos desaprobados")
        nota_media_suspendidos(alumnos)
    else:
        print("Opcion inválida. Elija una opción válida")
    opcion = menu()
    
print("Usted ha salido del programa.")

