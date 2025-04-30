estudiantes = { }
wile1 = True
nota = int
lista_notas = []
while wile1:
    wile4 = True
    while wile4:
        estudiante = input("ingrese el nombre completo del estudiante: ")
        estudiantes[estudiante] =  []
        
        
        for nombre, lista_notas in estudiantes.items():
            print(f"{nombre}: {[]}")
        wile2 = True
        while wile2:
        
            agregar_estudiante = input("desea seguir agregando estudiantes? (si/no)")
            
            if agregar_estudiante == "si":
                print("")
                wile2 = False
            elif agregar_estudiante == "no":
                wile2 = False
                wile1 = False
                wile4 = False
            else: 
                print("respuesta no valida")
    
    wile3 = True
    while wile3:
        print("Estudiante agregado con exito ")
        print("---"*30)
        menu = int(input("--Que desea hacer-- \n(1) Ingresar otro estudiante \n(2) Asignar notas a estudiante \n"
        "(3) Buscar esudiante \n(4) Listar estudiantes y mostrar notas"))
        if menu == 1:
            print("")
            wile3 = False
        elif menu == 2:
            notas_otro_estudiante = True
            while notas_otro_estudiante:
                nombre_buscar = input("Ingrese el nombre del estudiante para asignarle notas: ")
                
                valores_nombre = estudiantes.get(nombre_buscar)
                print(valores_nombre)
                print(nombre_buscar,valores_nombre)
                print(estudiantes)
                ingresar_mas_notas_while = True
                while ingresar_mas_notas_while:
                    nota = int(input("Ingrese la nota del estudiante"))

                    estudiantes[nombre_buscar].append(nota)
                    valores_nombre = estudiantes.get(nombre_buscar)
                    print(nombre_buscar,valores_nombre)

                    ingresar_mas_notas = input("Desea ingresar mas notas? (si/no)")
                    if ingresar_mas_notas == "si":
                        print("")
                       
                    elif ingresar_mas_notas == "no":
                        ingresar_mas_notas_while = False
                        
                    
                ingresar_notas_otro_estudiante = input("Desea ingresar notas de otro estudiante? (si/no)")
                if ingresar_notas_otro_estudiante== "si":
                    print("")
                elif ingresar_notas_otro_estudiante == "no":
                    notas_otro_estudiante = False
                    
        elif menu == 4:
                print(estudiantes)

            

        


            # if nombre_buscar in estudiantes:
            #     print(estudiantes[nombre_buscar])
            #     nota = int(input("ingrese la nota del estudiante"))
            #     estudiante[lista_notas.append(nota)]
            #     print(estudiantes[estudiante])
                

        








        
