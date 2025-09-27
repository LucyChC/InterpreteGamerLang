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

        Args:
            instruction: Instrucción en texto.

        Returns:
            Lista de tuplas (tipo, valor).
        """
        tokens = []
        words = instruction.strip().split()
        for word in words:
            if word == "=":
                tokens.append(("IGUAL", word))
            elif word.lstrip('-').isdigit():
                tokens.append(("NUMERO", word))
            elif word.replace('.', '', 1).lstrip('-').isdigit():
                tokens.append(("DECIMAL", word))
            elif word.isidentifier():
                tokens.append(("IDENTIFICADOR", word))
            else:
                # Si no es número ni identificador, lo tratamos como desconocido
                tokens.append(("DESCONOCIDO", word))
        return tokens

# Ejemplo de uso:
if __name__ == "__main__":
    lexer = Lexer()
    instruccion = "crear vida = 100"
    print(lexer.tokenize(instruccion))