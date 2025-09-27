
# Intérprete con Lenguaje Gamer

Intérprete de lenguaje Gamer en español con interfaz gráfica (Tkinter) y pruebas automáticas.

## Requisitos

- Instalar Python 3.13.7 
- Instalar dependencias (si tienes un archivo `requirements.txt`):
  ```
  pip install -r requirements.txt
  ```

## Cómo ejecutar la GUI

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el archivo principal:
   ```
   python main.py
   ```
   *(Reemplaza `main.py` por el nombre de tu archivo GUI si es diferente)*

3. Escribe instrucciones en la interfaz y presiona el botón para complilar/ejecutar.

## Ejemplos de instrucciones

- `crear vida = 100`
- `curar vida pocion`
- `dividir oro cofres`
- `crear mana = 3.14`
- `crear nombre = Juan`
- `decir vida`
- `golpear enemigo jugador`

## Cómo ejecutar los tests

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:
   ```
   pytest tests/
   ```

## Estructura del proyecto

- `interprete/` — Módulos del intérprete (lexer, parser, interpreter)
- `tests/` — Pruebas unitarias
- `main.py` — Archivo principal de la GUI

## Créditos

Desarrollado por:
- Christian Jafeth Pena Espinoza 
- Luciana Chacon Castillo


