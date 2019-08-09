import os

def crear_directorio(ruta,ruta1,ruta2, ruta3):
	try:
		
		os.makedirs(ruta)
		os.makedirs(ruta1)
		os.makedirs(ruta2)
		os.makedirs(ruta3)
		return True

	except :
		return False

directorio_escritorio = os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia"
directorio_escritorio1 = os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia\\Prohibicion"
directorio_escritorio2 = os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia\\Exclusion"
directorio_escritorio3 = os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia\\Confirmacion"
#directorio_escritorio4 = os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia\\Renovaciones de Medidas"
#directorio_escritorio5 = os.environ['USERPROFILE'] + "\\Desktop\\Juzgado de Violencia Familia\\Resoluciones Desestimatorias"

crear_directorio(directorio_escritorio, directorio_escritorio1, directorio_escritorio2, directorio_escritorio3,)
