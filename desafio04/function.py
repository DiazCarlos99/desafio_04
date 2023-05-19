
def mostrar_menu():
    print(f'\n--------------- Menú ---------------')
    print(f'1- Mostrar lista de inmuebles')
    print("2- Agregar inmueble")
    print("3- Editar inmueble")
    print("4- Eliminar inmueble")
    print("5- Cambiar estado de inmueble")
    print("6- Buscar inmuebles por presupuesto")
    print("7- Salir")
    print("-----------------------------")

def mostrar_inmuebles(lista, precio=False):
    print('\n*******************************')
    print('***** Listado de inmuebles *****')
    print('********************************')
    i = 1
    for inmueble in lista:
        print(f'inmueble {i}: ')
        print('Año:', inmueble['año'])
        print('Metros:', inmueble['metros'])
        print('Habitaciones: ', inmueble['habitaciones'])
        print('Garaje:', 'Sí' if inmueble['garaje'] else 'No')
        print('Zona:', inmueble['zona'])
        print('Estado:', inmueble['estado'])
        if precio:
            print('Precio:', inmueble['precio'])
        print('***********************')
        i += 1

def validar_inmueble(inmueble):
    if (
        inmueble['año'] < 2000
        or inmueble['metros'] < 60
        or inmueble['zona'] not in ['A', 'B', 'C']
        or inmueble['habitaciones'] < 2
        or inmueble['estado'] not in ['Reservado', 'Disponible', 'Vendido']
    ):
        return False
    return True

def agregar_inmuebles(lista):
    print('\n****************************')
    print('***** Agregar inmueble *****')
    print('****************************')
    nuevo_inmueble = {
        'año': int(input('Año: ')),
        'metros': int(input('Metros: ')),
        'habitaciones': int(input('Habitaciones: ')),
        'garaje': input("Garaje (s/n): ").lower() == 's',
        'zona': input('Zona (A/B/C): ').upper(),
        'estado': input('Estado (Disponible/Reservado/Vendido): ')
    }
    if validar_inmueble(nuevo_inmueble):
        lista.append(nuevo_inmueble)
        print('***** Inmueble agregado correctamente *****')
    else:
        print('No se pudo agregar el inmueble. Por favor verifique los datos ingresados')

def editar_inmuebles(lista):
    mostrar_inmuebles(lista)
    print('\n**************************************************')
    print('***** SELECCIONE EL INMUEBLE SEGUN SU INDICE *****')
    print('**************************************************')
    indice = int(input('Indice: '))
    if indice >= 0 and indice <= len(lista):
        inmueble = lista[indice - 1]
        print(f'***** Editar el inmueble: {indice} *****')
        print('***** Ingrese los nuevos Datos *****')
        inmueble['año'] = int(input('Año: '))
        inmueble['metros'] = int(input('Metros: '))
        inmueble['habitaciones'] = int(input('Habitaciones: '))
        inmueble['garaje'] = input('Garaje (s/n): ').lower() == 's'
        inmueble['zona'] = input('Zona (A/B/C): ').upper()
        inmueble['estado'] = input('Estado (Disponible/Reservado/Vendido): ')
        if validar_inmueble(inmueble):
            lista.append(inmueble)
            print('\n**************************************************')
            print('********* Inmueble agregado correctamente ********')
            print('**************************************************')
        else:
            print(
                'No se pudo agregar el inmueble. Por favor verifique los datos ingresados')
    else:
        print('Ha ingresado un indice no valido')

def eliminar_inmueble(lista):
    mostrar_inmuebles(lista)
    print('\n**************************************************')
    print('***** SELECCIONE EL INMUEBLE SEGUN SU INDICE *****')
    print('**************************************************')
    indice = int(input('Indice: '))
    indice = indice - 1
    print(f'Esta segurdo de eliminar el inmuble {lista[indice]}')
    confirmacion = input('s/n: ')
    if confirmacion == 's':
        lista.pop(indice)
        print('\n****************************************************')
        print('***** El inmueble se ha eliminado correctamente *****')
        print('*****************************************************')
        mostrar_inmuebles(lista)
    else:
        print(f'No se ha eliminado el inmueble {lista[indice]}')

def cambiar_estado(lista):
    mostrar_inmuebles(lista)
    print('\n**************************************************')
    print('***** SELECCIONE EL INMUEBLE SEGUN SU INDICE *****')
    print('**************************************************')
    indice = int(input('Indice: '))
    indice = indice - 1
    print(f'Ha seleccionado el inmueble: {lista[indice]}')
    lista[indice]['estado'] = input('Estado (Disponible/Reservado/Vendido: ')
    if validar_inmueble(lista[indice]):
        print('\n****************************************')
        print('***** Se ha actualizado el estado correctamente *****')
        print('*****************************************')
    else:
        print('No se ha actualizado el estado. Verifique los datos ingresados')

def inmueble_presupuesto(lista):
    print('\n*****************************************')
    print('***** Inmuebles Segun su presupuesto *****')
    print('******************************************')
    presupuesto = float(input('Ingrese el presupuesto máximo: '))
    inmuebles_segun_presupuesto = []

    for inmueble in lista:
        precio = calcular_precio(inmueble)
        if precio <= presupuesto and inmueble['estado'] in ['Reservado', 'Disponible']:
            inmueble_precio = inmueble.copy()
            inmueble_precio['precio'] = precio
            inmuebles_segun_presupuesto.append(inmueble_precio)
    mostrar_inmuebles(inmuebles_segun_presupuesto, True)
    return inmuebles_segun_presupuesto

def calcular_precio(inmueble):
    zona = inmueble['zona']
    metros = inmueble['metros']
    habitaciones = inmueble['habitaciones']
    garaje = inmueble['garaje']
    antiguedad = 2023 - inmueble['año']
    if zona == 'A':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100)
    elif zona == 'B':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 1.5
    elif zona == 'C':
        precio = (metros * 100 + habitaciones * 500 +
                  garaje * 1500) * (1 - antiguedad / 100) * 2
    return precio
