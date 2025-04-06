# API REST de Reconocimiento Facial con Flask

# Integrantes:
- Jhonatan Ocoro Perea
- Jorge Isaac Gongora Naranjo
- Maria del Mar Garces Celorio

Este proyecto implementa una API REST para la detección y reconocimiento facial utilizando Flask, OpenCV y Face-Recognition.

## Instalación
1. Clonar el repositorio.
2. Crear un entorno virtual: ´python -m venv venv´
   - En Windows: `python -m venv venv`
   - En Linux/Mac: `python3 -m venv venv`	
3. Activar el entorno virtual: ´venv\Scripts\activate´
   - En Windows: `venv\Scripts\activate`
   - En Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias: ´pip install -r requirements.txt´
   - En Windows: `pip install -r requirements.txt`
   - En Linux/Mac: `pip3 install -r requirements.txt`
   - En caso de error, instalar las dependencias manualmente:
     - `pip install Flask`
     - `pip install Flask-Cors`
     - `pip install opencv-python`
     - `pip install face_recognition`
     - `pip install numpy`
     - `pip install Pillow`
5. Ejecutar la aplicación: ´python server.py´
   - En Windows: `python server.py`
   - En Linux/Mac: `python3 server.py`
6. Probar la API utilizando Postman o cualquier cliente HTTP.