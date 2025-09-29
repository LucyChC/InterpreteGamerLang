from interprete.lexer import Lexer
from interprete.keywords import KEYWORDS

def test_tokenize_crear():
    lexer = Lexer()
    tokens = lexer.tokenize("crear vida = 100")
    assert tokens == [
        ("KEYWORD", "crear"),   # 🔹 antes era IDENTIFICADOR
        ("IDENTIFICADOR", "vida"),
        ("IGUAL", "="),
        ("NUMERO", "100")
    ]

def test_tokenize_curar():
    lexer = Lexer()
    tokens = lexer.tokenize("curar vida pocion")
    assert tokens == [
        ("KEYWORD", "curar"),   # 🔹 corregido
        ("IDENTIFICADOR", "vida"),
        ("IDENTIFICADOR", "pocion")
    ]

def test_tokenize_dividir():
    lexer = Lexer()
    tokens = lexer.tokenize("dividir oro cofres")
    assert tokens == [
        ("KEYWORD", "dividir"),  # 🔹 corregido
        ("IDENTIFICADOR", "oro"),
        ("IDENTIFICADOR", "cofres")
    ]

def test_tokenize_decimal():
    lexer = Lexer()
    tokens = lexer.tokenize("crear mana = 3.14")
    assert tokens == [
        ("KEYWORD", "crear"),  # 🔹 corregido
        ("IDENTIFICADOR", "mana"),
        ("IGUAL", "="),
        ("DECIMAL", "3.14")
    ]

def test_tokenize_desconocido():
    lexer = Lexer()
    tokens = lexer.tokenize("crear vida @ 100")
    assert tokens == [
        ("KEYWORD", "crear"),  # 🔹 corregido
        ("IDENTIFICADOR", "vida"),
        ("DESCONOCIDO", "@"),
        ("NUMERO", "100")
    ]

def test_lexer_case_insensitive_crear():
    lexer = Lexer()
    tokens = lexer.tokenize("CREAR VIDA = 100")
    assert tokens[0] == ("KEYWORD", "crear")   # 🔹 corregido
    assert tokens[1] == ("IDENTIFICADOR", "vida")
    assert tokens[2] == ("IGUAL", "=")
    assert tokens[3] == ("NUMERO", "100")
