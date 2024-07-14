Editor de Texto Interactivo con Pygame
Este proyecto implementa un editor de texto interactivo utilizando la biblioteca Pygame. Permite abrir archivos existentes, crear nuevos archivos de texto, guardar cambios y salir del editor.

Requisitos
Python 3.x (recomendado 3.6+)
Pygame 2.6.0
Configuración del Entorno Virtual (opcional pero recomendado)
Se recomienda utilizar un entorno virtual para evitar conflictos con las dependencias de otros proyectos. A continuación, se muestra cómo configurarlo:

python -m venv venv #para windows
venv\Scripts\activate

Instalación de Pygame
Dentro del entorno virtual activado, instala Pygame:
pip install pygame==2.6.0

Ejecución del Editor de Texto
Para ejecutar el editor de texto, asegúrate de estar dentro del entorno virtual (si lo estás utilizando) y ejecuta main.py:
python main.py

Funcionalidades del Editor de Texto
Menú Principal: Permite elegir entre abrir un archivo existente, crear un nuevo archivo, guardar el archivo actual o salir del editor.
Edición de Texto: Permite escribir, borrar y navegar por el texto utilizando el teclado.
Guardar y Abrir Archivos: Guarda el contenido actual en un archivo o abre un archivo existente para su edición.
Interfaz Gráfica: Utiliza Pygame para la interfaz gráfica, con botones interactivos y manejo de eventos de teclado y ratón.