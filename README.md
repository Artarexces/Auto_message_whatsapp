

# Auto Message WhatsApp

Este repositorio contiene un script en Python para **automatizar el envío de mensajes por WhatsApp** usando la librería [PyWhatKit](https://github.com/Ankit404butfound/PyWhatKit).

> ⚠️ **Importante:** Debes tener abierta tu sesión de WhatsApp Web en el navegador predeterminado para que el script funcione correctamente.

---

## ✨ Características

- Lee una lista de contactos desde un archivo de texto.
- Permite definir, para cada contacto, el mensaje a enviar y la hora programada.
- Automatiza la apertura de WhatsApp Web y el envío del mensaje en el horario indicado.
- Incluye ejemplos de archivos de contacto para facilitar la configuración.

---

## 🛠️ Requisitos
;
- Python 3.7 o superior  
- Navegador web (Chrome o Edge recomendado)  
- Librería PyWhatKit  
- Conexión a Internet estable  

Instala las dependencias con:

##bash

pip install pywhatkit

---

## 📂 Estructura de archivos

Auto_message_whatsapp/


├── contactos.txt    
├── contactos_ejemplo.txt   
├── PyWhatKit_DB.txt            
├── main.py         
├── main-test.py   
└── README.md                

---

## 📥 Uso


### 1. Configura tu lista de contactos

Edita `contactos.txt` (o copia el formato de `contactos_ejemplo.txt`) siguiendo la estructura:

+54911XXXXXXX|“¡Hola Joe! ¿Cómo estás?”|14|30

+54911YYYYYYY|“Recordatorio: reunión a las 16:00.”|15|45


Cada línea contiene:

- **Número de teléfono** (con código de país y sin espacios)
- **Mensaje** (entre comillas)
- **Hora** (en formato 24 h)
- **Minutos**

---

### 2. Ejecuta el script

##bash

python main.py

El script leerá cada línea de contactos.txt y programará el envío en WhatsApp Web.

## Verifica la ejecución
Se abrirá una pestaña nueva por cada mensaje programado.

PyWhatKit registrará en PyWhatKit_DB.txt la hora y estado de cada envío.

---

## ✅ Ejecución de pruebas

Para ejecutar el script de prueba sin afectar tus datos reales:

```bash
python main-test.py

Este archivo simula un envío utilizando contactos_ejemplo.txt.
