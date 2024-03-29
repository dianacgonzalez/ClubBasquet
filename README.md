# ClubBasquet

# Alumno: Facundo Gonzalez y Diana Gonzalez

# Nombre del Proyecto: Club de Basquet

# Descripción del Proyecto

Página Web destinada a un club de básquet que desea organizar las categorias de los jugadores vinculado con su respectivo profesor.

A fin de navegar por las secciones de la página web, el usuario será requerido iniciar sesión o registrarse en caso de no contar con usuario o contraseña. En ambas opciones, una vez la página valide la autenticación del usuario, este será redirigido al inicio de la página web.

Los usuarios pueden realizar las siguientes accciones:

    Agregar, Visualizar, Editar y Borrar: Profesores, Alumnos, Categorias y Equipos.
    Iniciar (Loguearse) y Cerrar (Desloguearse) Sesión
    Ver información Nosotros
    Ver Inicio

# Como Descargar, instalar y Ejecutar la App desde Visual Studio Code

Iniciar Visual Studio Code
Ir a "Terminal"/"nueva termina"

# Para descargar el proyecto que contiene la App 

En el caso que se requiera, ejecutar:
git remote add origin https://github.com/dianacgonzalez/ClubBasquet.git

Modeverse a una carpeta vacía y ejecutar:
git clone https://github.com/dianacgonzalez/ClubBasquet.git

# Para abrir el proyecto que contiene la App 

Abrir la Carpeta 

# Para configurar VSC

Crear en el entorno virtual:
 `python -m venv .venv` (Windows)
 `python3 -m venv .venv` (Linux o Mac)

Luego activar el entorno virtual:
 `.\.venv\Scripts\activate`  (Windows Powershell)
 `source .venv/bin/activate` (Linux o Mac)

A continuación se deben instalar los requerimientos con:
pip install -r requirements.txt


# Para ejecutar la App 

Luego, debe moverse al path "project" y ejecutar:
python manage.py runserver

Por último, desde un navegador, ingresar a:
http://127.0.0.1:8000/


Repositorio https://github.com/dianacgonzalez/ClubBasquet.git

Video Demostración

https://drive.google.com/drive/folders/1G5GfoJHR-6LKEP6fPFBBeiWmQUu9yvnj?usp=sharing
