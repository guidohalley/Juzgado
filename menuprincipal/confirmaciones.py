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
    contadorromano=3
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
        Localidad=input("Ingrese el Nombre de la Localidad y Provincia donde se Radicó la denuncia: ")
        Comisaria = input("Ingrese el Nombre de la COMISARIA donde se Radicó la denuncia: ")
        fsresjp=input("Ingrese la Foja de la Resolucion del Juzgado de paz (Ejemplo > 2/3): ")
        nuevoexp=NdeExpediente+"/"+AnioExpediente
        fs=input("Ingrese la Foja de la denuncia (Ej> 2/3): ")
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

    cerrarWhile=0
    while cerrarWhile==0:
        print ("****************************************RESOLUCION DE CONFIRMACIONES***************************************")
        print ("*********************************************DATOS DEL DENUNCIADO****************************************\n")
        NombreDenunciado=input("Nombre completo del denunciado: ")
        NombreDenunciado=NombreDenunciado.upper()
        while True:
            SexoDenunciado = input("Sexo del/la denunciado (0=Masculino, 1=Femenino): ")
            if SexoDenunciado != "1" and SexoDenunciado != "0":
                print ("Respuesta incorrecta, vuelva a ingresar...")
            break
        while True:
            Dnidenunciado = input("D.N.I del denunciado (Eje: xx.xxx.xxx ) Ingrese 0 para DESCONOCIDO: ")
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
        print ("___________________________________________________________________")
        print ("|//////////////////////////////////////////////////////////////////|")
        print ("|Numero de expediente : "+NdeExpediente+"/"+AnioExpediente+"///////|")
        print ("|//////////////////////////////////////////////////////////////////|")
        print ("|//////////////////////////////////////////////////////////////////|")
        print ("|//////////////////   LOS DATOS DEL DENUNCIANTE SON:   ////////////|")
        print ("|//////////////////////////////////////////////////////////////////|")
        print ("|//////////////////////////////////////////////////////////////////|")
        print ("|Nombre completo del denunciante:   "+NombreDenunciante+"//////////|")
        if SexoDenunciante == "1":
            print ("|Sexo del/la denunciante:       Femenino///////////////////////|")
        if SexoDenunciante == "0":
            print ("|Sexo del/la denunciante:       Masculino//////////////////////|")
        print ("|D.N.I del denunciante:            "+ Dnidenunciante+"/////////////|")
        print ("|Domicio del denunciante:          "+DomicilioDenunciante+"////////|")
        print ("|N° de telefono del denunciante:   "+NumeroDeTelefonoDenunciante+"/|")
        print ("|Vinculo con el denunciado:        "+VinculoConElDenunciado+"//////|")
        print ("___________________________________________________________________")
        
        
        
        print ("\n___________________________________________________________________")
        print ("|///////////////////////////////////////////////////////////////|")
        print ("|//////////////////   LOS DATOS DEL DENUNCIADO SON: ////////////|")
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
        while True:
            medijp=input("Que medidas Tomo el juez de Paz? 1 = PROHIBICION, 2 = EXCLUSION: ")
            if medijp == "1":
                medidasjpexpro = ("PROHIBICION DE ACERCAMIENTO")
                break
            if medijp == "2":
                medidasjpexpro = ("EXCLUSION DEL HOGAR  Y PROHIBICION DE ACAERCAMIENTO")
                break                                  
                            
        while True:
            medidasjpconf=input("Confirmar el plazo? ingrese 1 si desea confirmar el plazo ordenado, de lo contrario presione 0: ")
            
            if medidasjpconf == "1":                
                medidasjp = ("CONFIRMAR las medidas adoptadas en las actuaciones, tomadas en fs."+fsresjp+"."+"\n")
                break

            if medidasjpconf == "0":
                plzjp=input("escriba el plazo ordenado por el juzgado de paz (ej: 2(dos)años) : ")
        while True:
            cantidaddemeses = input("Ingrese el plazo a ordenar para confirmar, 1 = 3 meses | 2 = 6 meses: ")
            if cantidaddemeses=="1":
                cm="3(trés)Meses"
                break
            if cantidaddemeses=="2":
                cm="6(seis)Meses"
                break
            medidasjp = ("CONFIRMAR las medidas adoptadas en las actuaciones, tomadas en fs."+fsresjp+".No confirmar el plazo de"+plzjp+".Disponer que el plazo de la prohibición de acercamiento ordenada sea de "+cm+"."+"\n")



        Variablefinal=("Y CONSIDERANDO: Ante la Comisaria "+Comisaria+","+sexo+" "+NombreDenunciante+" D.N.I. Nº "+Dnidenunciante+", con domicilio en "+DomicilioDenunciante+",  ha realizado denuncia por Violencia Familiar en contra de quien fuera su "+VinculoConElDenunciado+", "+sexo1+""+NombreDenunciado+" D.N.I Nº "+Dnidenunciado+", con domicilio en "+DomicilioDenunciado+"."+"\n"
        "Analizadas las constancias de la causa, se advierte que a fs. "+fsresjp+" obra resolución del Juez de Paz de "+Localidad+", conforme lo establece el art.657 del CPCC. y F., el mismo ha dispuesto medidas de "+medidasjpexpro+" y siendo que el Juez de Paz actuante, ha resuelto las medidas pertinentes teniendo en consideración la extrema urgencia que amerita la situación conforme la Ley de Violencia Familiar y en el marco del art. 657 del CPCC y F. y habiéndose remitido a este Juzgado corresponde ratificar la misma en virtud a las facultades atribuidas al suscripto por el art. 36 del CPCC y VF.")
  
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
    while True: 
        reintegrodenunciante = input("¿Solicita la denunciante reintegro al hogar? (1=SI, 0=NO): ")
        if reintegrodenunciante == "1":
            contadorromano=contadorromano+1
            reintegrodenunciante=(", y CUMPLIMENTAR con el correspondiente REINTEGRO de "+sexo+""+NombreDenunciante+"a su domicilio")
            break
        if reintegrodenunciante == "0":
            break

         

    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    resuelvo=("Por lo expuesto y normativa citada:"+"\n"+"RESUELVO: "+romano[0]+" TENER por recibida las presentes actuaciones remitidas por el Juez de Paz de "+Localidad+"  y  avócome al conocimiento de las misma."+"\n"
                +romano[1]+medidasjp
                +romano[2]+"DISPONER que el grupo familiar de las partes, realicen terapia psicológica por medio de alguna institución pública o privado, por el lapso que dure la medida ordenada, debiéndose acreditar en la causa la misma cada tres meses, y acompañar un informe general y pormenorizado de las sesiones llevadas a cabo, con diez días de anticipación al vencimiento de la medida, bajo apercibimiento de ley." +"\n")
    Variablefinal=Variablefinal+resuelvo  
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    cerrarWhile=0
    contadorromano=contadorromano-1

    while cerrarWhile==0:
        pupilar = input("¿Hay menores de 18 años en la causa?  (1=SI, 0=NO): ")
        if pupilar=="0":
            break
        if pupilar != "1" and pupilar != "0":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if pupilar == "1":
            while cerrarWhile==0:
                GuardaProvisoriacons = input("¿Necesita Guardia Provisoria? (1=SI, 0=NO): ")
                if GuardaProvisoriacons == "0":
                    cerrarWhile=cerrarWhile+1
                    break
                if GuardaProvisoriacons == "1":
                    cantidadhijos = input("Cantidad de hijos: ")
                    nombrehijos=""
                    c=0
                    cantidadhijos=int(cantidadhijos)
                    while c<cantidadhijos:
                        c=c+1
                        print ("DEL MENOR AL MAYOR...")
                        c=str(c)
                        ca=input("Nombre del hijo/a " + c + " : ")
                        c=int(c)
                        nombrehijos=ca+", "+ nombrehijos
                    guardapro = ("En consecuencia, y atento a las manifestaciones de la denunciante y lo expuesto precedentemente, se puede colegir que sería conveniente otorgar el Cuidado Personal Provisorio de las jovenes de marras "+nombrehijos+" a "+sexo+" "+NombreDenunciante+" en beneficio de las jóvenes debiendo cumplir con los deberes inherentes respecto de los niños consagrados por la Convención de los Derechos del Niño y el Pacto de San José de Costa Rica. Por lo expuesto, las disposiciones del art. 234 del C. P. C. y C.; y Convención Internacional sobre los Derechos del Niño. "+"\n")
                    Variablefinal=Variablefinal+guardapro
                    cerrarWhile=cerrarWhile+1
                    break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
     
    while True:
        if pupilar=="1":
            alimentos=input("¿Solicita de alimentos?(1=SI, 0=NO): ")
            if alimentos=="0":
                break
            if alimentos!="0" and alimentos!="1":
                print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
            if alimentos=="1":
                alimentos1=("En Doctrina se ha sostenido '....la importancia de la fijación de una cuota de alimentos provisorios en el procedimiento de denuncia de violencia familiar significa el mantenimiento de otras medidas de protección y el aseguramiento del derecho alimentarios de los niños...El denunciado que priva de las necesidades básicas alimentarias a sus hijos está ejerciendo violencia económica hacia ellos, en convergencia con otros tipos de violencia, como la psicológica, al perturbar su pleno desarrollo personal...'(Autor: Ortiz, Diego O. - Fecha: 6-sep-2016, Cita: MJ-DOC-10037-AR | MJD10037).-"+"\n")
                Variablefinal=Variablefinal+alimentos1
                montonum=input("Escriba el monto de cuota alimentaria provisoria EN NUMEROS: ")
                montoletra=input("Escriba el monto de cuota alimentaria provisoria EN LERTA: ")
                montoletra=montoletra.upper()
                break
        else:
            alimentos="0"
            break

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
     
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
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////     

        if conexidad == "1":
            contadorromano=contadorromano+1
            resuconexidad=(romano[contadorromano]+"En virtud de lo expuesto ut-supra, y atendiendo a la existencia de igualdad de sujeto y objeto, considero pertinente disponer la acumulación de los autos Expte. Nro. " +numexptecon+" "+caratulacon+"."+"\n")
            Variablefinal=Variablefinal+resuconexidad
            break
    
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        fiscalresu = input("¿Solicita intervencion del fiscal de instruccion Penal ? (1=SI, 0=NO): ")
        if fiscalresu == "1":
            fiscalresu=(romano[contadorromano]+"Líbrese Oficio al Fiscal de Instrucción Penal en turno, a fin que se notifique de todo lo actuado en este fuero, adjuntando copia simple de la denuncia obrante a fs. 1/2 y determine si la conducta desplegada por "+sexo1+" "+NombreDenunciado+" D.N.I. Nº"+Dnidenunciado+" "+DomicilioDenunciado+", Con Telefono Nº "+NumeroDeTelefonoDenunciado+", constituye delito de lesiones calificadas (conf. al Código Penal Argentino) y en su caso si corresponde instar la acción penal conforme a sus facultades y competencia."+"\n")
            Variablefinal=Variablefinal+fiscalresu
            break
        if fiscalresu!="0" and fiscalresu!="1":
            print (". . . OPCION INCORRECTA, VUELVA A INGRESAR . . .")
        if fiscalresu == "0":
            break

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True: 
        resudefensoria = input("¿Solicita intervencion de defensoria ? (1=SI, 0=NO): ")
        if resudefensoria == "1":
            contadorromano=contadorromano+1
            resudefensoria =(romano[contadorromano]+"Girar las presentes a la Defensoría Oficial de Violencia Familiar y/o que corresponda, a fin de que citen a la denunciante para  asumir el patrocinio letrado y/o manifieste si opta por patrocinio particular estando a su cargo la notificación a " + sexo +" "+ NombreDenunciante + " haciéndose saber que deberán diligenciarse en forma urgente las medidas judiciales ordenadas en las  causas de violencia familiar e informar al suscripto, el resultado de dichas diligencias, bajo la exclusiva responsabilidad de la Defensoría Oficial interviniente."+"\n")
            Variablefinal = Variablefinal+resudefensoria
            break
        if resudefensoria!="0" and resudefensoria!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if resudefensoria == "0":
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
     
    while True: 
        subscreresu = input("¿Solicita intervencion de Subscretearia de la mujer y familia ? (1=SI, 0=NO): ")
        if subscreresu == "1":
            contadorromano=contadorromano+1
            subscreresu=(romano[contadorromano]+"Dar intervención a la Subsecretaría de la mujer y la Familia, Dirección de Género, dependiente del Ministerio de Desarrollo Social de la Provincia, a fin de que tomen razón de la presente  ante  la medida y en el marco de su competencia coordinen los Servicios Públicos y privados para contener, evitar o en su caso superar las causas de maltrato, abusos y todo tipo de violencia dentro de la familia de la denunciante, debiendo comunicarse a este Juzgado las medidas y estrategias adoptadas en el término de veinte días de recepcionado el presente, a tal fin líbrese oficio pertinente, quedando a cargo del patrocinante, la confección y diligenciamiento de dicho oficio."+"\n")
            Variablefinal=Variablefinal+subscreresu
            break
        if subscreresu!="0" and subscreresu!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if subscreresu == "0":
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    if pupilar == "1":
        contadorromano=contadorromano+1
        pupilar=(romano[contadorromano]+"Dese intervención al representante del Ministerio Público Pupilar, a fin que la Defensoría Oficial que por turno corresponda, asuma la representación complementaria de los niños, niñas y adolescentes de autos, en resguardo de sus superiores intereses y dictamine respecto de las medidas adoptadas."+"\n")
        Variablefinal=Variablefinal+pupilar
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    if alimentos=="1":
        contadorromano=contadorromano+1
        alifinal=(romano[contadorromano]+ "ESTABLECER una cuota alimentaria a favor de  "+nombrehijos+" en la suma de pesos "+montoletra+" ($"+montonum+") que deberá abonar "+sexo1+" "+NombreDenunciado+" y depositar en la sección depósitos judiciales del Banco Macro del primero al diez de cada mes, por el término de "+cm+", bajo apercibimiento de ley. Haciendo saber a la denunciante que dado el carácter transitorio de las medidas adoptadas en esta causa, una vez vencido el plazo de vigencia de la cuota deberá acreditar el inicio de la causa de alimentos por ante el fuero pertinente, bajo apercibimiento de ley. "+"\n")
        Variablefinal=Variablefinal+alifinal
        contadorromano=contadorromano+1
        alifinal1=(romano[contadorromano]+"DISPONER que se libre oficio al Banco Macro a fin de que procedan a la apertura de una cuenta a la orden del Juzgado y como perteneciente al juicio de la carátula y abonen a "+sexo+" "+NombreDenunciante+" las sumas depositadas y/o a depositarse en  la misma por el plazo de "+cm+"."+"\n")
        Variablefinal=Variablefinal+alifinal1
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    if BotonDepanico == "1":
        contadorromano=contadorromano+1
        BotonDepanicoresu1=(romano[contadorromano]+"Atento a la gravedad de los hechos denunciados, corresponder proveer a "+sexo+" "+NombreDenunciante+ " D.N.I. Nº " +Dnidenunciante+ "realmente en "+DomicilioDenunciante+" de un Botón de Pánico, el cual tendrá una vigencia de "+cm+", será efectivizado en este Juzgado y comunicado a la Secretaria Técnica en Informática y de Superintendencia del S.T.J, una vez que la denunciante manifieste su número de celular, modelo del mismo y sistema operativo, debiendo presentarse ésta ante los estrados del presente Juzgado por ante el actuario, en el término de 48 hs. de notificada la presente, bajo apercibimiento de Ley, notifíquese personalmente o por cédula estando a cargo de la defensoría oficial patrocinante la confección de la correspondiente cédula y su diligenciamiento. Cumplido, líbrese el correspondiente Oficio a la Secretaria Técnica en Informática y de Superintendencia del S.T.J a los fines dispuestos ut-supra."+"\n")
        contadorromano=contadorromano+1
        BotonDepanicoresu2=(romano[contadorromano]+"Efectuada la instalación del botón de pánico a la denunciante, líbrese oficios por medio del SIGED a la Dirección de Violencia y Género de la Policía de Misiones, en coordinación con el Centro Integral de Operaciones (911); a la Subsecretaria de Relaciones con la comunidad -Ministerio de Gobierno- Línea 137 Programa las Víctimas contra las Violencias y Subsecretaria de Seguridad y Justicia -Ministerio de Gobierno- a fin de que reporten a sus respectivas jurisdicciones."+"\n")
        Variablefinal=Variablefinal+BotonDepanicoresu1+BotonDepanicoresu2
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////      
     
    while True: 
        informedeinteraccionfamiliar = input("¿Solicita interaccion familiar (Tevez) ? (1=SI, 0=NO): ")
        if informedeinteraccionfamiliar == "1":
            contadorromano=contadorromano+1
            informedeinteraccionfamiliar=(romano[contadorromano]+"Procedase a la realización de un informe de interacción familiar en el domicilio "+DomicilioDenunciante+" el que será llevado a cabo y elevado a esta Judicatura por el equipo interdisciplinario de este Juzgado de Violencia Familiar Nº 1 a cargo del Licenciado Alfredo Tevez"+"\n")
            Variablefinal=Variablefinal+informedeinteraccionfamiliar
            break
        if informedeinteraccionfamiliar!="0" and informedeinteraccionfamiliar!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if informedeinteraccionfamiliar == "0":
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True: 
        cuerpomedico = input("¿Solicita entrevista psicológica por el cuerpo medico forense ? (1=SI, 0=NO): ")
        if cuerpomedico == "1":
            contadorromano=contadorromano+1
            cuerpomedico=(romano[contadorromano]+"Señálese entrevista psicológica a "+sexo1+" "+NombreDenunciado+" y "+sexo+" "+NombreDenunciante+", a cargo del Gabinete Psicologico del Cuerpo Médico Forense del Poder Judicial, quienes deberán cumplir su cometido ante la presentación de las nombradas por ante dicho cuerpo, debiendo elevar el informe correspondiente en forma urgente"+"\n")
            Variablefinal=Variablefinal+cuerpomedico
            break
        if cuerpomedico!="0" and cuerpomedico!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if cuerpomedico == "0":
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True: 
        Primeraaudiencia = input("¿Solicita primera audiencia?  (1=SI, 0=NO): ")
        if Primeraaudiencia!="0" and Primeraaudiencia!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if Primeraaudiencia == "1":
            Cantidadaudiencia = input("Cantidad de personas que se toma audiencia: ")
            totalaudiencia=""
            c=0
            Cantidadaudiencia=int(Cantidadaudiencia)
            while c<Cantidadaudiencia:
                c=c+1
                ca=input("Nombre de la persona "+str(c)+"persona a tomar audiencia: ")
                totalaudiencia=ca+", "+ totalaudiencia
            contadorromano=contadorromano+1
            primeraudienci=(romano[contadorromano]+"Señalese primera audiencia en los términos del art. 5 de la Ley XIV Nº 6  a fin de que comparezca "+totalaudiencia+"a fin de que informe sobre su situacion actual Notifiquese personalmente o por cédula.-"+"\n")
            Variablefinal=Variablefinal+primeraudienci
            break
        if Primeraaudiencia == "0":
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        anmac = input ("¿Hay armas (anmac)?(1=SI, 0=NO): ")
        if anmac == "1":
            foja = input ("¿Que foja se denuncia?: ")
            contadorromano=contadorromano+1
            anmacresu=(romano[contadorromano]+"Atento a lo vertido a "+foja+", librese oficio al Delegado  del ANMAC en la ciudad de Posadas-Misiones, a los efectos de que tenga a bien remitir con carácter URGENTE informe respecto de "+sexo1+" "+NombreDenunciado+", DNI Nº "+Dnidenunciado+" con domicilio en "+DomicilioDenunciado+" y telefono "+NumeroDeTelefonoDenunciado+", se halla registrado ante esa Dirección como legitimo usuario de armas de fuego de uso civil y/o guerra, carácter y categoría condicional de la habilitación USO y/o PORTACIÓN. En caso positivo, informe respecto a los datos filiatorios completos, fecha de habilitación y expiración (Legajo, Lugar y Fecha).-"+"\n")
            Variablefinal=Variablefinal+anmacresu
            break
        if anmac == "0":
            break
        if anmac != "0" and anmac != "1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        drogadiccion = input ("¿Necesita de  intervención a la Subsecretaría de Prevención de Adicciones ?(1=SI, 0=NO): ")
        if drogadiccion == "1":
            drogadictoo=input("Cantidad de personas que necesitan intervención a la Subsecretaría de Prevención de Adicciones: ")
            c=0
            nombredroga=""
            drogadictoo=int(drogadictoo)
            while c<drogadictoo:
                c=c+1
                ca=input("Nombre de la persona " + str(c) + " : ")
                nombredroga=ca+", "+ nombredroga
            drogadiccionresu=(romano[contadorromano]+"Dese intervención a la Subsecretaría de Prevención de Adicciones y Control de Drogas (tel. 4447797) dependiente del Ministerio de Salud, a fin de que con carácter de valiosa colaboración, a efectos de que tomen intervención en autos respecto a la situación de "+nombredroga+" y en el ámbito de su competencia adopten las medidas que estimen corresponder a través de la  Dirección de Asistencia y Rehabilitación (Centro Manantial tel. 44456759) a cargo de la Dra. Mariela Garnier, brinden colaboración y asesoramiento al grupo familiar de la denunciante "+sexo+" "+NombreDenunciante+"estos fines líbrese el oficio pertinente con URGENTE Y PREFERENTE DESPACHO cuya confección y diligenciamiento estará a cargo de la Defensoría Oficial patrocinante."+"\n")
            contadorromano=contadorromano+1
            Variablefinal=Variablefinal+drogadiccionresu
            break
        if drogadiccion == "0":
            break
        if drogadiccion != "0" and drogadiccion != "1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        reingro=input("¿Hay restitucion de bienes?(1=SI, 0=NO): ")
        if reingro=="0":
            break
        if reingro!="0" and reingro!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if reingro=="1":
            reintegro=input("¿Quien denuncia los Bienes?(1=denunciante, 2=denunciado): ")
            if reintegro=="1":
                contadorromano=contadorromano+1
                reingrobienes=(romano[contadorromano]+" En cuanto a la restitución de bienes considero que en razón de lo ordenado en la presente y a los efectos de evitar que se produzcan nuevas situaciones de violencia, deberá " +sexo+" "+NombreDenunciante+" denunciar bienes y designar una persona, los datos de la misma (nombre y apellido, D.N.I, etc) autorizada por la misma a participar en el acto de retiro de bienes, la que quedará en calidad de depositario judicial de las pertenencias que en su caso se les restituirán debiendo acreditar la titularidad de los mismos."+"\n")
            if reintegro=="2":
                contadorromano=contadorromano+1
                reingrobienes=(romano[contadorromano]+" En cuanto a la restitución de bienes considero que en razón de lo ordenado en la presente y a los efectos de evitar que se produzcan nuevas situaciones de violencia, deberá " +sexo1+" "+NombreDenunciado+" denunciar bienes y designar una persona, los datos de la misma (nombre y apellido, D.N.I, etc) autorizada por la misma a participar en el acto de retiro de bienes, la que quedará en calidad de depositario judicial de las pertenencias que en su caso se les restituirán debiendo acreditar la titularidad de los mismos."+"\n")
            Variablefinal=Variablefinal+reingrobienes
            break

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        direcciondeinfacancia=input("¿Disponer de Dirección de Infancia del Ministerio de Desarrollo Social?(1=SI, 0=NO): ")
        if direcciondeinfacancia=="0":
            break
        if direcciondeinfacancia!= "0" and direcciondeinfacancia != "1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if direcciondeinfacancia=="1":
            contadorromano=contadorromano+1
            infacancia=(romano[contadorromano]+"Líbrese oficio a la Dirección de Infancia del Ministerio de Desarrollo Social a efectos que evalúe la situación de los menores y disponga o proponga en forma URGENTE las medidas de protección que considere necesarias, remitiendo el informe correspondiente al suscripto a la mayor brevedad y las medidas adoptadas, todo ello en los términos de la Ley II No 16 art. 36, 37, 38 y 41 tercer párrafo.Quedando a cargo su confección y diligenciamiento de la Defensoría Patrocinante."+"\n")
            Variablefinal=Variablefinal+infacancia
            break

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        busquedayparaderoresu=input("¿Necesita de busqueda y paradero?(1=SI, 0=NO): ")
        if busquedayparaderoresu=="0":
            break
        if busquedayparaderoresu!="0" and busquedayparaderoresu!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if busquedayparaderoresu=="1":
            contadorromano=contadorromano+1
            busqueda=(romano[contadorromano]+"Agréguese el informe que antecede y en atención a lo comunicado, como así también a los efectos de que se efectivice la notificación de la medida ordenada  en la causa, líbrese oficio al Departamento de Búsqueda de destino y paradero de la Policía de la Provincia de Misiones, a fin de dar con el paradero del "+sexo1+" "+NombreDenunciado+" D.N.I Nº "+Dnidenunciado+", y una vez habido, se proceda a informar al Defensor Oficial Nº1 de Violencia Familiar a cargo de la Dra. María Alejandra Ortega, a sus efectos."+"\n")
            Variablefinal=Variablefinal+busqueda
            break

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        ancianidad=input("¿Disponer del Departamento de Ancianidad? (1=SI, 0=NO): ")
        if ancianidad=="0":
            break
        if busquedayparaderoresu!="0" and busquedayparaderoresu!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if ancianidad=="1":
            nombreanciano=input("Nombre del anciano: ")
            contadorromano=contadorromano+1
            anciano=(romano[contadorromano]+"Dése intervención al Departamento de Ancianidad, dependiente del Ministerio de Desarrollo Social, a fin de que tomen conocimiento de la situación de "+nombreanciano+" y practiquen las medidas necesarias a fin de salvaguardar la integridad psicofísica de la misma e informe al suscripto las medidas adoptadas. Oficiese a sus efectos.-"+"\n")
            Variablefinal=Variablefinal+anciano
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        reguntacejume=input("¿Enviar a CE.JU.ME?(1=SI, 0=NO): " )
        if reguntacejume=="0":
            break
        if busquedayparaderoresu!="0" and busquedayparaderoresu!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if reguntacejume=="1":
            contadorromano=contadorromano+1
            pregceju=(romano[contadorromano]+"Hacer saber a "+sexo+" "+NombreDenunciante+" que para resolver las cuestiones de fondo, relativas a los ALIMENTOS, CUIDADO PERSONAL, Y RÉGIMEN DE COMUNICACIÓN Y CONTACTO de forma definitica, podrá recurrir al CEJUME a los fines de cumplimentar con la etapa de Advenimiento, conforme lo dispone el art. 653 del C.PCC y V.F., con patrocinio letrado de la Defensoria Oficial que por turno corresponda y/o abogado particular, a cuyo fin deberán concurrir por ante la DEUT, a fin de ser asesorado en su derecho o ser patrocinado en dicha materia."+"\n")
            Variablefinal=Variablefinal+pregceju
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True:
        serviciosocial=input("¿Solicita Servicio Social?(1=SI, 0=NO): ")
        if serviciosocial=="0":
            break
        if busquedayparaderoresu!="0" and busquedayparaderoresu!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if serviciosocial=="1":
            contadorromano=contadorromano+1
            serviso=(romano[contadorromano]+"Líbrese oficio a través del SIGED, a la Dirección de Asuntos de Familia y Género, de la Policía de la Provincia de Misiones, a fin de que el personal del Servicio Social de dicha institución, a modo de valiosa colaboración, se apersonen y realicen de manera URGENTE un amplio informe socio ambiental en el domicilio sito en"+DomicilioDenunciante+", respecto de: 1)- El estado de la vivienda, 2)- Personas que habitan en el domicilio, 3)- Relación de vecindad, 4)- Si las menores tiene seguimiento de salud (como ser vacunaciones, controles médicos, etc.), 5)- Personas que se encuentran en el hogar al momento de la entrevista y su relación con la familia, 6)- Si existe violencia psicofísica y todo otro dato de interés respecto de toda situación familiar actual."+"\n")
            Variablefinal=Variablefinal+serviso
            break

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

     
    while True: 
        oficioprovincial = input("¿Solicita Oficio al Registro Provincial de Actuaciones de Violencia? (1=SI, 0=NO): ")
        if oficioprovincial == "1":
            contadorromano=contadorromano+1
            oficioprovincial=(romano[contadorromano]+"Líbrese oficio al Registro Provincial de actuaciones de Violencia Familiar, en cumplimiento de lo dispuesto por el segundo párrafo del art. 7 de la Ley XIV No 6, a fin de que tome razón del inicio de la presente causa, debiendo comunicarse a este Juzgado si se ha efectivizado el registro en el término de veinte días de recepcionado el presente, quedando a cargo del patrocinante, la confección y diligenciamiento de dicho oficio."+"\n")
            Variablefinal=Variablefinal+oficioprovincial
            break
        if busquedayparaderoresu!="0" and busquedayparaderoresu!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if oficioprovincial == "0":
            break

    #///////////////////////////////////////////CREADOR DE ARCHIVOS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    contadorromano=contadorromano+1
    finalres=(romano[contadorromano]+"EXPEDIR copia certificada de la presente si fuere menester."+"\n")
    Variablefinal=Variablefinal+finalres
    contadorromano=contadorromano+1
    finalres=(romano[contadorromano]+"Regístrese, Cópiese, Notifíquese."+"\n"+"HGY")
    Variablefinal=Variablefinal+finalres
    os.system ("cls")
    time.sleep(2)
    archivo=open(os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia\\Confirmacion\\ResolucionFin"+" "+ NdeExpediente +".txt","a")
    archivo.write("Posadas, "+Dia+" de "+Mes+" del "+anio)
    archivo.write("\n")
    archivo.write("Y VISTOS: Estos autos caratulados: Expte Nº "+ NdeExpediente+"/"+AnioExpediente+ " " + "-" + " " + NombreDenunciante + " " + "C/" +" "+ NombreDenunciado + " " + "S/" + " " + "Violencia Familiar")
    archivo.write("\n")
    archivo.write(Variablefinal7318
    archivo.close()
    #///////////////////////////////////////////CREADOR DE ARCHIVOS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    print ("************************************************************************************************************************************")
    print ("********************************************RESOLUICION DE CONFIRMACION GENERADA EXITOSAMENTE*******************************************")
    print ("************************************************************************************************************************************")
    time.sleep(2)
    print ("BY GUIDO HALLEY JUZGADO DE VIOLENCIA FAMILIAR")
    time.sleep(2)
    import menuprincipal
    menuprincipal.menuprincipal()
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------



confirmacion()