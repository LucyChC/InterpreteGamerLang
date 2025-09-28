import pytest
from interprete.interpreter import Interpreter, InterpreterError

def test_define_and_get_variable():
    interp = Interpreter()
    interp.define_variable("x", 10)
    assert interp.get_variable("x") == 10

def test_eval_instruction_define_int():
    interp = Interpreter()
    result = interp.eval_instruction("crear x = 5")
    assert result == "Variable 'x' definida con valor 5"
    assert interp.get_variable("x") == 5

def test_eval_instruction_define_float():
    interp = Interpreter()
    result = interp.eval_instruction("crear y = 3.14")
    assert result == "Variable 'y' definida con valor 3.14"
    assert interp.get_variable("y") == 3.14

def test_eval_instruction_define_str():
    interp = Interpreter()
    result = interp.eval_instruction("crear nombre = Juan")
    assert result == "Variable 'nombre' definida con valor Juan"
    assert interp.get_variable("nombre") == "Juan"

def test_eval_instruction_mostrar():
    interp = Interpreter()
    interp.define_variable("x", 42)
    result = interp.eval_instruction("decir x")
    assert result == "x = 42"

def test_eval_instruction_empty():
    interp = Interpreter()
    with pytest.raises(InterpreterError):
        interp.eval_instruction("")

def test_eval_instruction_invalid():
    interp = Interpreter()
    with pytest.raises(InterpreterError):
        interp.eval_instruction("foo bar baz")

def test_get_variable_not_defined():
    interp = Interpreter()
    with pytest.raises(InterpreterError):
        interp.get_variable("noexiste")

def test_reset():
    interp = Interpreter()
    interp.define_variable("x", 1)
    interp.reset()
    assert interp.variables == {}

def test_crear_variable():
    interp = Interpreter()
    result = interp.eval_instruction("crear vida = 100")
    assert result == "Variable 'vida' definida con valor 100"
    assert interp.variables["vida"] == 100

def test_crear_variable_existente():
    interp = Interpreter()
    interp.eval_instruction("crear vida = 100")
    with pytest.raises(InterpreterError):
        interp.eval_instruction("crear vida = 200")

def test_curar():
    interp = Interpreter()
    interp.eval_instruction("crear vida = 100")
    interp.eval_instruction("crear pocion = 50")
    result = interp.eval_instruction("curar vida pocion")
    assert result == "Resultado: 150"

def test_golpear():
    interp = Interpreter()
    interp.eval_instruction("crear vida = 100")
    interp.eval_instruction("crear daño = 30")
    result = interp.eval_instruction("golpear vida daño")
    assert result == "Resultado: 70"

def test_multiplicar():
    interp = Interpreter()
    interp.eval_instruction("crear fuerza = 10")
    interp.eval_instruction("crear multiplicador = 3")
    result = interp.eval_instruction("multiplicar fuerza multiplicador")
    assert result == "Resultado: 30"

def test_dividir():
    interp = Interpreter()
    interp.eval_instruction("crear oro = 100")
    interp.eval_instruction("crear cofres = 4")
    result = interp.eval_instruction("dividir oro cofres")
    assert result == "Resultado: 25.0"

def test_dividir_por_cero():
    interp = Interpreter()
    interp.eval_instruction("crear oro = 100")
    interp.eval_instruction("crear cofres = 0")
    with pytest.raises(InterpreterError):
        interp.eval_instruction("dividir oro cofres")

def test_poder():
    interp = Interpreter()
    interp.eval_instruction("crear base = 2")
    interp.eval_instruction("crear exponente = 3")
    result = interp.eval_instruction("poder base exponente")
    assert result == "Resultado: 8"

def test_revivir():
    interp = Interpreter()
    interp.eval_instruction("crear vida = 16")
    result = interp.eval_instruction("revivir vida")
    assert result == f"Resultado: {16 ** 0.5}"

def test_revivir_negativo():
    interp = Interpreter()
    interp.eval_instruction("crear vida = -4")
    with pytest.raises(InterpreterError):
        interp.eval_instruction("revivir vida")

def test_xp():
    interp = Interpreter()
    interp.eval_instruction("crear puntos = -50")
    result = interp.eval_instruction("xp puntos")
    assert result == "Resultado: 50"

def test_jefe():
    interp = Interpreter()
    interp.eval_instruction("crear a = 10")
    interp.eval_instruction("crear b = 20")
    interp.eval_instruction("crear c = 5")
    result = interp.eval_instruction("jefe a b c")
    assert result == "Resultado: 20"

def test_esbirro():
    interp = Interpreter()
    interp.eval_instruction("crear a = 10")
    interp.eval_instruction("crear b = 20")
    interp.eval_instruction("crear c = 5")
    result = interp.eval_instruction("esbirro a b c")
    assert result == "Resultado: 5"

def test_decir():
    interp = Interpreter()
    interp.eval_instruction("crear vida = 100")
    result = interp.eval_instruction("decir vida")
    assert result == "vida = 100"

def test_variable_no_definida():
    interp = Interpreter()
    with pytest.raises(InterpreterError):
        interp.eval_instruction("decir mana")

def test_instruccion_no_reconocida():
    interp = Interpreter()
    with pytest.raises(InterpreterError):
        interp.eval_instruction("foo bar baz")

def test_multiplicar_numero_numero():
    from interprete.interpreter import Interpreter
    interp = Interpreter()
    result = interp.eval_instruction("multiplicar 4 5")
    assert result == "Resultado: 20"

def test_multiplicar_numero_variable():
    from interprete.interpreter import Interpreter
    interp = Interpreter()
    interp.eval_instruction("crear a = 10")
    result = interp.eval_instruction("multiplicar 4 a")
    assert result == "Resultado: 40"

def test_multiplicar_variable_numero():
    from interprete.interpreter import Interpreter
    interp = Interpreter()
    interp.eval_instruction("crear a = 10")
    result = interp.eval_instruction("multiplicar a 4")
    assert result == "Resultado: 40"

def test_poder_numero_numero():
    from interprete.interpreter import Interpreter
    interp = Interpreter()
    result = interp.eval_instruction("poder 2 3")
    assert result == "Resultado: 8"

def test_poder_variable_numero():
    from interprete.interpreter import Interpreter
    interp = Interpreter()
    interp.eval_instruction("crear a = 10")
    result = interp.eval_instruction("poder a 2")
    assert result == "Resultado: 100"

def test_poder_numero_variable():
    from interprete.interpreter import Interpreter
    interp = Interpreter()
    interp.eval_instruction("crear b = 3")
    result = interp.eval_instruction("poder 2 b")
    assert result == "Resultado: 8"

