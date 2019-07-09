import time
import os

print(" _   _  _         _                     _         ______                    _  _  _              ")
print("| | | |(_)       | |                   (_)        |  ___|                  (_)| |(_)             ")
print("| | | | _   ___  | |  ___  _ __    ___  _   __ _  | |_     __ _  _ __ ___   _ | | _   __ _  _ __ ")
print("| | | || | / _ \ | | / _ \| '_ \  / __|| | / _` | |  _|   / _` || '_ ` _ \ | || || | / _` || '__|")
print("\ \_/ /| || (_) || ||  __/| | | || (__ | || (_| | | |    | (_| || | | | | || || || || (_| || |   ")
print(" \___/ |_| \___/ |_| \___||_| |_| \___||_| \__,_| \_|     \__,_||_| |_| |_||_||_||_| \__,_||_|   ")                                                                                              
print(" _   _         _  _                _____                         ")
print("| | | |       | || |              |_   _|                        ")
print("| |_| |  __ _ | || |  ___  _   _    | |    ___   __ _  _ __ ___  ")
print("|  _  | / _` || || | / _ \| | | |   | |   / _ \ / _` || '_ ` _ \ ")
print("| | | || (_| || || ||  __/| |_| |   | |  |  __/| (_| || | | | | |")
print(" _| |_/ \__,_||_||_| \___| \__, |   \_/   \___| \__,_||_| |_| |_|")
print("                            __/ |                                ")
print("                           |___/                                 ")
time.sleep(2)
print("   ___                      _                             ___                    _                       ___ ")
print("  / _ \   _  _   ___     __| |  ___   ___  ___   __ _    | _ \  ___   ___  ___  | | __ __  ___   _ _    |__ \ ")
print(" | (_) | | || | / -_)   / _` | / -_) (_-< / -_) / _` |   |   / / -_) (_-< / _ \ | | \ V / / -_) | '_|     /_/")
print("  \__\_\  \_,_| \___|   \__,_| \___| /__/ \___| \__,_|   |_|_\ \___| /__/ \___/ |_|  \_/  \___| |_|      (_) ")
print("                                                                                                             ")
print ("1 - RESOLUCION DE PROHIBICION DE ACERCAMIENTO")
print ("2 - RESOLUCION DE EXCLUSION DE HOGAR")
#print ("3 - RESOLUCION CONFIRMACION DE MEDIDAS DE JUZGADO DE PAZ")
opcion=input("Ingrese Opcion: ")
os.system ("cls")

if opcion=="1":
    import os
    time.sleep(2)
    import prohibicion
    prohibicion.prohibicion()



if opcion=="2":
    import os
    time.sleep(2)
    import exclusion
    exclusion.exclusion()

    import menuprincipal
    menuprincipal.menuprincipal()