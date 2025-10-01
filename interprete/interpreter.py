"""
Módulo principal del intérprete Gamer.
Integra análisis léxico, sintáctico y semántico para procesar instrucciones.
"""

from typing import Any, Dict, Union, List, Tuple
import math

from interprete.lexer import Lexer
from interprete.parser import Parser, ParserError
from interprete.semantic import SemanticAnalyzer, SemanticError
from interprete.keywords import KEYWORD_ACTIONS

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
        action = KEYWORD_ACTIONS.get(cmd, None)

        if action == "definir_variable":
            name = tokens[1][1]
            rhs_tipo, rhs_val = tokens[3]
            # Resolver el valor según el tipo del token RHS.
            if rhs_tipo == "NUMERO":
                value = int(rhs_val)
            elif rhs_tipo == "DECIMAL":
                value = float(rhs_val)
            elif rhs_tipo == "CADENA":
                value = rhs_val
            elif rhs_tipo == "IDENTIFICADOR":
                # Si existe la variable referenciada, copiar su valor.
                if rhs_val in self.variables:
                    value = self.variables[rhs_val]
                else:
                    # Si no existe, lo tomamos como literal string (ej: crear nombre = Juan)
                    value = rhs_val
            else:
                # Caso raro: permitirlo por compatibilidad
                value = rhs_val

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
            a = self._resolve_value(tokens[1])
            b = self._resolve_value(tokens[2])
            self._check_numeric(a, b)
            return f"Resultado: {a * b}"

        elif action == "divide":
            a = self._resolve_value(tokens[1])
            b = self._resolve_value(tokens[2])
            self._check_numeric(a, b)
            if b == 0:
                raise InterpreterError("No se puede dividir por cero.")
            return f"Resultado: {a / b}"

        elif action == "potencia":
            a = self._resolve_value(tokens[1])
            b = self._resolve_value(tokens[2])
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
            varname = tokens[1][1]
            if varname not in self.variables:
                raise InterpreterError(f"La variable '{varname}' no está definida.")
            value = self.variables[varname]
            return f"{varname} = {value}"


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
    
    def _resolve_value(self, token: Tuple[str, str]):
        tipo, valor = token
        if tipo in ("NUMERO", "DECIMAL"):
            return self._parse_value(valor)
        elif tipo == "IDENTIFICADOR":
            return self.get_variable(valor)
        else:
            raise InterpreterError(f"Valor no válido: {valor}")

