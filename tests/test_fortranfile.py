import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from robot.bot import FortranFile

@pytest.fixture
def cleanup():
    yield
    files = [file for file in os.listdir() if file.endswith(".f")]
    for file in files:
        os.remove(file)

def test_fortran_file_creation(cleanup):
    term = "example"
    content = "program example\n  print *, 'Hello, World!'\nend program example"
    file = FortranFile(term, content)
    file.create()

    assert os.path.exists(file.filename)

    with open(file.filename, 'r') as f:
        file_content = f.read()
    
    assert file_content == content
