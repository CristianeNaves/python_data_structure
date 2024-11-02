# https://pythonacademy.com.br/blog/list-comprehensions-no-python
"""
Segue a seguinte sintaxe:
[expr for item in lista] -> o valor expr será salvo na nova lista.
"""

result = []
for num in range(1, 11):
    result.append(num ** 2)
print(result) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

result = [num ** 2 for num in range(1,11)]  
print(result) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

phrase = "Python é incrível"
[word[0] for word in phrase.split(" ")] # pega a primeira letra de cada palavra ["P", "é", "i"]

"""
Também é possível usar estruturas condicionais usando a seguinte estrutura:
[expr for intem in lista if conditional]  -> posso testar o item na condicional para salvar só o necessário
"""
result = [item for item in range(1, 21) if item % 2 == 0]
print(result) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

"""
If + else seguem a seguinte estrutura:
[expressão_se_verdadeiro if condição else expressão_se_falso for item in iterable]
"""
even_odd_strings = ["par" if x % 2 == 0 else "ímpar" for x in range(1, 11)]
print(even_odd_strings)  # Output: ['ímpar', 'par', 'ímpar', 'par', 'ímpar', 'par', 'ímpar', 'par', 'ímpar', 'par']

"""
Nested list comprehension
Regra geral, computa da esquerda para a direita.

https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
"""
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd_numbers = [val for row in numbers for val in row if val % 2 != 0]
print(odd_numbers) # [1, 3, 5, 7, 9]

matrix = [[j for j in range(0, 5)] for i in range(0, 5)]
print(matrix) # [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]