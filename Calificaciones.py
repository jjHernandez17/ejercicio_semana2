estudiantes = { }           #se crea eldiccionario vacìo 
wile_agregar_estudiante_menu = True            #se crea el while por si el usuario desea agregar estudiante desde el menù
nota = int                              #se define la variable nota como un entero
lista_notas = []                        #se crea la lista que almacena las notas 
while wile_agregar_estudiante_menu:         
    wile_seguir_agregando_estudiante = True         #se crea el while para seguir agregando estudiantes apenas haya creado el anterior
    while wile_seguir_agregando_estudiante:
        estudiante = input("ingrese el nombre completo del estudiante: \n")   
        estudiantes[estudiante] =  []                               #se define en el diccionario estudiantes que estudiante es la key y los values es la lista de notas
        
        
        for nombre, lista_notas in estudiantes.items():             #se recorre el diccionario con sus keys y sus valores 
            print(f"{nombre}: {[]}")                                #se imprime la key y su lista
        wile_respuesta_no_valida_seguir_agregando_estudiantes = True            #se crea while por si la respuesta del usuario no es ni si/no
        while wile_respuesta_no_valida_seguir_agregando_estudiantes:
        
            agregar_estudiante = input("desea seguir agregando estudiantes? (si/no)\n")
            
            if agregar_estudiante == "si":
                print("")
                wile_respuesta_no_valida_seguir_agregando_estudiantes = False
            elif agregar_estudiante == "no":
                wile_respuesta_no_valida_seguir_agregando_estudiantes = False
                wile_agregar_estudiante_menu = False
                wile_seguir_agregando_estudiante = False
            else: 
                print("respuesta no valida")
    
    wile_volver_menu = True                                     #se crea el while por si el usuario desea volver al menu
    while wile_volver_menu:
        print("Estudiante agregado con exito ")
        print("---"*30)
        menu = int(input("--Que desea hacer-- \n(1) Ingresar otro estudiante \n(2) Asignar notas a estudiante \n"
        "(3) Buscar esudiante \n(4) Listar estudiantes y mostrar notas\n(5) Sacar promedio de estudiante/s\n"))
        print ("---"*30)
        wile_agregar_estudiante_menu = True                 #se define esta variable verdadera porque para salir del while anterior lo definimos como falsa
        if menu == 1:                                       #si el estudiante escoge la opcion (1) agregar mas estudiantes 
            print("")
            wile_volver_menu = False                        #se quiebra el while de volver al menu pa que se devuelva al de crear estudiante
        elif menu == 2:                                     #si el usuario elige la opcion (2)  asignar notas a cada estudiante  
            notas_otro_estudiante = True                    #Se crea el while por si quiere agregarle notas a otro estudiante diferente del anterior
            while notas_otro_estudiante:  
                nombre_no_encontrado = True   
                while nombre_no_encontrado:               
                    nombre_buscar = input("Ingrese el nombre del estudiante para asignarle notas: ")
                    if not nombre_buscar in estudiantes:
                        print("estudiante no encontrado o mal escrito, intentelo de nuevo")
                        print("---"*30)
                    elif nombre_buscar in estudiantes:
                        nombre_no_encontrado = False
                valores_nombre = estudiantes.get(nombre_buscar)         #en la variable valores nombre se guarda los valores que tiene cada estudiante en especifico(.get)      
                print(nombre_buscar,valores_nombre)                     #se imprime el estudiante que buscò y la lista de notas
                ingresar_mas_notas_while = True                         #se crea el while que permite y pregunta si desea ingresar mas notas para ese estudiante
                while ingresar_mas_notas_while:
                    nota_no_valida = True
                    while nota_no_valida:
                        nota = int(input("Ingrese la nota del estudiante"))  
                        if nota<0 or nota>100:
                            print("esa nota no es valida, intentelo de nuevo")
                        else: 
                            nota_no_valida = False
                    estudiantes[nombre_buscar].append(nota)             #esto guarda la nota que ingresò en el estudiante en especìfico en su propia lista de notas
                    valores_nombre = estudiantes.get(nombre_buscar)     #nuevamente trae a la variable valores nombre la lista de notas de el estudiante para poder imprimirlas
                    print(nombre_buscar,valores_nombre)

                    ingresar_mas_notas = input("Desea ingresar mas notas? (si/no)\n")         
                    if ingresar_mas_notas == "si":
                        print("")
                       
                    elif ingresar_mas_notas == "no":
                        ingresar_mas_notas_while = False

                ingresar_notas_otro_estudiante = input("Desea ingresar notas de otro estudiante? (si/no)\n")

                if ingresar_notas_otro_estudiante== "si":
                    print("")
                elif ingresar_notas_otro_estudiante == "no":
                    notas_otro_estudiante = False
        elif menu == 3: 
            buscar_mas_estudiantes = True
            while buscar_mas_estudiantes: 

                estudiante_no_encontrado = True
                while estudiante_no_encontrado:
                    menu_buscar_nombre = input("Ingrese el nombre del estudiante que desea buscar: \n")
                    if menu_buscar_nombre in estudiantes:
                        mostrar_lista = estudiantes.get(menu_buscar_nombre)
                        print(menu_buscar_nombre , mostrar_lista)
                        estudiante_no_encontrado = False

                    elif not menu_buscar_nombre in estudiantes:
                        print("estudiante no encontrado o mal escrito, intentelo de nuevo")
                        print("---"*30)

                respuesta_no_valida = True
                while respuesta_no_valida:
                    desea_buscar_mas = input("Desea buscar mas estudiantes? (si/no) \n")
                    
                    if desea_buscar_mas == "si":
                        print("")
                        respuesta_no_valida = False
                    elif desea_buscar_mas == "no":
                        respuesta_no_valida = False
                        buscar_mas_estudiantes = False
                    else:
                        print("Esa respuesta no es valida")
                        print("---"*30)
     
        elif menu == 4:
            for nombre, lista_notas in estudiantes.items(): 
                mostrar = estudiantes.get(nombre)
                print(nombre , mostrar)

        elif menu == 5:
            promedio_estudiante = input("ingrese de que estudiante desea sacar el promedio: ")
            lista_pa_promedio = estudiantes.get(promedio_estudiante)
            cantidad_notas = len(lista_pa_promedio)
            notas_sumadas = 0
            for conta in lista_pa_promedio:
                notas_sumadas = notas_sumadas + conta
            promedio_total_estudiante = notas_sumadas / cantidad_notas
            print (f"el promedio de todas las notas de {promedio_estudiante} es: {promedio_total_estudiante}")

                


            

        


        








        
