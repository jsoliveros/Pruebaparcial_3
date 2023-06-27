
Pelicula_cine={'Nombre Pelicula':['SPIDER'],'Sala':['SALA 1'],'Categoria':['ACCION']}

compradores={'Nombre':['JORGE','NICOLAS'],'Pelicula':['SPIDER','SPIDER'],'Entradas':['1','1'],'Fila':['A','A'],'Columna':['1','2'],'Alumno':['SI','NO']}

fila_permitida=['A','B','C','D','E','F','G','H','I','J','K','L','N','M','O']
columna_permitida=['1','2','3','4','5','6','7','8','9','10']
entrada = 2500

sala1=[['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10'],
       ['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10'],
       ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10'],
       ['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10'],
       ['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10'],
       ['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10'],
       ['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10'],
       ['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10'],
       ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10'],
       ['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10'],
       ['K1','K2','K3','K4','K5','K6','K7','K8','K9','K10'],
       ['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10'],
       ['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10'],
       ['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10'],
       ['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10']]
       

for i in range(100):
    print('Menu')
    print('[1] Peliculas disponibles')
    print('[2] Mostrar Sala')
    print('[3] Comprar entradas')
    print('[4] Todos los usuarios que compraron su entrada asiento / pelicula')
    print('[5] Listado completo de las boletas')

    while True:
        try:
            opc=int(input('Ingrese opcion deseada: '))
            if opc >= 1 and opc <=5:
                break
            else: print('Ingrese un numero existente')
        except ValueError:
            print('Ingrese el dato solicitado')
        
    if opc == 1:
        print(f'Esta/s son las peliculas disponibles: {Pelicula_cine["Nombre Pelicula"]}')
    elif opc == 2:
        for fila in sala1:
            for asiento in fila:
                print(asiento, end= ' ')
            print() 
    elif opc == 3:
        while True:
            print('Has ingresado para comprar su entrada')
            nombre=str(input('Ingrese su nombre: ')).upper()
            if nombre:
                compradores['Nombre'].append(nombre)
                break
            else: print('El Nombre no puede estar vacio')
        alumno_si_no=['SI','NO']
        while True:
            alumno=str(input('Usted es alumno de DUOC [SI - NO] (Si lo eres tienes un descuento del 10%): ')).upper()
            if alumno in alumno_si_no:
                compradores['Alumno'].append(alumno)
                descuento = entrada - 250
                break
            else: print('El dato no puede estar vacio')

        while True:
            print(Pelicula_cine['Nombre Pelicula'])
            pelicula=str(input('Que pelicula desea ver: ')).upper()
            if pelicula in Pelicula_cine['Nombre Pelicula']:
                compradores['Pelicula'].append(pelicula)
                break
            else: print('El dato no puede estar vacio')

        while True:
            try:
                entradas=int(input('Ingrese la cantidad de entradas que desea [1 - 150]: '))
                if entradas >= 1 and entradas <= 150:
                    compradores['Entradas'].append(entradas)
                    for fila in sala1:
                        print(fila)
                        while True:
                            print('Estas son las filas: ')
                            print(fila_permitida)
                            fila=str(input('Ingrese la fila que desea: ')).upper()
                            if fila in fila_permitida:
                                compradores['Fila'].append(fila)
                                break
                            else: print('El dato no puede estar vacio')
                        while True:
                            print('Estas son las columnas: ')
                            print(columna_permitida)
                            columna=str(input('Ingrese la columna deseada: '))
                            if columna in columna_permitida:
                                compradores['Columna'].append(columna)
                                break
                            else: print('El dato no puede estar vacio')
                        for ro in range(len(sala1)):
                            for cio in range(len(sala1[ro])):
                                if sala1[ro][cio] == fila + columna:
                                    sala1[ro][cio] = 'XX' 
                        for fila in sala1:
                            print(fila)
                            break
                else: print('El dato no puede estar vacio')
            except ValueError: print('Ingrese el dato solicitado')
        
            print('|*******************************|')
            print('|          BOLETA               |')
            print('|*******************************|')
            print(f' Nombre: {compradores["Nombre"]}  ')
            print(f' Pelicula: {compradores["Pelicula"]}')
            print(f' Cantidad de entradas: {compradores["Entradas"]}')
            print(f' Fila: {compradores["Fila"]}')
            print(f' Columna: {compradores["Columna"]}')
            print(f' Alumno DUOC: {compradores["Alumno"]}')
            print(f' Precio entrada: {entrada}')
            print(f' Precio Alumno DUOC: {descuento}')
    elif opc == 4:
        print(f'Los asistentes de la pelicula: {Pelicula_cine["Nombre Pelicula"]} fueron un total de: {compradores["Entradas"]} con los asientos: {compradores["Fila"],compradores["Columna"]}')
        
    elif opc == 5:
        print(f'El total de ventas del cine: {compradores}')
        with open ('boleta.txt','w') as guardar:
            guardar.write(str(compradores))

