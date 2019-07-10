def confirmacion():
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
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
    print("|-----------------------------------INICIANDO PROGRAMA PARA CONFIRMACIONES----------------------------------------------|")
    print("|------------------------------------------by Halleyº-------------------------------------------------------------------|")
    time.sleep(2)
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system('cls')
    cerrarWhile=0
    while cerrarWhile==0:
        print ("**************************************RESOLUCION DE CONFIRMACIONES**********************************")
        print ("*****************************************DATOS DEL EXPEDIENTE***************************************")   
        NdeExpediente=input("Numero de expediente (sin el año): ")
        AnioExpediente=input("Año del expediente: ")
        Localidad=input("Ingrese el Nombre de la Localidad donde se Radicó la denuncia")
        Comisaria = input("Ingrese el Nombre de la Comisaria donde se Radicó la denuncia")
        fsresjp=input("Ingrese la Foja de la Resolucion del Juzgado de paz (Ejemplo > 2/3) ")
        nuevoexp=NdeExpediente+"/"+AnioExpediente
        fs=input("Ingrese la Foja de la denuncia (Ej> 2/3)")
        print ("**************************************RESOLUCION DE CONFIRMACIONES**********************************")
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
        os.system ("cls")
        print ("_________________________________________________________________")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|Numero de expediente : "+NdeExpediente+"/"+AnioExpediente+"////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|//////////////////   LOS DATOS INGRESADOS SON:   //////////////|")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|///////////////////////////////////////////////////////////////|")
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
        print ("****************************************RESOLUCION DE CONFIRMACIONES***************************************")
        print ("*********************************************DATOS DEL DENUNCIADO****************************************\n")
        NombreDenunciado=input("Nombre completo del denunciado: ")
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


     
    #//////////////////////////////PREGUNTAS PREVIAS AL RESUELVO/////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    cerrarwhile=0
    while cerrarwhile==0:
            conexidad = input("¿Hay conexidad?  (1=SI, 0=NO): ")
            if conexidad != "0" and conexidad != "1":
                    print ("OPCION INCORRECTA, VUELVA A INGRESAR LA OPCION.")
            if conexidad == "1":
                    numexpco=input("Numero de expediente de la conexidad (sin el año): ")
                    anioexpcon=input("Año del expediente: ")
                    numexptecon=numexpco+"/"+anioexpcon
                    caratulacon=input("COPIE la caratula de la conexidad: ")
                    cerrarwhile=cerrarwhile+1
            if conexidad == "0":
                    cerrarwhile=cerrarwhile+2


    #//////////////////////////////PREGUNTAS PREVIAS AL RESUELVO/////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system ("cls")
    while True:
        cantidaddemeses = input("exclusion 1 = 3 meses     2 = 6 meses ")
        if cantidaddemeses=="1":
            cm="3(trés)Meses"
            break
        if cantidaddemeses=="2":
            cm="6(seis)Meses"
            break
        if cantidaddemeses!="1" and cantidaddemeses!="2":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
   

    #//////////////////////////////PREGUNTAS PREVIAS AL RESUELVO/////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    plazojp
    os.system ("cls")
    while True:
        plazojp = input("PRESIONE 1 para confirmar el tiempo dispuesto por el juzgado de paz, de lo contrario PRESIONE 0")
        if plazojp=="1":
            cm=" "
            break
        if cantidaddemeses=="0":
            punto
            plazojp=("No confirmar el plazo de Fs. "+fsresjp+ ".Disponer que el plazo de la prohibición de acercamiento ordenada sera de"+cm+"."\n")"
            break
        if cantidaddemeses!="1" and cantidaddemeses!="O":


    Variablefinal=("Y CONSIDERANDO: Ante la Comisaria "+Comisaria+","+sexo+" "+NombreDenunciante+" D.N.I. Nº "+Dnidenunciante+", con domicilio en "+DomicilioDenunciante+",  ha realizado denuncia por Violencia Familiar en contra de quien fuera su "+VinculoConElDenunciado+", "+sexo1+""+NombreDenunciado+" D.N.I Nº "+Dnidenunciado+", con domicilio en "+DomicilioDenunciado+"."+"\n"
                   "Analizadas las constancias de la causa, se advierte que a fs. "+fsresjp+" obra resolución del Juez de Paz de la localidad de "+Localidad+", conforme lo establece el art.657 del CPCC. y F., el mismo ha dispuesto medidas de "+medidasjp+" y siendo que el Juez de Paz actuante, ha resuelto las medidas pertinentes teniendo en consideración la extrema urgencia que amerita la situación conforme la Ley de Violencia Familiar y en el marco del art. 657 del CPCC y F. y habiéndose remitido a este Juzgado corresponde ratificar la misma en virtud a las facultades atribuidas al suscripto por el art. 36 del CPCC y VF."

    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    resuelvo=("Por lo expuesto y normativa citada:"+"\n"+
              "RESUELVO: "+romano[0]+" TENER por recibida las presentes actuaciones remitidas por el Juez de Paz de "+Localidad+"  y  avócome al conocimiento de las misma."+"\n"
              +romano[1]+"CONFIRMAR las medidas adoptadas en las actuaciones, a fs."+fsresjp+". "+plazojp+"."+"\n"
              +romano[2]+"DISPONER que el grupo familiar de las partes, realicen terapia psicológica por medio de alguna institución pública o privado, por el lapso que dure la medida ordenada, debiéndose acreditar en la causa la misma cada tres meses, y acompañar un informe general y pormenorizado de las sesiones llevadas a cabo, con diez días de anticipación al vencimiento de la medida, bajo apercibimiento de ley." +"\n")    
    Variablefinal=Variablefinal+resuelvo 
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////


confirmacion()