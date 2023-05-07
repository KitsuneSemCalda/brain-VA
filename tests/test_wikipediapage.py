import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from robot.bot import WikipediaSearch

@pytest.mark.parametrize("term, user_input", [
    ("Python", "1"),  # Simula a escolha do primeiro resultado
    ("OpenAI", ""),   # Simula pressionar ENTER (escolha do primeiro resultado)
    ("Artificial intelligence", "invalid"),  # Simula entrada inválida (escolha do primeiro resultado)
])
def test_wikipedia_search(monkeypatch, term, user_input):
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    search = WikipediaSearch(term)
    page = search.search()
    assert page.title is not None
    assert page.url is not None
    assert page.content is not None
