import time 
import pywhatkit as kit

hora = time.localtime()
hora_envio = (hora.tm_hour,(hora.tm_min + 2) %60)
kit.sendwhatmsg("+5491171038515", "Traniella te saluda desde python",hora_envio[0], hora_envio[1])