"""
Módulo de análisis semántico para el intérprete Gamer.
Verifica el significado lógico de las instrucciones.
"""

from typing import List, Tuple, Dict

class SemanticError(Exception):
    """Excepción personalizada para errores semánticos."""
    pass

class SemanticAnalyzer:
    """
    Analizador semántico para el lenguaje Gamer.
    """

    def __init__(self) -> None:
        # Diccionario de variables definidas y sus valores
        self.variables: Dict[str, str] = {}

    def analyze(self, tokens: List[Tuple[str, str]]) -> bool:
        if not tokens:
            raise SemanticError("No hay tokens para analizar.")

        cmd = tokens[0][1]

        # crear <identificador> = <numero/decimal>
        if cmd == "crear":
            var_name = tokens[1][1]
            if var_name in self.variables:
                raise SemanticError(f"La variable '{var_name}' ya está definida.")
            self.variables[var_name] = tokens[3][1]
            return True

        # curar <identificador> <identificador>
        if cmd == "curar":
            var1 = tokens[1][1]
            var2 = tokens[2][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            if var2 not in self.variables:
                raise SemanticError(f"La variable '{var2}' no está definida.")
            return True

        # golpear <identificador> <identificador>
        if cmd == "golpear":
            var1 = tokens[1][1]
            var2 = tokens[2][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            if var2 not in self.variables:
                raise SemanticError(f"La variable '{var2}' no está definida.")
            return True

        # multiplicar <identificador> <identificador>
        if cmd == "multiplicar":
            var1 = tokens[1][1]
            var2 = tokens[2][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            if var2 not in self.variables:
                raise SemanticError(f"La variable '{var2}' no está definida.")
            return True

        # dividir <identificador> <identificador>
        if cmd == "dividir":
            var1 = tokens[1][1]
            var2 = tokens[2][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            if var2 not in self.variables:
                raise SemanticError(f"La variable '{var2}' no está definida.")
            if self.variables[var2] == "0" or self.variables[var2] == 0:
                raise SemanticError("No se puede dividir por cero.")
            return True

        # poder <identificador> <identificador>
        if cmd == "poder":
            var1 = tokens[1][1]
            var2 = tokens[2][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            if var2 not in self.variables:
                raise SemanticError(f"La variable '{var2}' no está definida.")
            return True

        # revivir <identificador>
        if cmd == "revivir":
            var1 = tokens[1][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            if float(self.variables[var1]) < 0:
                raise SemanticError("No se puede calcular la raíz de un número negativo.")
            return True

        # xp <identificador>
        if cmd == "xp":
            var1 = tokens[1][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            return True

        # jefe <identificador> <identificador> ...
        if cmd == "jefe":
            for t in tokens[1:]:
                var = t[1]
                if var not in self.variables:
                    raise SemanticError(f"La variable '{var}' no está definida.")
            return True

        # esbirro <identificador> <identificador> ...
        if cmd == "esbirro":
            for t in tokens[1:]:
                var = t[1]
                if var not in self.variables:
                    raise SemanticError(f"La variable '{var}' no está definida.")
            return True

        # decir <identificador>
        if cmd == "decir":
            var1 = tokens[1][1]
            if var1 not in self.variables:
                raise SemanticError(f"La variable '{var1}' no está definida.")
            return True

        raise SemanticError("Instrucción no reconocida o semántica inválida.")

# Ejemplo de uso:
if __name__ == "__main__":
    from lexer import Lexer
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    instrucciones = [
        "crear vida = 100",
        "crear pocion = 50",
        "curar vida pocion",
        "golpear vida pocion",
        "multiplicar vida pocion",
        "dividir vida pocion",
        "poder vida pocion",
        "revivir vida",
        "xp vida",
        "jefe vida pocion",
        "esbirro vida pocion",
        "decir vida"
    ]
    for instruccion in instrucciones:
        tokens = lexer.tokenize(instruccion)
        try:
            valido = semantic.analyze(tokens)
            print(f"Semántica válida para '{instruccion}':", valido)
        except SemanticError as e:
            print(f"Error semántico en '{instruccion}':", e)