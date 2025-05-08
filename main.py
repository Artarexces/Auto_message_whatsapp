import time 
import pywhatkit as kit 

archivo_contacto = "contactos.txt" 

mensaje_base = "Hola {nombre}, te voy a romper el orto con la comision."

with open(archivo_contacto, "r", encoding="utf-8") as archivo:
    contactos = [linea.strip().split(",")for linea in archivo if linea.strip()]

hora_actual = time.localtime()
minuto = (hora_actual.tm_min + 2) % 60
hora_extra = (hora_actual.tm_min +2) // 60
hora_envio = (hora_actual.tm_hour + hora_extra, minuto) 
