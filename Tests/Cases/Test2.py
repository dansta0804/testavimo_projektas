# TEST 2
# Test that calls 'vdot.py' program with several valid data files. The
# files meet the following requirements:
#     - files have even vector component counts;
#     - files store values that follow numeric value syntax.

import os
from pathlib import Path
from vdot import handle_input

IN_NAME1 = "even_num_ncom_neln1.dat"
IN_NAME2 = "even_num_ncom_neln2.dat"
IN_DIR = "Inputs/"
OUT_ACTUAL = "Outputs/Actual/"
OUT_EXPECTED = "Outputs/Expected/"
OUT_NAME = "Test2.out"

def test_program_outputs():
    base_dir = Path(__file__).resolve().parents[1]
    input_file1 = os.path.join(base_dir, IN_DIR, IN_NAME1)
    input_file2 = os.path.join(base_dir, IN_DIR, IN_NAME2)
    expected_result = os.path.join(base_dir, OUT_EXPECTED, OUT_NAME)
    actual_result = os.path.join(base_dir, OUT_ACTUAL, OUT_NAME)

    handle_input(actual_result, [input_file1, input_file2])

    with open(actual_result, 'r') as f:
        actual_result = f.read().strip()

    with open(expected_result, 'r') as f:
        expected_result = f.read().strip()

    assert actual_result == expected_result,\
        "Generated output differs from the expected output."