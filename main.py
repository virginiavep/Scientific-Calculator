#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cjeffcoa
"""

import math


def basic():
    # =============================================================================
    #     +     for a + b
    #     -     for a - b
    #     /     for a / b
    #     *     for a * b
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))

    if op == '+':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b)
    elif op == '-':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
    elif op == '*':
        return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
    elif op == '/':
        if b == 0:
            return 'Error: Cannot be divided by 0'
        else:
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
    else:
        return "Incorrect operator! Please select from the given options!"


def scientific():
    # =============================================================================
    #     ^     for a ^ b
    #     %     for a mod b
    #     r     for the bth root of a (a ^ (1/b))
    #     !     for a factorial
    #     sin   for sin(a) in radians
    #     cos   for cos(a) in radians
    #     tan   for tan(a) in radians
    #     ln    for ln(a) (log base e of a)
    # =============================================================================

    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "^, r, %, !, sin, cos, tan, ln" : ')

    if op in '^r%':
        a = int(input('Please type the first number: '))
        b = int(input('Please type the second number: '))
    elif op in '!sincostanln':
        a = int(input('Please type the number: '))
    # for each of the operations, return the operation and result
    # 1) input a to the power of input b
    if op == '^':
        return str(a) + op + str(b) + ' = ' + str(math.pow(a, b))
    # 2) for roots the input a is to to the power of 1/input b
    elif op == 'r':
        return str(a) + op + str(b) + ' = ' + str(a**(1.0/(b)))
    # 3) remainder of input a / input b
    elif op == '%':
        return str(a) + op + str(b) + ' = ' + str(a % b)
    # 4) factorial of input a (ex. 5! = 5*4*3*2*1 = 120)
    elif op == '!':
        return str(a) + op + ' = ' + str(math.factorial(a))
    # 5) sine of input a
    elif op == 'sin':
        return op + '(' + str(a) + ') = ' + str(math.sin(a))
    # 6) cosine of input a
    elif op == 'cos':
        return op + '(' + str(a) + ') = ' + str(math.cos(a))
    # 7) tangent of input a
    elif op == 'tan':
        return op + '(' + str(a) + ') = ' + str(math.tan(a))
    # 8) ln of input a
    elif op == 'ln':
        return op + '(' + str(a) + ') = ' + str(math.log(a))
    # If the user does not enter one of the operators then display an error message
    else:
        return "Incorrect operator! Please select from the given options!"


def main():  # Wrapper function

    print("""Choose a calculator
    1. Basic Calculator
    2. Scientific Calculator""")
    choice = int(input('Please choose as 1 or 2: '))

    if choice == 1:
        print(basic())
    elif choice == 2:
        print(scientific())
    else:
        print('Invalid choice! Please select between 1 and 2:')


if __name__ == '__main__':
    main()