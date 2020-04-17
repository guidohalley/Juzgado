
def programod():
    
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
    print("|-----------------------------------INICIANDO PROGRAMA PARA EXCLUSION DEL HOGAR-----------------------------------------|")
    print("|------------------------------------------by Halleyº-------------------------------------------------------------------|")
    time.sleep(2)
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system('cls')
    cerrarWhile=0
    while cerrarWhile==0:
        print ("**************************************RESOLUCION DE EXCLUSION DE HOGAR******************************")
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
        os.system ("cls")
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
        print ("****************************************RESOLUCION DESESTIMATORIA******************************************")
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
    Variablefinal=("CONSIDERANDO: Que a fs. 2/3,obra denuncia de "+sexo+" "+NombreDenunciante  + " D.N.I" + " N°: "+Dnidenunciante+" con domicilio en " + DomicilioDenunciante + " con N° de Teléfono: "+ NumeroDeTelefonoDenunciante + " contra su " +VinculoConElDenunciado+" "+ sexo1 + " "+NombreDenunciado +
				   "domiciliado en " + DomicilioDenunciado+ ". Con Teléfono N°: " + NumeroDeTelefonoDenunciado+"."+"\n"+
                   "Concretamente denuncia que " +DenunciaConcreta+"\n"+
                   "Que la norma provincial citada entiende a la violencia familiar como '...toda acción, omisión, abuso o abandono que afecte la integridad física, psíquica, moral, sexual, patrimonial y la libertad de la misma (en referencia al/la denunciante) en el ámbito familiar, aunque no configure delito, sea ésta en forma permanente o temporaria...'"+"\n"
                   "Que, tal como se señaló en el III Congreso de Derecho de Familia (El Salvador, 1992) en las situaciones de violencia que se generan dentro de la familia se conculcan derechos fundamentales de las víctimas... 'El maltrato es cualquier acto u omisión que directa o indirecta mediante cualquiera de los miembros que conforman el grupo familiar, ya sea de una familia nuclear o extensa que constituye una clara violación de los derechos humanos'."+"\n"
                   "La mentada ley Provincial de Violencia Familiar XIV, N° 6, dispone en su art. 4º las medidas que el juez puede adoptar para preservar la integridad pisco-física de la víctima y de su grupo familiar, debiendo remediarse esta situación de inmediato en salvaguarda de la misma, tornándose impostergable adoptar medidas contra la violencia familiar manifestada."+"\n"
                   "Así pues, el marco legal de aplicación, persigue la protección del derecho personalísimo a conservar la integridad pisco-fisica que goza de protección de carácter constitucional tanto en el orden local, como en el orden internacional a través  de trascendentes instrumentos de Derechos Humanos, como son la Convención Americana Sobre Derechos Humanos (Art. 4.1, 5.1, 5.2, y concordantes), la Convención Sobre la Eliminación de todas las Formas de Discriminación contra la Mujer - CEDAW, aprobada por Naciones Unidas en el año 1979, ratificada por nuestro país el 17 de Julio de 1980 por Ley 23.179 del año 1985 con rango constitucional a partir de 1994 (conf. Art. 75 inc. 22 de la Constitución Nacional), la Convención Sobre los Derechos del Niño (con rango constitucional desde 1994, conf. Art. 75 inc. 22 de la Constitución Nacional), la Convención Interamericana Para Prevenir,  Sancionar y Erradicar La Violencia Contra La Mujer  'Convención de Belem Do Para', ratificada por nuestro país a través de la Ley 24.632 y con jerarquía constitucional desde el año 2011, la que en su Artículo 1º establece claramente lo que debe entenderse como violencia hacia la mujer, disponiendo que: Para los efectos de esta Convención debe entenderse por violencia contra la mujer cualquier acción o conducta, basada en su género, que cause muerte, daño o sufrimiento físico, sexual o psicológico a la mujer, tanto en el ámbito público como en el privado; aclarando en su Art. 7.e como obligación de los Estados parte: Adoptar medidas jurídicas para conminar al agresor a abstenerse de hostigar, intimidar, amenazar, dañar o poner en peligro la vida de la mujer de cualquier forma que atente contra su integridad o perjudique su propiedad...”."+"\n"
                   "También debe considerarse que el presente decisorio responde al deber del Estado de proteger a la familia (conf.a los Art. 14bis, 16, 19, 28, 75 inc. 22 e inc. 23, sgtes y concordantes de la Constitución Nacional)."+"\n"
                   "En tanto que en el ámbito interno, cobra relevancia, la ley Nº 26.485 “Ley de Protección Integral para Prevenir, Sancionar y Erradicar la Violencia contra las Mujeres en los ámbitos en que desarrollen sus Relaciones Interpersonales”, en lo que constituyó un refuerzo adicional a las disposiciones de las convenciones internacionales citadas."+"\n"
                   "Que en autos se evidencia una clara posición de vulnerabilidad en la persona de la denunciante y debe tenerse presente lo sostenido por la Comisión Interamericana de Derecho Humanos en el Informe Nº 54/01 caso 12.051: Maria Da Penha Maia Fernandes vs. Brasil (Abril de 2001) en el sentido de que es una obligación de los Estados el de actuar con la debida diligencia, y que ello va mas allá de procesar y/o condenar, sino que incluye la obligación de 'prevenir estas prácticas degradantes', y considerando que la omisión del Estado de actuar implica en la práctica una 'tolerancia de todo el sistema, que no hace sino perpetuar las raíces y factores psicológicos, sociales e históricos que mantienen y alimentan la violencia contra la mujer', lo que implica que si el Poder Judicial, como uno de los poderes del Estado, debe adoptar todas las medidas que estime necesarias a fin de prevenir o evitar la materialización de un daño o riesgo, o hacer cesar los efectos perjudiciales de una conducta; en este sentido se vienen pronunciado los tribunales de nuestro país. (Excma. Cám. de Familia de 2º Nom. In re 'C., A. - DENUNCIA POR VIOLENCIA DE GENERO - RECURSO DE APELACIÓN' - Expte. Nº 6465967 - A.I Nº 109 - 22/09/2017."+"\n"
                   "Por la índole y naturaleza del fenómeno de violencia familiar y ante la necesidad de que la víctima de la violencia pueda requerir y obtener auxilio para que cese el hecho dañoso, dada la celeridad y sumariedad exigida por el trámite establecido en la ley, no se requiere que el Juez haga un contradictorio con la denuncia efectuada y luego de todo un proceso judicial, tenga la absoluta convicción para tener por ciertos los hechos denunciados, a fin de disponer una medida provisional."+"\n"
                   "Corresponde definir que el objetivo principal de la leyes de violencia familiar es crear un marco procesal que permita adoptar las medidas urgentes tendientes a neutralizar las crisis familiar existente, evitando el agravamiento de los perjuicios concretos derivados del maltrato, para lo cual se necesita de adopción de medidas eficaces, urgentes y transitorias."+"\n"
                   "Que, ante el relato de la denunciante, estimo que corresponde, en pos de su protección y del grupo familiar que esta integra, proceder a la exclusión del hogar del denunciado, ya que, tal como lo sostiene la doctrina... 'la necesidad o conveniencia de decretar una medida tan gravosa como es excluir del hogar a un miembro de la familia derivará de los hechos generadores de la denuncia, toda vez que si quien la efectúa u otras personas que habitan la vivienda familiar resultan ser víctimas de actos de violencia o de maltrato (sea físico o psíquico) que pudiesen poner en peligro su integridad o su vida, el juez podrá disponer la medida ordenando que el autor de dichos actos deje de habitar el hogar...' (Guahnon Silvia V., Sistemas de Protección en Materia de Violencia Familiar, Sistemas Cautelares y Procesos Urgentes, Revista de Derecho Procesal, Rubinzal Culzoni Editores, pág. 237; debe entenderse que el sistema de protección que establece la ley, pone en marcha el andamiaje judicial ante la existencia de violencia en el ámbito que la misma norma circunscribe, sin perjuicio que ante la mera probabilidad o sospecha de que ello este ocurriendo o que pudiera ocurrir, se deben ordenar las medidas en forma urgente e inaudita parte, y en este caso, aún manteniendo su naturaleza de medida cautelar, el requisito de verosimilitud se torna mas flexible, por lo que los datos de la denuncia por mínimos que sean, siempre que reflejen una potencial situación de peligro para la denunciante habilitan a este juzgador a adoptar las medidas que la  normativa vigente establece.'"+"\n"
                   "De igual manera corresponde ordenar al denunciado la prohibición de acceso y acercamiento al domicilio supra mencionado, como también a la propia denunciante en todos los ámbitos donde esta desarrolle sus actividades, tales como: lugares de trabajo, circulación, lugares donde concurra por razones sociales, deportivas, religiosas, de salud, por esparcimiento, etc., prohibición que se extiende además a contactarla por telefonía fija o móvil, redes sociales, correo electrónico, medios postales, etc., todo ello por el mismo término al de la exclusión dispuesta."+"\n"
                   "Asimismo, a los fines de no menoscabar el derecho de defensa  del denunciado deberá hacérsele saber que podrá comparecer a estos obrados con patrocinio letrado de Defensor Oficial o abogado particular."+"\n"
                   "De igual manera se dará intervención a la Subsecretaria de la Mujer y Familia, Dirección de Genero, dependiente del Ministerio de Desarrollo Social de la Provincia de Misiones, para que arbitren los medios necesarios en protección de la víctima y su entorno familiar."+"\n")

  
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
    #////////////////////////////////////////// E J E M P L O ///////////////////////////////////////////////
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
   
    os.system ("cls")
    while True: 
        reintegrodenunciante = input("¿Solicita la denunciante reintegro al hogar? (1=SI, 0=NO): ")
        if reintegrodenunciante == "1":
            contadorromano=contadorromano+1
            reintegrodenunciante=(romano[contadorromano]+",con el correspondiente REINTEGRO de "+sexo+""+NombreDenunciante+"a su domicilio")
            break
        if reintegrodenunciante == "0":
            break



    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    resuelvo=("ACA VA EL POR QUE DEL RESUELVO"+"\n"
        "RESUELVO: "+romano[0]+"PARRAFO DE PUNTO I"+"\n"
        +romano[1]+"PARRAFO DE PUNTO II"+"\n"
        +romano[2]+"PARRAFO DE PUNTO III"+"\n"
        +romano[3]+"PARRAFO DE PUNTO IV"+"\n"
        +romano[4]+"PARRAFO DE PUNTO V "+"\n")
    Variablefinal=Variablefinal+resuelvo  
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #//////////////////////////////ACA VAN LAS MEDIDAS A TOMAR INDEPENDIENTEMENTE DE CADA PROGRAMA//////////////////////////////////////////