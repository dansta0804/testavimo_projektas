# TEST 8
# Test that calls 'vdot.py' program with one existent data file. The file
# meets the following requirements:
#   - file has odd vector component count (the program dies after detecting
#     lines that have odd value count);
#   - file stores values that follow numeric value syntax.

import os
from pathlib import Path
from vdot import handle_input

IN_NAME = "odd_num.dat"
IN_DIR = "Inputs/"
OUT_ACTUAL = "Outputs/Actual/"
OUT_EXPECTED = "Outputs/Expected/"
OUT_NAME = "Test8.out"

def test_program_outputs():
    base_dir = Path(__file__).resolve().parents[1]
    input_file = os.path.join(base_dir, IN_DIR, IN_NAME)
    expected_result = os.path.join(base_dir, OUT_EXPECTED, OUT_NAME)
    actual_result = os.path.join(base_dir, OUT_ACTUAL, OUT_NAME)

    handle_input(actual_result, input_file)

    with open(actual_result, 'r') as f:
        actual_result = f.read().strip()

    with open(expected_result, 'r') as f:
        expected_result = f.read().strip()

    assert actual_result == expected_result,\
        "Generated output differs from the expected output."