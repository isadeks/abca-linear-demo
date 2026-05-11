#!/usr/bin/env python3
"""
generate.py — 10-million-line JavaScript code generator.

Generates a file containing exactly 10,000,000 lines of valid JavaScript:
  - 1,000 modules, each containing 1,000 exported functions
  - Each function is 10 lines (signature + 8 body lines + closing brace)
  - Total: 1,000 × 1,000 × 10 = 10,000,000 lines

Usage:
    python3 generate.py [output_file]

Default output: generated_10m.js
"""

import sys
import time

TARGET_LINES = 10_000_000
NUM_MODULES = 1_000
FUNCS_PER_MODULE = 1_000
LINES_PER_FUNC = 10  # 1 signature + 8 body + 1 closing brace

assert NUM_MODULES * FUNCS_PER_MODULE * LINES_PER_FUNC == TARGET_LINES, \
    "Parameters must multiply to exactly 10,000,000"

output_file = sys.argv[1] if len(sys.argv) > 1 else "generated_10m.js"

print(f"Generating {TARGET_LINES:,} lines → {output_file}")
start = time.time()

with open(output_file, "w", buffering=1 << 20) as f:
    line_count = 0
    for module_idx in range(NUM_MODULES):
        for func_idx in range(FUNCS_PER_MODULE):
            fname = f"module{module_idx:04d}_fn{func_idx:04d}"
            # Line 1: function signature
            f.write(f"export function {fname}(a, b, c) {{\n")
            line_count += 1
            # Lines 2–9: body (8 lines)
            f.write(f"  // Module {module_idx}, function {func_idx}\n")
            f.write(f"  const id = {module_idx * FUNCS_PER_MODULE + func_idx};\n")
            f.write(f"  const sum = a + b + c;\n")
            f.write(f"  const product = a * b * c;\n")
            f.write(f"  const label = `{fname}:${{id}}`;\n")
            f.write(f"  if (sum === 0) {{ return {{ id, label, value: product }}; }}\n")
            f.write(f"  const ratio = product / sum;\n")
            f.write(f"  return {{ id, label, value: ratio }};\n")
            line_count += 8
            # Line 10: closing brace
            f.write("}\n")
            line_count += 1

elapsed = time.time() - start
print(f"Done. Lines written: {line_count:,}  ({elapsed:.1f}s)")
assert line_count == TARGET_LINES, f"Expected {TARGET_LINES}, got {line_count}"
print("✓ Line count verified: exactly 10,000,000 lines.")
