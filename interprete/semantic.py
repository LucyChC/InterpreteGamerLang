"""
Módulo de análisis semántico para el intérprete Gamer.
Valida solo la estructura de las instrucciones, no gestiona variables.
"""

from typing import List, Tuple

class SemanticError(Exception):
    """Excepción personalizada para errores semánticos."""
    pass

class SemanticAnalyzer:
    """
    Analizador semántico: valida forma, no existencia de variables.
    """

    def __init__(self) -> None:
        # Ya no guardamos variables en esta versión
        pass

    def analyze(self, tokens: List[Tuple[str, str]]) -> bool:
        if not tokens:
            raise SemanticError("No hay tokens para analizar.")

        cmd = tokens[0][1]

        # crear <identificador> = <valor>
        if cmd == "crear":
            if not (
                len(tokens) == 4
                and tokens[1][0] == "IDENTIFICADOR"
                and tokens[2][0] == "IGUAL"
                and tokens[3][0] in ("NUMERO", "DECIMAL", "IDENTIFICADOR", "CADENA")
            ):
                raise SemanticError("Sintaxis inválida para 'crear'.")
            return True

        # Comandos binarios
        if cmd in ["curar", "golpear", "multiplicar", "dividir", "poder"]:
            if len(tokens) != 3:
                raise SemanticError(f"Sintaxis inválida para '{cmd}'.")
            # solo revisamos tipo de token
            for t in tokens[1:]:
                if t[0] not in ("IDENTIFICADOR", "NUMERO", "DECIMAL"):
                    raise SemanticError(f"Token inesperado: {t}")
            return True

        # Comandos unarios
        if cmd in ["revivir", "xp", "decir"]:
            if len(tokens) != 2 or tokens[1][0] != "IDENTIFICADOR":
                raise SemanticError(f"Sintaxis inválida para '{cmd}'.")
            return True

        # Comandos múltiples
        if cmd in ["jefe", "esbirro"]:
            if len(tokens) < 2:
                raise SemanticError(f"Sintaxis inválida para '{cmd}'.")
            for t in tokens[1:]:
                if t[0] != "IDENTIFICADOR":
                    raise SemanticError(f"Token inesperado: {t}")
            return True

        raise SemanticError(f"Instrucción no reconocida: {cmd}")
