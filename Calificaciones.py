estudiantes = { }                                #se crea eldiccionario vacìo 
wile_agregar_estudiante_menu = True                                  #se crea el while por si el usuario desea agregar estudiante desde el menù
nota = int                                                #se define la variable nota como un entero
lista_notas = []  
                                        #se crea la lista que almacena las notas 
while wile_agregar_estudiante_menu:         
    wile_seguir_agregando_estudiante = True                          #se crea el while para seguir agregando estudiantes apenas haya creado el anterior
    while wile_seguir_agregando_estudiante:
        estudiante_repetido = True
        while estudiante_repetido:
            estudiante = input("ingrese el nombre completo del estudiante: \n")   
                                                                
            if estudiante in estudiantes:
                print("Este estudiante ya se encuentra en la lista, si hay dos estudiantes con el mismo nombre, \ningresale a uno algo que lo distinga")       
            else: 
                estudiantes[estudiante] =  [] 
                estudiante_repetido = False
        for nombre, lista_notas in estudiantes.items():                                   
            print(f"{nombre}: {[]}")                                                          
        wile_respuesta_no_valida_seguir_agregando_estudiantes = True                           
        while wile_respuesta_no_valida_seguir_agregando_estudiantes:
        
            agregar_estudiante = input("desea seguir agregando estudiantes? (si/no)\n")
            
            if agregar_estudiante == "si":
                print("")
                wile_respuesta_no_valida_seguir_agregando_estudiantes = False
            elif agregar_estudiante == "no":
                print("Estudiante/s agregado/s con exito ")
                wile_respuesta_no_valida_seguir_agregando_estudiantes = False
                wile_agregar_estudiante_menu = False
                wile_seguir_agregando_estudiante = False
            else: 
                print("respuesta no valida, intentelo de nuevo ")
    
    wile_volver_menu = True                                     #se crea el while por si el usuario desea volver al menu
    while wile_volver_menu:
        print("---"*30)
        menu = int(input("--Que desea hacer-- \n(1) Ingresar otro estudiante \n(2) Asignar notas a estudiante \n"
        "(3) Buscar esudiante \n(4) Listar estudiantes y mostrar notas\n(5) Sacar promedio de estudiante/s\n(6) Eliminar estudiante o nota de estudiante\n "))
        print ("---"*30)
        wile_agregar_estudiante_menu = True                
        if menu == 1:                                       
            print("")
            wile_volver_menu = False                       
        elif menu == 2:                                     
            notas_otro_estudiante = True                  
            while notas_otro_estudiante:  
                nombre_no_encontrado = True   
                while nombre_no_encontrado:               
                    nombre_buscar = input("Ingrese el nombre del estudiante para asignarle notas: \n")
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
                        try:
                            nota = int(input("Ingrese la nota del estudiante \n"))
                        except ValueError:
                            print("No se permite ingresar letras")  
                        if nota<0 or nota>100:
                            print("esa nota no es valida, intentelo de nuevo")
                        else: 
                            nota_no_valida = False
                    estudiantes[nombre_buscar].append(nota)             #esto guarda la nota que ingresò en el estudiante en especìfico en su propia lista de notas
                    valores_nombre = estudiantes.get(nombre_buscar)     #nuevamente trae a la variable valores nombre la lista de notas de el estudiante para poder imprimirlas
                    print(nombre_buscar,valores_nombre)
                    ingresar_mas_notas_no_valida = True
                    while ingresar_mas_notas_no_valida:
                        ingresar_mas_notas = input("Desea ingresar mas notas? (si/no)\n")         
                        if ingresar_mas_notas == "si":
                            print("")
                            ingresar_mas_notas_no_valida = False
                        
                        elif ingresar_mas_notas == "no":
                            ingresar_mas_notas_while = False
                            ingresar_mas_notas_no_valida = False
                        else:
                            print("Respuesta no valida, intentalo de nuevo")

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
            estudiante_no_encontrado_pal_promedio = True
            while estudiante_no_encontrado_pal_promedio:
                promedio_estudiante = input("ingrese de que estudiante desea sacar el promedio: \n")
                if not promedio_estudiante in estudiantes:
                    print("no se ha encontrado ese estudiante, intentelo de nuevo")
                    print("--"*15)
                else: 
                    estudiante_no_encontrado_pal_promedio = False

            lista_pa_promedio = estudiantes.get(promedio_estudiante)
            cantidad_notas = len(lista_pa_promedio)
            notas_sumadas = 0
            for conta in lista_pa_promedio:
                notas_sumadas = notas_sumadas + conta
            promedio_total_estudiante = notas_sumadas / cantidad_notas
            print("--"*15)
            print (f"ESTUDIANTE:  {promedio_estudiante} ")
            print("--"*15)
            print(f"NOTAS:  {lista_pa_promedio}")
            print("--"*15)
            print(f"PROMEDIO:  {promedio_total_estudiante}")
            print("--"*15)
            if promedio_total_estudiante < 60: 
                print(f"ESTADO DEL ESTUDIANTE EN LA MATERIA: REPROBADO")
            else:
                print(f"ESTADO DEL ESTUDIANTE EN LA MATERIA: APROBADO")


        elif menu == 6:
            valor_o_caracter_no_valido = True
            while valor_o_caracter_no_valido:
                try:
                    menu_opcion_6 = int(input("--Que desea hacer?-- \n(1)  Eliminar una nota especifica de un estudiante \n(2) Eliminar estudiante por completo \n(3) volver al menù \n"))
                    if menu_opcion_6 == 1:
                        volver_eliminar_nota = True
                        el_estudiante = input("Ingrese el nombre del estudiante al que lequiere eliminar nota: \n")
                        el_lista_estu = estudiantes.get(el_estudiante)
                        while volver_eliminar_nota:
                            print(el_lista_estu) 
                            cant_notas = len(el_lista_estu)
                            indice = list(range(1,cant_notas+1))
                            for n in indice:
                                print(f" {n}  ", end='')
                            indice_elim = int(input("\nIndique la nota que desea eliminar segun el indice que aparece abajo de esta"))
                            not_eliminada = el_lista_estu.pop(indice_elim - 1)
                            print(f"{not_eliminada} se borrò de la lista de notas, La lista de {el_estudiante} quedò: ")
                            print( el_lista_estu)
                            respuesta_no_valida2 = True
                            while respuesta_no_valida2:
                                pregunt_volver_eliminar_nota = input(f"Desea eliminar otra nota de {el_estudiante}? ")
                                if pregunt_volver_eliminar_nota == "si":
                                    print("")
                                    respuesta_no_valida2 = False
                                elif pregunt_volver_eliminar_nota == "no": 
                                    volver_eliminar_nota = False
                                    respuesta_no_valida2 = False
                                    valor_o_caracter_no_valido = False

                                else: 
                                    print("Respuesta no valida, intentelo de nuevo ")
                    

                    elif menu_opcion_6 == 2:
                        eliminar_mas = True
                        while eliminar_mas:
                            elim_estudiante = input("Digite el nombre del estudiante al cual desea eliminar por completo \n")
                            segur_elim =True
                            while segur_elim:
                                seguro_elim = input (f"Esta seguro que quiere eliminar a: {elim_estudiante}? (si/no) \n")
                                if seguro_elim == "si":
                                    del estudiantes[elim_estudiante]
                                    print("asì quedò la lista de estudiantes: ")
                                    print("---"*30)
                                    for nombre, lista_notas in estudiantes.items(): 
                                        mostrar = estudiantes.get(nombre)
                                        print(nombre , mostrar)
                                    print("---"*30)
                                    segur_elim = False
                                    eliminar_mas = False
                                    valor_o_caracter_no_valido = False

                                elif seguro_elim == "no":
                                    eliminar_mas = False
                                    segur_elim = False
                                    valor_o_caracter_no_valido = False
                                else:
                                    print("Respuesta no valida, intentelo de nuevo ")
                    elif menu_opcion_6 == 3:
                        print("")
                        valor_o_caracter_no_valido = False

                    else:
                        print("Valor o caracter no valido")
                        valor_o_caracter_no_valido = False
                except ValueError:
                    print("No se pueden ingresar letras")

    