def mostrar_menu():
    print(f'--------------- Menú ---------------')
    print(f'1. Mostrar lista de inmuebles')
    print("2. Agregar inmueble")
    print("3. Editar inmueble")
    print("4. Eliminar inmueble")
    print("5. Cambiar estado de inmueble")
    print("6. Buscar inmuebles por presupuesto")
    print("7. Salir")
    print("-----------------------------")


def mostrar_inmuebles(inmuebles):
    i = 1
    for inmueble in inmuebles:
        print(f'Inmueble {i}:', end=' ')
        for clave, valor in inmueble.items():
            print(f'{clave}: {valor} ', end=' ')
        i += 1
        print('')


def agregar_inmueble(lista):
    print('---- Agregar Inmueble ----')
    nuevo_inmueble = {
        'año': int(input("Año: ")),
        'metros': int(input("Metros: ")),
        'habitaciones': int(input("Habitaciones: ")),
        'garaje': input("Garaje (s/n): ").lower() == 'n',
        'zona': input("Zona (A/B/C): ").upper(),
        'estado': input("Estado (Disponible/Reservado/Vendido): ")
    }
    if agregar_inmueble_lista(lista, nuevo_inmueble):
        print('Inmueble agregado correctamente.')
    else:
        print('No se pudo agregar el inmueble. Por favor verifique los datos ingresados')


def agregar_inmueble_lista(lista, nuevo_inmueble):
    if nuevo_inmueble['garaje'] == 'n':
        nuevo_inmueble['garaje'] = False
        lista.append(nuevo_inmueble)
        return True
    else:
        nuevo_inmueble['garaje'] = True
        lista.append(nuevo_inmueble)
        return True



def editar_inmueble(inmuebles):
    print(f'')


def agregar_inmueble(inmuebles):
    print(f'')


def eliminar_inmueble(inmuebles):
    print(f'')


def cambiar_estado(inmuebles):
    print(f'')


def buscar_inmuebles_por_presupuesto(inmuebles):
    print(f'')
