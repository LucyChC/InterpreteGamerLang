# Intérprete con Lenguaje Gamer

Intérprete de lenguaje Gamer en español con interfaz gráfica (Tkinter) y pruebas automáticas.

## Requisitos

- Python 3.13.7
- Instalar dependencias:
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

3. Escribe instrucciones en la interfaz y presiona el botón para compilar/ejecutar.

## Ejemplos de instrucciones

- `crear vida = 100`
- `curar vida pocion`
- `dividir oro cofres`
- `crear mana = 3.14`
- `crear nombre = Juan`
- `decir vida`
- `golpear enemigo jugador`

## Palabras clave y funciones predefinidas

Estas son las instrucciones que puedes usar en el intérprete Gamer:

- `crear <nombre> = <valor>` — Define una variable.
- `curar <a> <b>` — Suma dos variables.
- `golpear <a> <b>` — Resta dos variables.
- `multiplicar <a> <b>` — Multiplica dos variables.
- `dividir <a> <b>` — Divide dos variables.
- `poder <a> <b>` — Eleva una variable a la potencia de otra.
- `revivir <a>` — Calcula la raíz cuadrada de una variable.
- `xp <a>` — Valor absoluto de una variable.
- `jefe <a> <b> ...` — Máximo de una lista de variables.
- `esbirro <a> <b> ...` — Mínimo de una lista de variables.
- `decir <a>` — Muestra el valor de una variable.

### Ejemplo de uso extenso

```
crear a = 10
crear b = 5
crear c = -8
crear nombre = Juan

curar a b           # Suma: 10 + 5 = 15
golpear a b         # Resta: 10 - 5 = 5
multiplicar a b     # Multiplicación: 10 * 5 = 50
dividir a b         # División: 10 / 5 = 2.0
poder a b           # Potencia: 10^5 = 100000
revivir a           # Raíz cuadrada: sqrt(10) = 3.16...
xp c                # Valor absoluto: abs(-8) = 8
jefe a b c          # Máximo: max(10, 5, -8) = 10
esbirro a b c       # Mínimo: min(10, 5, -8) = -8
decir nombre        # Muestra el valor de la variable 'nombre'
decir a             # Muestra el valor de la variable 'a'
```

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

## Desarrollado por

- Christian Jafeth Peña Espinoza
- Luciana Chacón Castillo