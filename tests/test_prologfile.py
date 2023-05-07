import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from robot.bot import PrologFile

@pytest.fixture
def cleanup():
    # Executa antes dos testes
    yield
    # Executa depois dos testes
    files = [file for file in os.listdir() if file.endswith(".pl")]
    for file in files:
        os.remove(file)

def test_prolog_file_creation(cleanup):
    term = "example"
    content = "predicate(a).\npredicate(b).\npredicate(c)."
    file = PrologFile(term, content)
    file.create()

    assert os.path.exists(file.filename)

    with open(file.filename, 'r') as f:
        file_content = f.read()
    
    assert file_content == content
