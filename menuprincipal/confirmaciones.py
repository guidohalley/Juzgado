#import creadordecarpetas
import time
import os
def medconexidad():
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
def medbotonpanico():
        while True:
            BotonDepanico = input("¿Solicita boton de panico? (1=SI, 0=NO): ")
            if BotonDepanico=="1":
                if SexoDenunciante=="1":
                    botonpanico=("En virtud a la naturaleza  de la presente causa y el riesgo  a la que podría estar sujeta la denunciante y su familia conforme surge de los elementos aportados, corresponde proveer a "+sexo+" "+NombreDenunciante+" con D.N.I N° "+Dnidenunciante + ", con domicilio en "+DomicilioDenunciante+", de un Botón de Pánico."+"\n")
                    Variablefinal=Variablefinal+BotonDepanico
                break
            if SexoDenunciante=="0":
                botonpanico=("En virtud a la naturaleza  de la presente causa y el riesgo  a la que podría estar sujeta la denunciante y su familia conforme surge de los elementos aportados, corresponde proveer a "+sexo+" "+NombreDenunciante+" con D.N.I N° "+Dnidenunciante + ", con domicilio en "+DomicilioDenunciante+", de un Botón de Pánico."+"\n")
                Variablefinal=Variablefinal+BotonDepanico
                break
            if BotonDepanico!="1" and BotonDepanico!="0":
                print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
            if BotonDepanico=="0":
                break


def fechasdiashoras():
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
        #******************# #******************#     #******************#  #******************#
def preguntasinciales():
                NdeExpediente=input("Ingrese el Numero de expediente (sin el año): ")
                AnioExpediente=input("Ingrese el Año del expediente: ")
                nuevoexp=NdeExpediente+"/"+AnioExpediente
                Comisariadeladenuncia=input("Ingrese la comisaria: ")
                Comisariadeladenuncia=Comisariadeladenuncia.upper()
                Localidadremitente=input("Ingrese la Localidad Remitente")
                Localidadremitente=Localidadremitente.upper()
                Fojares=input("Ingrese la Foja de la Resolucion del juzgado de Paz (ej:6/8)")
                confirmacionplazo=input("Confirmar o No confirmar el plazo de la foja anterior? 1=SI 0=NO")
                cantidaddemeses=input("ingrese la opcion para CONFIRMAR 1= 3 meses 2= 6 meses")
        #******************# #******************#     #******************#  #******************#
def datosdenunciante():
    print ("*****************************************DATOS DEL DENUNCIANTE**************************************")
    print ("****************************************************************************************************")
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
        print ("************************* ")
        print ("LOS DATOS INGRESADOS SON: ")
        print ("************************* ")
        print (" ")
        print ("Numero de expediente : "+NdeExpediente+"/"+AnioExpediente)
        print ("Nombre completo del denunciante: "+NombreDenunciante)
        if SexoDenunciante == "1":
            print ("Sexo del/la denunciante: Femenino")
        if SexoDenunciante == "0":
            print ("Sexo del/la denunciante: Masculino")
        print ("D.N.I del denunciante: "+ Dnidenunciante)
        print ("Domicio del denunciante: "+DomicilioDenunciante)
        print ("N° de telefono del denunciante: "+NumeroDeTelefonoDenunciante)
        print ("Vinculo con el denunciado: "+VinculoConElDenunciado)
        print (" ")
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
        #******************# #******************#     #******************#  #******************#
def datosdenunciado():
    os.system ("cls")
    cerrarWhile=0
    while cerrarWhile==0:
        print ("*****************************RESOLUCION DE PROHIBICION DE ACERCAMIENTO******************************")
        print ("****************************************DATOS DEL DENUNCIADO****************************************")
        print ("****************************************************************************************************")
        print ("\n")
        NombreDenunciado=input("Nombre completo del denunciado: ")
        NombreDenunciado=NombreDenunciado.upper()
        while True:
            SexoDenunciado = input("Sexo del/la denunciante (0=Masculino, 1=Femenino): ")
            if SexoDenunciado == "1":
                print ("Sexo del/la denunciado Seleccionado : Femenino")
            if SexoDenunciado == "0":
                print ("Sexo del/la denunciado Seleccionado: Masculino")
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
        os.system ("cls")
        print ("************************* ")
        print ("LOS DATOS INGRESADOS SON: ")
        print ("************************* ")
        print (" ")
        print ("Nombre completo del denunciado: "+NombreDenunciado)
        print ("D.N.I del denunciando: "+ Dnidenunciado)
        print ("Domicio del denunciado: "+ DomicilioDenunciado)

        print ("N° de telefono del denunciado: "+NumeroDeTelefonoDenunciado)
        print (" ")
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

def medidasatomar():
    DenunciaConcreta = input("Concretamente la denunciante  manifiesta que: ")


def confirmaciones():
    romano=['I)','II)','III)','IV)','V)','VI)','VII)','VIII)','IX)','X)','XI)','XII)','XIII)','XIV)','XV)','XVI)','XVII)','XVIII)',
    'XIX)','XX)','XXI)','XXII)','XXIII)','XXIV)','XXV)','XXVI)','XXVII)','XXVIII)','XXIX)','XXX)']
    contadorromano=2
    cerrarWhile=0
    preguntasinciales()
    print("PROCEDEMOS CON LOS DATOS A CARGAR DEL DENUNCIADO Y DENUNCIANTE")
    datosdenunciante()
    Variablefinal=("Y CONSIDERANDO: Ante la "+Comisariadeladenuncia+","+sexo+" "+NombreDenunciante+". "+Dnidenunciante+",con domicilio en "+DomicilioDenunciante+",ha realizado denuncia por Violencia Familiar en contra de quien fuera su "+VinculoConElDenunciado+" "+sexo1+" "+NombreDenunciado+", domiciliado en "+DomicilioDenunciado+"+\n" + "Analizadas las constancias de la causa, se advierte que a Fs."+Fojares+" obra resolución del Juez de Paz de la localidad de "+Localidadremitente+", conforme lo establece el art.657 del CPCC. y F., el mismo ha dispuesto medidas de "+medidadeljuezdepaz+" y siendo que el Juez de Paz actuante, ha resuelto las medidas pertinentes teniendo en consideración la extrema urgencia que amerita la situación conforme la Ley de Violencia Familiar y en el marco del art. 657 del CPCC y F. y habiéndose remitido a este Juzgado corresponde ratificar la misma en virtud a las facultades atribuidas al suscripto por el art. 36 del CPCC y VF."+"\n")



    #print (Variablefinal)
    #corroborar si los datos del denunciante funcionan
    #corroborar considerando y agregar resuelvo con las medidas.
datosdenunciado()

  


