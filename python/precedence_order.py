"""
Ordem de precedência
1. Parentêses
2. Expoentes (**) -> se tiver mais de 1 expoente é lido da direita para a esquerda
3. Multiplicação e Divisão (a ordem de precedência é da esquerda para a direita)
4. Adição e subtração (a ordem de precedência é da esquerda para a direita)

Essa ordem de precendência é conhecida como PEMDAS (parentheses, exponents, multiplication and
division, adiction and subtraction)

How python precedence operators work
-----------------------------------------------------
|Category                  | Operators               |
-----------------------------------------------------
|Arithmetic Operators      |  **, *, /, +, -         |
-----------------------------------------------------
|Comparison Operators      |  ==, !=, <=, >=, <, >   |
-----------------------------------------------------
|Logical Operators         |  not, and, or           |
-----------------------------------------------------
|Bitwise Operators 	       |  &, |, ^                |
-----------------------------------------------------
|Assignment Operators      |  =, +=, -=              |
-----------------------------------------------------


The modulo operator ( % ) shares the same level of precedence as the multiplication ( * ), 
division ( / ), and floor division ( // ) operators.

Reference: https://www.upgrad.com/tutorials/software-engineering/python-tutorial/operator-precedence-in-python/
"""

2 ** 2 / 1 
2 ** 3 ** 2 # 2 ** (3 ** 2)


2 ** 2 + 4 ** 2 
# print 20

10 / 2 * 4 # é o mesmo que (10/2) * 4


