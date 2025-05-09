import time 
import pywhatkit as kit 

archivo_contacto = "contactos_ejemplo.txt" # <-- Aca podes cambiar por el archivo txt que gustes.

mensaje_base = "Hola {nombre}, saludos!."

with open (archivo_contacto, "r", encoding="utf-8") as archivo:
    contactos = [linea.strip().split(",") for linea in archivo if linea.strip()]

hora_actual = time.localtime()
minuto = (hora_actual.tm_min + 2) % 60
hora_extra = (hora_actual.tm_min +2) // 60
hora_envio = (hora_actual.tm_hour + hora_extra, minuto) 

for i, (nombre, numero) in enumerate(contactos):
    mensaje_personalizado = mensaje_base.format(nombre=nombre)
    envio_hora = hora_envio[0] + ((hora_envio[1] + i)// 60)
    envio_minuto = (hora_envio[1]+i) % 60
    print(f"Enviado a {nombre} ({numero}) a las {hora_envio}:{envio_minuto}...")
    kit.sendwhatmsg_instantly(numero, mensaje_personalizado, wait_time=10, tab_close=True,close_time=3)
    
time.sleep(5)