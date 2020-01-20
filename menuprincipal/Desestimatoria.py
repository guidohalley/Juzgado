def desestimatoria():    
    # en este Programa no existen Medidas Especiales para tomar
    # en este Programa se deriva a Secretaria de Acceso a la Justicia
    import creadordecarpetas
    import time
    import os
    Dia = (time.strftime("%d"))
    Mes = (time.strftime("%B"))
    anio = (time.strftime("%Y"))
    if time.strftime("%B") == "May":
        Mes="Mayo"
    if time.strftime("%B") == "January":
        Mes="Enero"    
    if time.strftime("%B") == "February":
        Mes="Febrero"
    if time.strftime("%B") == "April" :
        Mes="Marzo"
    if time.strftime("%B") == "June" :
        Mes="Junio"
    if time.strftime("%B") == "July" :
        Mes="Julio"
    if time.strftime("%B") == "August" :
        Mes="Agosto"
    if time.strftime("%B") == "September" :
        Mes="Septiembre"
    if time.strftime("%B") == "October" :
        Mes="Octubre"
    if time.strftime("%B") == "November" :
        Mes="Noviembre"
    if time.strftime("%B") == "December" :
        Mes="Diciembre"
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    romano=['I)','II)','III)','IV)','V)','VI)','VII)','VIII)','IX)','X)','XI)','XII)','XIII)','XIV)','XV)','XVI)','XVII)','XVIII)',
    'XIX)','XX)','XXI)','XXII)','XXIII)','XXIV)','XXV)','XXVI)','XXVII)','XXVIII)','XXIX)','XXX)']
    contadorromano=5

    print("|-----------------------------------------------------------------------------------------------------------------------|")
    print("|-----------------------------------INICIANDO PROGRAMA PARA DESESTIMAR -------------------------------------------------|")
    print("|------------------------------------------by Halleyº-------------------------------------------------------------------|")
    time.sleep(2)
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system('cls')
    cerrarWhile=0
    while cerrarWhile==0:
        print ("**************************************RESOLUCION DESESTIMATORIA ***********************************")
        print ("*****************************************DATOS DEL EXPEDIENTE***************************************")   
        NdeExpediente=input("Numero de expediente (sin el año): ")
        AnioExpediente=input("Año del expediente: ")
        nuevoexp=NdeExpediente+"/"+AnioExpediente
        fs=input("Ingrese la Foja de la denuncia (Ej> 2/3)")
        print ("**************************************RESOLUCION DE EXCLUSION DE HOGAR******************************")
        print ("*****************************************DATOS DEL DENUNCIANTE**************************************")
        NombreDenunciante=input("Nombre completo del denunciante: ")
        NombreDenunciante=NombreDenunciante.upper()

        while True:
            SexoDenunciante = input("Sexo del/la denunciante (0=Masculino, 1=Femenino): ")
            if SexoDenunciante != "1" and SexoDenunciante != "0":
                print ("Respuesta incorrecta, vuelva a ingresar...")
            break
        while True:
            Dnidenunciante = input("D.N.I del denunciante (Eje: xx.xxx.xxx ) Ingrese 0 para DESCONOCIDO: ")
            if Dnidenunciante=="0":
                Dnidenunciante = "DESCONOCIDO"
                break
            else:
                if len(Dnidenunciante)<9 or len(Dnidenunciante)>10:
                    print ("Cantidad incorecta de caracteres: ")
                else: 
                    break

        DomicilioDenunciante = input("Domicilio del denunciante (Ingrese 0 para DESCONOCIDO): ")
        DomicilioDenunciante=DomicilioDenunciante.upper()
        NumeroDeTelefonoDenunciante = input("N° de telefono del denunciante (Ingrese 0 para DESCONOCIDO): ")
        VinculoConElDenunciado = input("Vinculo con el denunciado: ")
        VinculoConElDenunciado=VinculoConElDenunciado.upper()
        if DomicilioDenunciante=="0":
            DomicilioDenunciante= "DESCONOCIDO"
        if NumeroDeTelefonoDenunciante == "0" :
            NumeroDeTelefonoDenunciante = "DESCONOCIDO"
        if SexoDenunciante == "0" :
            sexo = "el Sr."
        if SexoDenunciante == "1" :
            sexo = "la Sra."
        print ("_________________________________________________________________")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|Numero de expediente : "+NdeExpediente+"/"+AnioExpediente+"////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|//////////////////   LOS DATOS INGRESADOS SON:   //////////////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|////////////////////////////////////////////////////////////////|")
        print ("|Nombre completo del denunciante:   "+NombreDenunciante+"//////////|")
        if SexoDenunciante == "1":
            print ("|Sexo del/la denunciante:       Femenino///////////////////////|")
        if SexoDenunciante == "0":
            print ("|Sexo del/la denunciante:       Masculino//////////////////////|")
        print ("|D.N.I del denunciante:            "+ Dnidenunciante+"/////////////|")
        print ("|Domicio del denunciante:          "+DomicilioDenunciante+"////////|")
        print ("|N° de telefono del denunciante:   "+NumeroDeTelefonoDenunciante+"/|")
        print ("|Vinculo con el denunciado:        "+VinculoConElDenunciado+"//////|")
        print ("_________________________________________________________________")
        while True:
            preg=input ("Si la informacion es correcta, Ingrese 1, para volver a ingresar presione 0: ")
            if preg == "1":
                cerrarWhile=cerrarWhile+1
                break
            if preg != "1" and preg != "0":
                print ("OPCION INCORRECTA, VUELVA A INGRESAR LA OPCION.")
            if preg == "0":
                break
