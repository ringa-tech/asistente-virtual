
# Asistente virtual
Este repositorio es el código para el video del Asistente Virtual en el canal Ringa Tech:
https://youtu.be/-0tIy8wWtzE

## Configuración
Para ejecutar el proyecto es necesario:
- Descargar el repositorio
- Opcional: Crea un ambiente virtual
- Instala las dependencias ejecutando 
	- ```  pip install -r requirements.txt ```
- Crea un archivo llamado ```.env```
	- En el archivo coloca las llaves. Para el proyecto tal cual del video (y este repositorio) estoy utilizando:
	- ```OPENAI_API_KEY=XXXXXX```
	- ```ELEVENLABS_API_KEY=XXXXXX```
	- ```WEATHER_API_KEY=XXXXXX```

## Ajustes
El proyecto cuenta con algunas cosas que quizá quieras modificar, por ejemplo:

- En la clase LLM puedes modificar para que el asistente no sea "malhablado". Se utiliza en 2 lugares del archivo.
- En la clase PcCommand, abre Chrome buscándolo en una ruta fija para Windows. Puedes modificarlo para que busque el ejecutable en Mac / Linux.

## Ejecución
- Este proyecto utiliza Flask. Puedes levantar el servidor en modo debug por defecto en el puerto 5000 con el comando
	- ```flask --app app run --debug```
	- En tu navegador ve a http://localhost:5000
	- Da clic para comenzar a grabar (pedirá permiso). Dar clic para dejar de grabar
	- Espera y ve como domina al mundo


## ¿Problemas?

Solo lo probé en mi equipo así que si tienes problemas, levanta un issue aquí en Github, con el mayor detalle que puedas (versión de python, de paquetes, mensaje completo de error, etc).

Si eres ninja y lo solucionas, ¡levanta un Pull Request!

## Licencias
- Imagen de micrófono por Freepik