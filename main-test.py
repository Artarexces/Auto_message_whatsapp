import time 
import pywhatkit as kit

# App de prueba

nombre = "test" # <-- Añade el nombre del contacto. 
nombre = nombre.capitalize()

hora = time.localtime()
hora_envio = (hora.tm_hour,(hora.tm_min + 2) %60) # <-- Modificale el tiempo de envio
kit.sendwhatmsg("+5491160155806", f"Hola {nombre} pobrando si funciona!",hora_envio[0], hora_envio[1]) 


