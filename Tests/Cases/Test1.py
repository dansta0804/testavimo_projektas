# TEST 1
# Test that calls 'vdot.py' program with one valid data file. The file
# meets the following requirements:
#   - file has even vector component count;
#   - file stores values that follow numeric value syntax.

import os
from pathlib import Path
from vdot import handle_input

IN_NAME = "even_num_ncom_neln1.dat"
IN_DIR = "Inputs/"
OUT_ACTUAL = "Outputs/Actual/"
OUT_EXPECTED = "Outputs/Expected/"
OUT_NAME = "Test1.out"

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