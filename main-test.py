import time 
import pywhatkit as kit

nombre = "atzel"
nombre = nombre.upper()

hora = time.localtime()
hora_envio = (hora.tm_hour,(hora.tm_min + 2) %60)
kit.sendwhatmsg("+5491160155806", f"Hola {nombre} ahora si funciona esta poha ?",hora_envio[0], hora_envio[1]) 


