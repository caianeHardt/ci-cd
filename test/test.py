from src.main import *
import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_create_estudante():
    estudante_test = Estudante(name="Caiane Teste", curso="ADS", ativo=False)
    result = await create_estudante(estudante_test)
    assert estudante_test == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo():
    result = await delete_estudante(-9)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_positivo():
    result = await delete_estudante(6)
    assert result
