import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from robot.bot import sanitize

@pytest.mark.parametrize("input_content, expected_output", [
    ("<p>Hello, <b>World</b>!</p>", "Hello, World!"),
    ("<h1>Title</h1>", "Title"),
    ("Plain text", "Plain text"),
])
def test_sanitize(input_content, expected_output):
    assert sanitize(input_content) == expected_output