#///////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system ("cls")
    cerrarWhile=0
    while cerrarWhile==0:
        print ("****************************************RESOLUCION DE EXCLUSION DE HOGAR******************************")
        print ("*********************************************DATOS DEL DENUNCIADO****************************************\n")   NombreDenunciado=input("Nombre completo del denunciado: ")
        NombreDenunciado=NombreDenunciado.upper()
        while True:
            SexoDenunciado = input("Sexo del/la denunciante (0=Masculino, 1=Femenino): ")
            if SexoDenunciado != "1" and SexoDenunciado != "0":
                print ("Respuesta incorrecta, vuelva a ingresar...")
            break
        while True:
            Dnidenunciado = input("D.N.I del denunciante (Eje: xx.xxx.xxx ) Ingrese 0 para DESCONOCIDO: ")
            if Dnidenunciado=="0":
                Dnidenunciado = "DESCONOCIDO"
                break
            else:
                if len(Dnidenunciado)<9 or len(Dnidenunciado)>10:
                    print ("Cantidad incrrecta de caracteres: ")
                else: 
                    break
        DomicilioDenunciado = input("Domicilio del denunciado (Ingrese 0 para DESCONOCIDO): ")
        DomicilioDenunciado=DomicilioDenunciado.upper()
        NumeroDeTelefonoDenunciado = input("N° de telefono del denunciado (Ingrese 0 para DESCONOCIDO): ")
        if DomicilioDenunciado == "0" :
            DomicilioDenunciado = "DESCONOCIDO"
        if NumeroDeTelefonoDenunciado == "0" :
            NumeroDeTelefonoDenunciado = "DESCONOCIDO"
        if SexoDenunciado == "0" :
            sexo1 = "el Sr."
        if SexoDenunciado == "1" :
            sexo1 = "la Sra."
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
        os.system ("cls")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|//////////////////   LOS DATOS INGRESADOS SON:   //////////////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|Nombre completo del denunciado: "+NombreDenunciado+"///////////|")
        if SexoDenunciado == "1":
            print ("|Sexo del/la denunciado:    Femenino////////////////////////|")
        if SexoDenunciado == "0":
            print ("|Sexo del/la denunciado:    Masculino""/////////////////////|")
        print ("|D.N.I del denunciando:         "+Dnidenunciado+"///////////////|")
        print ("|Domicio del denunciado:        "+ DomicilioDenunciado+"////////|")
        print ("|Vinculo con el denunciado:     "+VinculoConElDenunciado+"//////|")
        print ("|N° de telefono del denunciado: "+NumeroDeTelefonoDenunciado+"//|")
        print ("|///////////////////////////////////////////////////////////////|")
        while True:
            preg=input ("Si la informacion es correcta, Ingrese 1, para volver a ingresar presione 0: ")
            if preg == "1":
                cerrarWhile=cerrarWhile+1
                break
            if preg != "1" and preg != "0":
                print ("OPCION INCORRECTA, VUELVA A INGRESAR LA OPCION.")
            if preg == "0":
                break
        os.system ("cls")

    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|/// INGRESE DATOS CONCRETOS, EN LO POSIBLE EN 3ERA PERSONA ////|")
        print ("|///////////////////////////////////////////////////////////////|")


#modificar la parte de alimentos, y añadir una funcion donde si el denunciante es masculino sacar el parrafo que corresponda ("Violencia de Genero LINEA 193")
    DenunciaConcreta = input("Concretamente la denunciante  manifiesta que: ")



desestimatoria()