# Flask - Python
Flask (Framework de Python) - Aplicaciones Web

## Commands Course

```
virtualenv -p python3 env
pip list
python -m pip install --upgrade pip
pip install flask

app/templates → Flask reconoce este nombre de directorio donde se almacenan las plantillas


MySql:

pip install flask-mysqldb


```




## Entornos Virtuales con Python (Módulo virtualenv)

```
Note Geo:
1.	Instalar python en su version mas reciente 3.x.x
2.	Instalar pip
3.	Mediante pip instalamos virtualenv pip install virtualenv 
    (https://docs.python.org/3/tutorial/venv.html)
4.	Creamos el ambiente basándonos en el ambiente virtual
5.	Ejecutamos el siguiente comando Python -m venv name_folder-env
6.	Para activar el ambiente virutal de Python ejecutamos el siguiente archivo.
7.	Comado para activar el venv name_folder-env\Scripts\activate.bat
8.	Una vez activado el venv procedemos a instalar los requirements.txt
9.	Ejecutamos el comando pip install -r requirements.txt


Other - Course:

Folder: entorno - env
Entorno virtuales con diferentes caracteristicas de python.
Instalar python de forma global.

pip list → Lista los paqueres de python instalados de forma global
virtualenv -p python3 env → crear entorno virtual
env\Scripts\activate → Ejecuto entorno virtual
pip list


pip install flask

pip freeze > requirements.txt → Exportar los paquetes que tenemos instalados
pip install -r requirements.txt


```

## PIP (Package Installer for Python): Administrador de Paquetes de Python

```
pip list → Lista de paquetes globales
pip -m pip install --upgrate pip → Actualizar PIP
pip list --outdated → Ver paquetes desactualizados
pip show django → Ver información de un paquete
pip help install → Ver ayuda de un comando
pip check django → Informa si un paquete tiene alguna dependencia faltante.
pip freeze → Ver los paquetes actualmente instalados
pip freeze>req.txt

```







