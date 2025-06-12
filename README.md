# Requerimientos

## Crear entorno virtual
Recomendado usar un entorno virtual con el comando:  
`python -m venv venv`

## Activar entorno virtual
- En **Windows**:  
  `venv\Scripts\activate`
- En **Mac/Linux**:  
  `source venv/bin/activate`

## Instalar dependencias
Con el entorno virtual activado y estando dentro de la carpeta del juego, instala las dependencias ejecutando:  
`pip install -r requirements.txt`

## Ejecutar el juego
Con el entorno virtual abierto, ejecuta:  
`python main.py`  
Nota: "python" puede ser reemplazado por `py`, `python.exe` o `python3.XX` (la X siendo la versión).

## Cerrar el entorno virtual
`deactivate`

## Cómo ejecutar las pruebas
Asegúrate de estar en la raíz del proyecto y ejecuta:
`python -m unittest discover -s tests`
