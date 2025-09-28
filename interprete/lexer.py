"""
Módulo de análisis léxico para el intérprete Gamer.
Convierte instrucciones en una lista de tokens.
"""

from typing import List, Tuple

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
        # Pasamos todo a minúsculas para que CREAR = crear
        words = instruction.strip().split()
        for word in words:
            w = word.lower()
            if w == "=":
                tokens.append(("IGUAL", "="))
            elif w.lstrip('-').isdigit():
                tokens.append(("NUMERO", w))
            elif w.replace('.', '', 1).lstrip('-').isdigit():
                tokens.append(("DECIMAL", w))
            elif w.isidentifier():
                tokens.append(("IDENTIFICADOR", w))
            else:
                tokens.append(("DESCONOCIDO", w))
        return tokens


# Ejemplo de uso:
if __name__ == "__main__":
    lexer = Lexer()
    instruccion = "crear vida = 100"
    print(lexer.tokenize(instruccion))

