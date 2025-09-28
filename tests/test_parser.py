import pytest
from interprete.lexer import Lexer
from interprete.parser import Parser, ParserError

def test_parse_crear_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("crear vida = 100")
    assert parser.parse(tokens) is True

def test_parse_crear_invalido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("crear vida 100")
    with pytest.raises(ParserError):
        parser.parse(tokens)

def test_parse_curar_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("curar vida pocion")
    assert parser.parse(tokens) is True

def test_parse_curar_invalido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("curar vida")
    with pytest.raises(ParserError):
        parser.parse(tokens)

def test_parse_golpear_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("golpear vida daño")
    assert parser.parse(tokens) is True

def test_parse_multiplicar_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("multiplicar fuerza multiplicador")
    assert parser.parse(tokens) is True

def test_parse_dividir_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("dividir oro cofres")
    assert parser.parse(tokens) is True

def test_parse_poder_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("poder base exponente")
    assert parser.parse(tokens) is True

def test_parse_revivir_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("revivir vida")
    assert parser.parse(tokens) is True

def test_parse_xp_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("xp puntos")
    assert parser.parse(tokens) is True

def test_parse_jefe_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("jefe a b c")
    assert parser.parse(tokens) is True

def test_parse_esbirro_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("esbirro a b c")
    assert parser.parse(tokens) is True

def test_parse_decir_valido():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("decir vida")
    assert parser.parse(tokens) is True

def test_parse_instruccion_no_reconocida():
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("foo bar baz")
    with pytest.raises(ParserError):
        parser.parse(tokens)

def test_parser_multiplicar_valores():
    from interprete.lexer import Lexer
    from interprete.parser import Parser
    lexer = Lexer()
    parser = Parser()
    tokens = lexer.tokenize("multiplicar 2 a")
    assert parser.parse(tokens) is True
