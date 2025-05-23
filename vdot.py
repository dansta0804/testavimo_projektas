#!/usr/bin/env python3

import sys, os

INPUT_DIR = "Tests/Inputs/"
OUTPUT_DIR = "Tests/Outputs/Actual/"

def calculate_dot_product(output, vectors: str, filename: str):
    split_vector = vectors.strip().split()
    if len(split_vector) % 2 != 0:
        with open(output, "a") as out_file:
            out_file.write(f"Issue: vector component count is not even!\n\n")
        return None
    else:
        mid = len(split_vector) // 2
        first_part, second_part, mul_results = [], [], []

        for i, val in enumerate(split_vector):
            try:
                val = float(val)
            except ValueError:
                with open(output, "a") as out_file:
                    filename = os.path.basename(filename)
                    out_file.write(f"Value '{val}' does not match numeric"
                                   f" syntax in {filename}!\n\n")
                return None

            if i < mid:
                first_part.append(val)
            else:
                second_part.append(val)

        for a, b in zip(first_part, second_part):
            mul_results.append(a * b)

        with open(output, "a") as out_file:
            out_file.write(f"Result (dot product): {sum(mul_results)}\n\n")
        return sum(mul_results)

def handle_input(output, files):
    if isinstance(files, str):
        files = [files]

    for file in files:
        results = []
        if not os.path.exists(file):
            file = os.path.basename(file)
            print(f"Cannot open '{file}': No such file!")
            with open(output, "a") as out_file:
                out_file.write(f"Cannot open '{file}': No such file!\n")
            continue

        with open(file, 'r') as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()

            if not line or line.startswith('#'):
                continue
            try:
                with open(output, "a") as out_file:
                    out_file.write(str(f"Working with vectors: {line}\n"))
                results.append(calculate_dot_product(output, line, file))
            except ValueError as e:
                sys.stderr.write(str(e) + '\n')

        with open(output, "a") as out_file:
            out_file.write(
                    str(f"# {len([sum for sum in results if sum is not None])} "
                        f"vector pair(-s) was(were) multiplied in total.\n"))

    return ""