"""
Módulo de análisis léxico para el intérprete Gamer.
Convierte instrucciones en una lista de tokens.
"""

from typing import List, Tuple
from interprete.keywords import KEYWORDS
import re

class Lexer:
    """
    Analizador léxico simple para el lenguaje Gamer.
    """

    def __init__(self) -> None:
        pass

    def tokenize(self, instruction: str) -> List[Tuple[str, str]]:
        """
        Convierte una instrucción en una lista de tokens (tipo, valor).
        """
        tokens = []

        # Regex para separar cadenas entre comillas y palabras/números
        pattern = r'"[^"]*"|\S+'
        words = re.findall(pattern, instruction)

        for word in words:
            # Guardamos el valor original (para cadenas)
            val = word

            # Comparamos en minúsculas para palabras clave
            w = word.lower()

            if w == "=":
                tokens.append(("IGUAL", "="))
            elif re.fullmatch(r'-?\d+', w):
                tokens.append(("NUMERO", w))
            elif re.fullmatch(r'-?\d+\.\d+', w):
                tokens.append(("DECIMAL", w))
            elif w in KEYWORDS:  # 🔹 Reconocer palabra clave
                tokens.append(("KEYWORD", w))
            elif re.fullmatch(r'"[^"]*"', word):  # 🔹 Detectar cadena
                tokens.append(("CADENA", word.strip('"')))
            elif w.isidentifier():
                tokens.append(("IDENTIFICADOR", w))
            else:
                tokens.append(("DESCONOCIDO", w))

        return tokens


# Ejemplo de uso:
if __name__ == "__main__":
    lexer = Lexer()
    instruccion = 'crear nombre = "Juan"'
    print(lexer.tokenize(instruccion))
