#!/usr/bin/env python3
import argparse
from sympy.parsing.sympy_parser import parse_expr
from sympy import pprint

parser = argparse.ArgumentParser(
        description='Parse and pretty print mathematical formulas to stdout.'
        )
parser.add_argument(
        'expressions',
        metavar='E',
        type=str,
        nargs='+',
        help='an expression to be turned into a string'
        )
parser.add_argument(
        '-u', '--use_unicode',
        dest='use_unicode',
        action='store_const',
        default=False,
        const=True,
        help='use unicode instead of ascii for printing expressions'
        )

args = parser.parse_args()

for expression in args.expressions :
    pprint(parse_expr(expression), use_unicode=args.use_unicode)
