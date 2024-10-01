from src.main import *

def test_root():
    assert root() == {"message": "Hello World"}


def test_create_estudante():
    estudante_test = Estudante(name="Caiane Teste", curso="ADS", ativo=False)
    assert estudante_test == create_estudante(estudante_test)


def test_update_estudante_negativo():
    assert not update_estudante(-5)

def test_update_estudante_positivo():
    assert update_estudante(7)

def test_delete_estudante_negativo():
    assert not update_estudante(-8)

def test_delete_estudante_positivo():
    assert update_estudante(8)
