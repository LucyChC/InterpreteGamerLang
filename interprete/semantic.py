"""
Módulo de análisis semántico para el intérprete Gamer.
Verifica el significado lógico de las instrucciones.
"""

from typing import List, Tuple, Dict
from interprete.keywords import KEYWORDS

class SemanticError(Exception):
    """Excepción personalizada para errores semánticos."""
    pass

class SemanticAnalyzer:
    """
    Analizador semántico para el lenguaje Gamer.
    """

    def __init__(self) -> None:
        # Diccionario de variables definidas y sus valores
        self.variables: Dict[str, object] = {}  # 🔹 object para poder guardar int, float, str

    """Helper para verificar si un token es una variable definida o un número válido."""
    def _check_var_or_number(self, token):
        tipo, valor = token
        if tipo == "NUMERO":
            return True
        if tipo == "DECIMAL":
            return True
        if tipo == "IDENTIFICADOR":
            if valor not in self.variables:
                raise SemanticError(f"La variable '{valor}' no está definida.")
            return True
        if tipo == "CADENA":
            return True
        raise SemanticError(f"Token inesperado: {valor}")

    def analyze(self, tokens: List[Tuple[str, str]]) -> bool:
        if not tokens:
            raise SemanticError("No hay tokens para analizar.")

        cmd = tokens[0][1]

        # crear <identificador> = <numero/decimal/cadena>
        if cmd == "crear":
            var_name = tokens[1][1]
            if var_name in self.variables:
                raise SemanticError(f"La variable '{var_name}' ya está definida.")
            self._check_var_or_number(tokens[3])
            # Guardar valor convertido a int/float/str según tipo
            tipo, valor = tokens[3]
            if tipo == "NUMERO":
                self.variables[var_name] = int(valor)
            elif tipo == "DECIMAL":
                self.variables[var_name] = float(valor)
            else:
                self.variables[var_name] = valor  # IDENTIFICADOR o CADENA
            return True

        # Para todos los comandos que usan variables existentes
        cmds_2vars = ["curar", "golpear", "multiplicar", "dividir", "poder"]
        if cmd in cmds_2vars:
            self._check_var_or_number(tokens[1])
            self._check_var_or_number(tokens[2])
            return True

        cmds_1var = ["revivir", "xp", "decir"]
        if cmd in cmds_1var:
            var1 = tokens[1][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            return True

        cmds_multi = ["jefe", "esbirro"]
        if cmd in cmds_multi:
            for t in tokens[1:]:
                var = t[1]
                if var not in self.variables:
                    raise SemanticError(f"La variable '{var}' no está definida.")
            return True

        raise SemanticError("Instrucción no reconocida o semántica inválida.")


# Ejemplo de uso:
if __name__ == "__main__":
    from lexer import Lexer
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    instrucciones = [
        'crear vida = 100',
        'crear nombre = "Juan"',
        'curar vida nombre',  # ejemplo ficticio
        'golpear vida nombre',
        'multiplicar vida nombre',
        'dividir vida nombre',
        'poder vida nombre',
        'revivir vida',
        'xp vida',
        'jefe vida nombre',
        'esbirro vida nombre',
        'decir vida'
    ]
    for instruccion in instrucciones:
        tokens = lexer.tokenize(instruccion)
        try:
            valido = semantic.analyze(tokens)
            print(f"Semántica válida para '{instruccion}':", valido)
        except SemanticError as e:
            print(f"Error semántico en '{instruccion}':", e)
