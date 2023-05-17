from function import mostrar_menu, mostrar_inmuebles, agregar_inmuebles, editar_inmuebles, eliminar_inmueble, cambiar_estado, inmueble_presupuesto
from inmuebles import inmuebles


while True:
    mostrar_menu()
    opcion = input('Ingrese una opcion: ')

    if not opcion:
        print('Ingrese una opción numerica válida')

    if opcion == '1':
        print('***** lista de Inmuebles *****')
        mostrar_inmuebles(inmuebles)
    elif opcion == '2':
        agregar_inmuebles(inmuebles)
    elif opcion == '3':
        print('***** Editar Inmuebles *****')
        editar_inmuebles(inmuebles)
    elif opcion == '4':
        print('***** Eliminar Inmuebles *****')
        eliminar_inmueble(inmuebles)
    elif opcion == '5':
        print('***** Cambiar estado del inmueble *****')
        cambiar_estado(inmuebles)
    elif opcion == '6':
        print('***** Cambiar estado del inmueble *****')
        inmueble_presupuesto(inmuebles)
    elif opcion == '7':
        break
