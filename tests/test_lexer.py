from interprete.lexer import Lexer

def test_tokenize_crear():
    lexer = Lexer()
    tokens = lexer.tokenize("crear vida = 100")
    assert tokens == [
        ("IDENTIFICADOR", "crear"),
        ("IDENTIFICADOR", "vida"),
        ("IGUAL", "="),
        ("NUMERO", "100")
    ]

def test_tokenize_curar():
    lexer = Lexer()
    tokens = lexer.tokenize("curar vida pocion")
    assert tokens == [
        ("IDENTIFICADOR", "curar"),
        ("IDENTIFICADOR", "vida"),
        ("IDENTIFICADOR", "pocion")
    ]

def test_tokenize_dividir():
    lexer = Lexer()
    tokens = lexer.tokenize("dividir oro cofres")
    assert tokens == [
        ("IDENTIFICADOR", "dividir"),
        ("IDENTIFICADOR", "oro"),
        ("IDENTIFICADOR", "cofres")
    ]

def test_tokenize_decimal():
    lexer = Lexer()
    tokens = lexer.tokenize("crear mana = 3.14")
    assert tokens == [
        ("IDENTIFICADOR", "crear"),
        ("IDENTIFICADOR", "mana"),
        ("IGUAL", "="),
        ("DECIMAL", "3.14")
    ]

def test_tokenize_desconocido():
    lexer = Lexer()
    tokens = lexer.tokenize("crear vida @ 100")
    assert tokens == [
        ("IDENTIFICADOR", "crear"),
        ("IDENTIFICADOR", "vida"),
        ("DESCONOCIDO", "@"),
        ("NUMERO", "100")
    ]