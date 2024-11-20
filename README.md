# 🏠 Proyecto E-Commerce EDB
Proyecto para crear un e-commerce para la empresa EDB. Forma parte de la asignatura PGPI.

## Configuración e inicio del proyecto
Antes de comenzar, será necesario tener instalado [Python](https://www.python.org/downloads/). Una vez tengas Python instalado en tu equipo Windows, deberás ejecutar los siguientes comandos en el directorio raíz para configurar el proyecto:

1. Inicializar el entorno virtual: `python -m venv venv`
2. Activar el entorno virtual: `.\venv\Script\activate`
3. Instalar dependencias: `pip install -r requirements.txt`

Una vez realizados los pasos anteriores, simplemente ejecutar el proyecto:
```
python manage.py runserver
```

Enhorabuena, ya tendrías el proyecto ejecutándose en tu equipo 🎉.

Luego, como guía para expandir la aplicación, tenemos los siguientes comandos:

1. Crear una nueva app o módulo: `python manage.py startapp <nombre del módulo>`
2. Añadir las migraciones por cambios en el modelo: `python manage.py makemigrations`
3. Aplicar las migraciones: `python manage.py migrate`
4. Añadir super usuarios: `python manage.py createsuperuser`
5. Nos piden instalar nuevas librerías, y ya las hemos instalado: `pip freeze > requirements.txt`
6. Añadir un archivo de migración de datos: `python manage.py makemigrations --empty <nombre del módulo al que añadir el fichero>`
7. Acceder al shell de datos para trabajar con la bbdd: `python manage.py shell`
