from function import mostrar_menu, mostrar_inmuebles, editar_inmueble, buscar_inmuebles_por_presupuesto, cambiar_estado, agregar_inmueble, eliminar_inmueble


inmuebles = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
             {'año': 2016, 'metros': 80, 'habitaciones': 2,
                 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
             {'año': 2000, 'metros': 180, 'habitaciones': 4,
                 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
             {'año': 2015, 'metros': 95, 'habitaciones': 3,
                 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
             {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

while True:
    mostrar_menu()
    opcion = input('Ingrese una opción: ')
    if not opcion.isdigit():
        print('Ingrese una opción numérica válida')
        continue

    opcion = int(opcion)

    if opcion == 1:
        mostrar_inmuebles(inmuebles)
    if opcion == 2:
        agregar_inmueble(inmuebles)
    elif opcion == 3:
        editar_inmueble(inmuebles)
    elif opcion == 4:
        eliminar_inmueble(inmuebles)
    elif opcion == 5:
        cambiar_estado(inmuebles)
    elif opcion == 6:
        buscar_inmuebles_por_presupuesto(inmuebles)
    elif opcion == 7:
        break
    else:
        print("Opción inválida. Intente nuevamente.")
