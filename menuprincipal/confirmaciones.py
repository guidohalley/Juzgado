def confirmaciones():
	import CrearCarpetas
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
	contadorromano=5
	#------------------------------------------------------------------------------------------------------------------------
	# MENU SECTOR 1 DENUNCIANTE----------------------------------------------------------------------------------------------
	#------------------------------------------------------------------------------------------------------------------------
