"""
Módulo principal del intérprete Gamer.
Integra análisis léxico, sintáctico y semántico para procesar instrucciones.
"""

from typing import Any, Dict, Union, List, Tuple
import math

from interprete.lexer import Lexer
from interprete.parser import Parser, ParserError
from interprete.semantic import SemanticAnalyzer, SemanticError

KEYWORDS = {
    "crear": "definir_variable",
    "curar": "suma",
    "golpear": "resta",
    "multiplicar": "multiplica",
    "dividir": "divide",
    "poder": "potencia",
    "revivir": "raiz",
    "xp": "abs",
    "jefe": "max",
    "esbirro": "min",
    "decir": "imprimir"
}

class InterpreterError(Exception):
    """Excepción personalizada para errores del intérprete."""
    pass

class Interpreter:
    """
    Clase principal para interpretar instrucciones y gestionar variables.
    Integra lexer, parser y semantic.
    """

    def __init__(self) -> None:
        self.variables: Dict[str, Union[int, float, str]] = {}
        self.lexer = Lexer()
        self.parser = Parser()
        self.semantic = SemanticAnalyzer()

    def eval_instruction(self, instruction: str) -> Any:
        # 1. Análisis léxico
        tokens = self.lexer.tokenize(instruction)

        # 2. Análisis sintáctico
        try:
            self.parser.parse(tokens)
        except ParserError as e:
            raise InterpreterError(f"Error de sintaxis: {e}")

        # 3. Análisis semántico
        try:
            self.semantic.variables = self.variables  # Sincroniza variables
            self.semantic.analyze(tokens)
        except SemanticError as e:
            raise InterpreterError(f"Error semántico: {e}")

        # 4. Ejecución de la instrucción
        cmd = tokens[0][1]
        action = KEYWORDS.get(cmd, None)

        if action == "definir_variable":
            name = tokens[1][1]
            value = self._parse_value(tokens[3][1])
            self.variables[name] = value
            return f"Variable '{name}' definida con valor {value}"

        elif action == "suma":
            a = self.variables[tokens[1][1]]
            b = self.variables[tokens[2][1]]
            self._check_numeric(a, b)
            return f"Resultado: {a + b}"

        elif action == "resta":
            a = self.variables[tokens[1][1]]
            b = self.variables[tokens[2][1]]
            self._check_numeric(a, b)
            return f"Resultado: {a - b}"

        elif action == "multiplica":
            a = self.variables[tokens[1][1]]
            b = self.variables[tokens[2][1]]
            self._check_numeric(a, b)
            return f"Resultado: {a * b}"

        elif action == "divide":
            a = self.variables[tokens[1][1]]
            b = self.variables[tokens[2][1]]
            self._check_numeric(a, b)
            if b == 0:
                raise InterpreterError("No se puede dividir por cero.")
            return f"Resultado: {a / b}"

        elif action == "potencia":
            a = self.variables[tokens[1][1]]
            b = self.variables[tokens[2][1]]
            self._check_numeric(a, b)
            return f"Resultado: {a ** b}"

        elif action == "raiz":
            a = self.variables[tokens[1][1]]
            self._check_numeric(a)
            if a < 0:
                raise InterpreterError("No se puede calcular la raíz de un número negativo.")
            return f"Resultado: {math.sqrt(a)}"

        elif action == "abs":
            a = self.variables[tokens[1][1]]
            self._check_numeric(a)
            return f"Resultado: {abs(a)}"

        elif action == "max":
            values = [self.variables[name[1]] for name in tokens[1:]]
            self._check_numeric(*values)
            return f"Resultado: {max(values)}"

        elif action == "min":
            values = [self.variables[name[1]] for name in tokens[1:]]
            self._check_numeric(*values)
            return f"Resultado: {min(values)}"

        elif action == "imprimir":
            value = self.variables[tokens[1][1]]
            return f"{tokens[1][1]} = {value}"

        else:
            raise InterpreterError("Comando Gamer no reconocido o no implementado.")

    def reset(self) -> None:
        self.variables.clear()

    def _parse_value(self, value: str) -> Union[int, float, str]:
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def _check_numeric(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise InterpreterError("Solo se pueden operar números.")

    def define_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        if name not in self.variables:
            raise InterpreterError(f"La variable '{name}' no está definida.")
        return self.variables[name]