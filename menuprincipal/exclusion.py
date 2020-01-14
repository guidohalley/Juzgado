def exclusion():
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
        print ("****************************************RESOLUCION DE EXCLUSION DE HOGAR******************************")
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
    resuelvo=("Por ello, Ley Provincial XIV, Nº 6, las facultades atribuidas al suscripto por el art 4 de la misma, normas procesales y ccs.:"+"\n"
        "RESUELVO: "+romano[0]+"Téngase por recibida denuncia de "+sexo+""+NombreDenunciante+", D.N.I. Nº "+Dnidenunciante+", domiciliada realmente en "+DomicilioDenunciante+"\n"
        +romano[1]+"Por iniciada acción de Violencia Familiar en los términos de la ley XIV-Nº 6 contra "+sexo1+" "+NombreDenunciado+" , D.N.I. Nº "+Dnidenunciado+", domiciliado actualmente "+DomicilioDenunciante+"\n"
        +romano[2]+"Procédase a Excluir del Hogar "+sexo1+" "+NombreDenunciado+", D.N.I. Nº"+Dnidenunciado+" con sus pertenencias personales, el que se asienta en el domicilio sito en "+DomicilioDenunciante+", por el término de "+cm+" y  en este mismo acto, ordenar la Prohibición de Acceso y Acercamiento "+sexo1+" "+NombreDenunciado+" al domicilio "+DomicilioDenunciante+", como también hacia "+sexo+" "+NombreDenunciante+" y a todos los ámbitos donde desarrolle sus actividades, tales como: lugares de trabajo, circulación, lugares donde concurra por razones sociales, deportivas, religiosas, de salud, por esparcimiento, etc., prohibición que se extiende además a contactarla por telefonía fija o móvil, redes sociales, correo electrónico, medios postales, etc., y/o por cualquier medio signifique intromisión injustificada con relación a la denunciante, todo ello por el mismo término al de la exclusión dispuesta, todo ello bajo apercibimiento de que ante la desobediencia a la presente medida, se procederá a su ARRESTO por incumplimiento de orden judicial, en los términos y conforme a las facultades otorgadas al suscripto por el artículo 658 ley XII - Nº 27 DJM, quedando a disposición del Juez de Instrucción que por turno corresponda y/o de imponerle multa en los  términos del art. 5 de la Ley XIV Nº 6 DJM."+"\n"
        +romano[3]+"Líbrese oficio a la Dirección de Asuntos de Familia y Género, Dirección General de Seguridad de la Policía de la Provincia de Misiones, a fin de que arbitren los medios necesarios para que una Comisión Policial a cargo de un Oficial de Policía que presente idoneidad para el diligenciamiento de la medida, teniendo en cuenta la situación particular de cada caso (si hay menores de edad, discapacitados, personas ancianas, si algunos de los involucrados revisten condición de agentes de seguridad de cualquier fuerza, y en su caso si en el lugar pueden haber armas de cualquier naturaleza) para que se constituyan en el término de 24 horas, en el domicilio sito en "+DomicilioDenunciante+" CUMPLIMENTEN CON LA EXCLUSIÓN DEL HOGAR "+sexo1+""+NombreDenunciado+" "+reintegrodenunciante+" ""Y NOTIFIQUEN LA PROHIBICIÓN DE ACCESO Y ACERCAMIENTO del mismo  a "+sexo+" "+NombreDenunciante+", su domicilio, lugares de trabajo y concurrencia por el termino de "+cm+", debiendo en dicho acto la comisión asignada, proceder resguardando la integridad física de la denunciante, del denunciado y todo el grupo familiar, teniéndose presente que la problemática familiar debe ser abordada con un elevado criterio de protección y respeto al núcleo familiar. Se le hace saber al denunciado que ante la desobediencia a la presente medida, se procederá a su ARRESTO por incumplimiento de orden judicial, en los términos y conforme a las facultades otorgadas al suscripto por el artículo 658 ley XII - No 27 DJM, quedando a disposición del Juez de Instrucción que por turno corresponda y/o de imponerle multa en los términos del art. 5 de la Ley XIV No 6 DJM. Se hace saber que la comisión policial se encuentra facultada en caso de ser estrictamente necesario allanar domicilio y utilizar los servicios de un cerrajero y toda otra medida prudente al solo efecto del cumplimiento de la orden judicial, debiéndose comunicar al suscripto en el plazo de 48 horas, la comisión asignada dando detalle pormenorizado de los agentes intervinientes y el resultado de la diligencia. Asimismo poner en conocimiento del denunciado excluido, que en este mismo acto puede retirar sus ropas, documentos personales, elementos de higiene y/o herramientas de trabajo si las tuviera, debiendo en dicho acto la comisión policial designada al efecto, realizar inventario de todas las pertenencias extraídas del hogar por parte del denunciado. Queda autorizado a intervenir en el diligenciamiento al Defensor Oficial y/o quien este designe con facultades de práctica. Debiendo informar a la Defensoría Oficial o abogado patrocinante el momento del diligenciamiento de la medida. Queda estrictamente prohibida la presencia de personas ajenas al excluido y a la Comisión Policial interviniente en el acto de exclusión."+"\n"
        +romano[4]+"Se hace saber al denunciado que podrá comparecer ante este juzgado y en estos obrados a fin de ejercer su derecho de defensa, con patrocinio letrado de abogado particular y/o Defensor Oficial. "+"\n")
    Variablefinal=Variablefinal+resuelvo  
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////




    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system ("cls")
    cerrarWhile=0
    while cerrarWhile==0:
        pupilar = input("¿Hay menores de 18 años en la causa?  (1=SI, 0=NO): ")
        if pupilar=="0":
            break
        if pupilar != "1" and pupilar != "0":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if pupilar == "1":
            pupilarhijos=(romano[contadorromano]+"Asimismo ante la presencia de niños, niñas y adolescentes, corresponde dar intervención a la Defensoría Oficial que por turno corresponda a fin de que asuma la representación complementaria de los mismos y se pronuncie respecto a los supremos intereses de los niños, niñas y adolescentes respecto a la presente denuncia y a las medidas que en su consecuencia se dicten."+"\n")
            Variablefinal=Variablefinal+pupilarhijos
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
                    guardapro = (romano[contadorromano]+"En consecuencia, y atento a las manifestaciones de la denunciante y lo expuesto precedentemente, se puede colegir que sería conveniente otorgar el Cuidado Personal Provisorio de las jovenes de marras "+nombrehijos+" a "+sexo+" "+NombreDenunciante+" en beneficio de las jóvenes debiendo cumplir con los deberes inherentes respecto de los niños consagrados por la Convención de los Derechos del Niño y el Pacto de San José de Costa Rica. Por lo expuesto, las disposiciones del art. 234 del C. P. C. y C.; y Convención Internacional sobre los Derechos del Niño. "+"\n")
                    Variablefinal=Variablefinal+guardapro
                    cerrarWhile=cerrarWhile+1
                    break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system ("cls")
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
    os.system ("cls")
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

    os.system ("cls")
    while True:
        fiscalresu = input("¿Solicita intervencion del fiscal de instruccion Penal ? (1=SI, 0=NO): ")
        if fiscalresu == "1":
            contadorromano=contadorromano+1
            fiscalresu=(romano[contadorromano]+"Líbrese Oficio al Fiscal de Instrucción Penal en turno, a fin que se notifique de todo lo actuado en este fuero, adjuntando copia simple de la denuncia que antecede y determine si la conducta desplegada por "+sexo1+" "+NombreDenunciado+" D.N.I. Nº"+Dnidenunciado+" "+DomicilioDenunciado+", Con Telefono Nº "+NumeroDeTelefonoDenunciado+", constituye delito(conf. al Código Penal Argentino) y en su caso si corresponde instar la acción penal conforme a sus facultades y competencia."+"\n")
            Variablefinal=Variablefinal+fiscalresu
            break
        if fiscalresu!="0" and fiscalresu!="1":
            print (". . . OPCION INCORRECTA, VUELVA A INGRESAR . . .")
        if fiscalresu == "0":
            break

    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS//////////////////////En consecuencia///////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////

    os.system ("cls")
    while True: 
        resudefensoria = input("¿Solicita intervencion de defensoria ? (1=SI, 0=NO): ")
        if resudefensoria == "1":
            contadorromano=contadorromano+1
            resudefensoria =(romano[contadorromano]+"Girar las presentes a la Defensoría Oficial de Violencia Familiar y/o que corresponda, a fin de que citen a la denunciante para  asumir el patrocinio letrado y/o manifieste si opta por patrocinio particular estando a su cargo la notificación a " + sexo +" "+ NombreDenunciante + "donde este se encuentre; haciéndose saber que deberán diligenciarse en forma urgente las medidas judiciales ordenadas en las  causas de violencia familiar e informar al suscripto, el resultado de dichas diligencias, bajo la exclusiva responsabilidad de la Defensoría Oficial interviniente."+"\n")
            Variablefinal = Variablefinal+resudefensoria
            break
        if resudefensoria!="0" and resudefensoria!="1":
            print ("OPCION INCORRECTA, VUELVA A INGRESAR...")
        if resudefensoria == "0":
            break
    #///////////////////////////////////////////PREGUNTAS DE MEDIDAS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    os.system ("cls")
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
    os.system ("cls")
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
    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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

    os.system ("cls")
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
    finalres=(romano[contadorromano]+"Regístrese, Cópiese, Notifíquese."+"\n"+"HYG")
    Variablefinal=Variablefinal+finalres
    os.system ("cls")
    time.sleep(2)
    archivo=open(os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia\\Exclusion\\ResolucionFin"+" "+ NdeExpediente +".txt","a")
    archivo.write("Posadas, "+Dia+" de "+Mes+" del "+anio)
    archivo.write("\n")
    archivo.write("Y VISTOS: Estos autos caratulados: Expte Nº "+ NdeExpediente+"/"+AnioExpediente+ " " + "-" + " " + NombreDenunciante + " " + "C/" +" "+ NombreDenunciado + " " + "S/" + " " + "Violencia Familiar")
    archivo.write("\n")
    archivo.write(Variablefinal)
    archivo.close()
    #///////////////////////////////////////////CREADOR DE ARCHIVOS/////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    print ("********************************************")
    print ("****** ARCHIVO GENERADO EXITOSAMENTE *******")
    print ("********************************************")
    time.sleep(2)
    os.system("cls")
    print ("******** volviendo al menu principal********")
    time.sleep(3)
    os.system("cls")
    import menuprincipal
    menuprincipal
    print ("BY GUIDO HALLEY JUZGADO DE VIOLENCIA FAMILIAR")
    time.sleep(2)
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY------------------------------------------------------
#-----------------------------------------------------------POR GUIDO HALLEY-----------------------------------------------------
  