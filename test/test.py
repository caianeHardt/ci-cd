from src.main import *

def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}


def test_create_estudante():
    estudante_test = Estudante(name="Caiane Teste", curso="ADS", ativo=False)
    result = create_estudante(estudante_test)
    yield result
    assert estudante_test == result


def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result

def test_update_estudante_positivo():
    result = update_estudante(10)
    yield result
    assert result

def test_delete_estudante_negativo():
    result = delete_estudante(-9)
    yield result
    assert result

def test_delete_estudante_positivo():
    result = delete_estudante(6)
    yield result
    assert result
