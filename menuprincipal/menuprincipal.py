import time
import os

print(" _   _  _         _                     _         ______                    _  _  _              ")
print("| | | |(_)       | |                   (_)        |  ___|                  (_)| |(_)             ")
print("| | | | _   ___  | |  ___  _ __    ___  _   __ _  | |_     __ _  _ __ ___   _ | | _   __ _  _ __ ")
print("| | | || | / _ \ | | / _ \| '_ \  / __|| | / _` | |  _|   / _` || '_ ` _ \ | || || | / _` || '__|")
print("\ \_/ /| || (_) || ||  __/| | | || (__ | || (_| | | |    | (_| || | | | | || || || || (_| || |   ")
print(" \___/ |_| \___/ |_| \___||_| |_| \___||_| \__,_| \_|     \__,_||_| |_| |_||_||_||_| \__,_||_|   ")                                                                                              
print(" _   _         _  _               ")
print("| | | |       | || |              ")
print("| |_| |  __ _ | || |  ___  _   _  ")
print("|  _  | / _` || || | / _ \| | | | ")
print("| | | || (_| || || ||  __/| |_| | ")
print(" _| |_/ \__,_||_||_| \___| \__, | ")
print("                            __/ | ")
print("                           |___/  ")
time.sleep(2)
print("   ___                      _                             ___                    _                       ___ ")
print("  / _ \   _  _   ___     __| |  ___   ___  ___   __ _    | _ \  ___   ___  ___  | | __ __  ___   _ _    |__ \ ")
print(" | (_) | | || | / -_)   / _` | / -_) (_-< / -_) / _` |   |   / / -_) (_-< / _ \ | | \ V / / -_) | '_|     /_/")
print("  \__\_\  \_,_| \___|   \__,_| \___| /__/ \___| \__,_|   |_|_\ \___| /__/ \___/ |_|  \_/  \___| |_|      (_) ")
print("                                                                                                             ")
print ("1 - RESOLUCION DE PROHIBICION DE ACERCAMIENTO")
print ("2 - RESOLUCION DE EXCLUSION DE HOGAR")
print ("3 - RESOLUCION DE CONFIRMACION **FALTA TERMINAR**")
opcion=input("Ingrese Opcion: ")
os.system ("cls")

if opcion=="1":
    import os
    print("ESTE PROGRAMA ES UNA VERSION DE PRUEBA ECHO POR GUIDO HALLEY")
    print("EJECUTANDO PROHIBICION DE ACERCAMIENTO")
    time.sleep(3)
    import prohibicion
    prohibicion.prohibicion()



if opcion=="2":
    import os
    print("ESTE PROGRAMA ES UNA VERSION DE PRUEBA ECHO POR GUIDO HALLEY")
    print("EJECUTANDO EXCLUSION DE HOGAR")
    time.sleep(3)
    import exclusion
    exclusion.exclusion()

if opcion=="3":
    import os
    print("ESTE PROGRAMA ES UNA VERSION DE PRUEBA ECHO POR GUIDO HALLEY")
    print("EJECUTANDO CONFIRMACIONES ** VERSION TEST ** ")
    time.sleep(3)
    import confirmaciones
    confirmaciones.confirmaciones()


