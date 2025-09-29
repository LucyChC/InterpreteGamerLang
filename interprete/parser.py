"""
Módulo de análisis sintáctico para el intérprete Gamer.
Valida la estructura de las instrucciones tokenizadas.
"""

from typing import List, Tuple
from interprete.keywords import KEYWORDS

class ParserError(Exception):
    """Excepción personalizada para errores de sintaxis."""
    pass

class Parser:
    """
    Analizador sintáctico simple para el lenguaje Gamer.
    """

    def __init__(self) -> None:
        pass

    def _parse_value(self, value: str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value  # Devuelve la cadena tal cual

    def parse(self, tokens: List[Tuple[str, str]]) -> bool:
        """
        Valida la estructura de una instrucción tokenizada.

        Args:
            tokens: Lista de tuplas (tipo, valor) generadas por el lexer.

        Returns:
            True si la sintaxis es válida.

        Raises:
            ParserError si la sintaxis es inválida.
        """
        if not tokens:
            raise ParserError("No hay tokens para analizar.")

        # crear <identificador> = <numero/decimal>
        if tokens[0][1] == "crear":
            if (len(tokens) == 4 and
                tokens[1][0] == "IDENTIFICADOR" and
                tokens[2][0] == "IGUAL" and
                tokens[3][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR", "CADENA")):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'crear'.")
        # curar <identificador> <identificador>
        if tokens[0][1] == "curar":
            if (len(tokens) == 3 and
                tokens[1][0] == "IDENTIFICADOR" and
                tokens[2][0] == "IDENTIFICADOR"):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'curar'.")
        # golpear <identificador> <identificador>
        if tokens[0][1] == "golpear":
            if (len(tokens) == 3 and
                tokens[1][0] == "IDENTIFICADOR" and
                tokens[2][0] == "IDENTIFICADOR"):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'golpear'.")
        # multiplicar <valor> <valor>
        if tokens[0][1] == "multiplicar":
            if (len(tokens) == 3 and
                tokens[1][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR") and
                tokens[2][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR")):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'multiplicar'.")
        # dividir <identificador> <identificador>
        if tokens[0][1] == "dividir":
            if (len(tokens) == 3 and
                tokens[1][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR") and
                tokens[2][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR")):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'dividir'.")
        # poder <valor> <valor>
        if tokens[0][1] == "poder":
            if (len(tokens) == 3 and
                tokens[1][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR") and
                tokens[2][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR")):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'poder'.")
        # revivir <identificador>
        if tokens[0][1] == "revivir":
            if (len(tokens) == 2 and
                tokens[1][0] == "IDENTIFICADOR"):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'revivir'.")
        # xp <identificador>
        if tokens[0][1] == "xp":
            if (len(tokens) == 2 and
                tokens[1][0] == "IDENTIFICADOR"):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'xp'.")
        # jefe <identificador> <identificador> ...
        if tokens[0][1] == "jefe":
            if (len(tokens) >= 2 and
                all(t[0] == "IDENTIFICADOR" for t in tokens[1:])):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'jefe'.")
        # esbirro <identificador> <identificador> ...
        if tokens[0][1] == "esbirro":
            if (len(tokens) >= 2 and
                all(t[0] == "IDENTIFICADOR" for t in tokens[1:])):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'esbirro'.")
        # decir <identificador>
        if tokens[0][1] == "decir":
            if (len(tokens) == 2 and
                tokens[1][0] == "IDENTIFICADOR"):
                return True
            else:
                raise ParserError("Sintaxis inválida para 'decir'.")

        raise ParserError("Instrucción no reconocida.")

# Ejemplo de uso:
if __name__ == "__main__":
    from lexer import Lexer
    lexer = Lexer()
    parser = Parser()
    instruccion = "crear vida = 100"
    tokens = lexer.tokenize(instruccion)
    try:
        valido = parser.parse(tokens)
        print("Sintaxis válida:", valido)
    except ParserError as e:
        print("Error de sintaxis:", e)

