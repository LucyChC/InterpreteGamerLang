import pytest
from interprete.lexer import Lexer
from interprete.semantic import SemanticAnalyzer

def test_semantic_crear_variable():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    tokens = lexer.tokenize("crear vida = 100")
    assert semantic.analyze(tokens) is True

def test_semantic_crear_variable_existente():
    analyzer = SemanticAnalyzer()
    tokens = [("IDENTIFICADOR", "crear"), ("IDENTIFICADOR", "x"), ("IGUAL", "="), ("NUMERO", "10")]
    analyzer.analyze(tokens)
    tokens2 = [("IDENTIFICADOR", "crear"), ("IDENTIFICADOR", "x"), ("IGUAL", "="), ("NUMERO", "20")]
    assert analyzer.analyze(tokens2)

def test_semantic_curar_variables_definidas():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    semantic.analyze(lexer.tokenize("crear vida = 100"))
    semantic.analyze(lexer.tokenize("crear pocion = 50"))
    tokens = lexer.tokenize("curar vida pocion")
    assert semantic.analyze(tokens) is True

def test_semantic_curar_variable_no_definida():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    semantic.analyze(lexer.tokenize("crear vida = 100"))
    tokens = lexer.tokenize("curar vida pocion")
    assert semantic.analyze(tokens) is True

def test_semantic_dividir_por_cero():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    semantic.analyze(lexer.tokenize("crear oro = 100"))
    semantic.analyze(lexer.tokenize("crear cofres = 0"))
    tokens = lexer.tokenize("dividir oro cofres")
    assert semantic.analyze(tokens) is True

def test_semantic_revivir_negativo():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    semantic.analyze(lexer.tokenize("crear vida = -4"))
    tokens = lexer.tokenize("revivir vida")
    assert semantic.analyze(tokens) is True

def test_semantic_jefe_variables_definidas():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    semantic.analyze(lexer.tokenize("crear a = 10"))
    semantic.analyze(lexer.tokenize("crear b = 20"))
    tokens = lexer.tokenize("jefe a b")
    assert semantic.analyze(tokens) is True

def test_semantic_jefe_variable_no_definida():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    semantic.analyze(lexer.tokenize("crear a = 10"))
    tokens = lexer.tokenize("jefe a b")
    assert semantic.analyze(tokens) is True

def test_semantic_decir_variable_definida():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    semantic.analyze(lexer.tokenize("crear vida = 100"))
    tokens = lexer.tokenize("decir vida")
    assert semantic.analyze(tokens) is True

def test_semantic_decir_variable_no_definida():
    lexer = Lexer()
    semantic = SemanticAnalyzer()
    tokens = lexer.tokenize("decir mana")
    assert semantic.analyze(tokens) is True
