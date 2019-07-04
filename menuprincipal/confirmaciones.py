def confirmaciones():
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
    #------------------------------------------------------------------------------------------------------------------------    
    # CONTADOR NUMERO ROMANO-------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------------
    romano=['I)','II)','III)','IV)','V)','VI)','VII)','VIII)','IX)','X)','XI)','XII)','XIII)','XIV)','XV)','XVI)','XVII)','XVIII)',
    'XIX)','XX)','XXI)','XXII)','XXIII)','XXIV)','XXV)','XXVI)','XXVII)','XXVIII)','XXIX)','XXX)']
    contadorromano=2
    NdeExpediente=input("Ingrese el Numero de EXPEDIENTE(sin el año): ")
    AnioExpediente=input("Ingrese el Año del expediente: ")
    nuevoexp=NdeExpediente+"/"+AnioExpediente
    NombreDenunciante=input("Ingrese el Nombre completo de el/la denunciante: ")
    NombreDenunciante=NombreDenunciante.upper()
    cerrarWhile=0
    while cerrarWhile==0:
            print ("*****************************RESOLUCION DE JUZGADO DE VIOLENCIA FAMILIAR******************************")
            print ("*****************************************CONFIRMACIONES**************************************")
            print ("****************************************************************************************************")
            
            NdeExpediente=input("Ingrese el Numero de expediente (sin el año): ")
            AnioExpediente=input("Ingrese el Año del expediente: ")
            nuevoexp=NdeExpediente+"/"+AnioExpediente
            Comisariadeladenuncia=("Ingrese la comisaria: ")
            Comisariadeladenuncia=Comisariadeladenuncia.upper()
            Fojares=("Ingrese la Foja de la Resolucion del juzgado de Paz (ej:6/8)")
            NombreDenunciante=input("Ingrese Nombre completo del denunciante: ")
            NombreDenunciante=NombreDenunciante
            




Variablefinal=("Y CONSIDERANDO: Ante la "+Comisariadeladenuncia+","+sexo+" "+NombreDenunciante+". "+Dnidenunciante+",con domicilio en "+DomicilioDenunciante+",ha realizado denuncia por Violencia Familiar en contra de quien fuera su "+VinculoConElDenunciado+" "+sexo1+" "+NombreDenunciado+", domiciliado en "+DomicilioDenunciado+"+\n" + "Analizadas las constancias de la causa, se advierte que a Fs."+Fojares+" obra resolución del Juez de Paz de la localidad de "+Localidadremitente+", conforme lo establece el art.657 del CPCC. y F., el mismo ha dispuesto medidas de "+medidadeljuezdepaz+" y siendo que el Juez de Paz actuante, ha resuelto las medidas pertinentes teniendo en consideración la extrema urgencia que amerita la situación conforme la Ley de Violencia Familiar y en el marco del art. 657 del CPCC y F. y habiéndose remitido a este Juzgado corresponde ratificar la misma en virtud a las facultades atribuidas al suscripto por el art. 36 del CPCC y VF."+"\n")