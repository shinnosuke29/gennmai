#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
# (c) 2024 Shinnosuke

import sys
import argparse
import statistics

def calculate_stats(numbers, args):
    if args.sum:
        print(f"Sum: {sum(numbers)}")
    if args.avg:
        print(f"Average: {sum(numbers)/len(numbers):.2f}")
    if args.max:
        print(f"Max: {max(numbers)}")
    if args.min:
        print(f"Min: {min(numbers)}")
    if args.median:
        print(f"Median: {statistics.median(numbers)}")
    if args.std:
        print(f"Standard Deviation: {statistics.pstdev(numbers):.2f}")

def main():
    parser = argparse.ArgumentParser(description="Calculate statistics from numbers.")
    parser.add_argument("--sum", action="store_true", help="Calculate the sum of numbers")
    parser.add_argument("--avg", action="store_true", help="Calculate the average of numbers")
    parser.add_argument("--max", action="store_true", help="Find the maximum value")
    parser.add_argument("--min", action="store_true", help="Find the minimum value")
    parser.add_argument("--median", action="store_true", help="Find the median value")
    parser.add_argument("--std", action="store_true", help="Calculate standard deviation")

    args = parser.parse_args()
    input_text = sys.stdin.read().strip()

    if not input_text:
        print("Error: No input provided.", file=sys.stderr)
        sys.exit(1)

    try:
        numbers = [float(num) for num in input_text.split()]
        calculate_stats(numbers, args)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
