# listas são mutáveis

## How to add elements to a Python List
### APPEND: podemos adicionar elementos, um por vez, no final da lista, usando o método append.
num = []
num.append(5)
num.append(2)
# [5, 2]

### EXTEND: podemos adicionar listas (ou outro iterável) ao invés de adicionar 1 por 1 usando o extend. Também adiciona no final.
num.extend([42, 30]) # [5, 2, 42, 30]

### Também é possível concatenar duas listas. Obs.: não pode concatenar 'list' e 'int' e o resultado da operação é uma nova lista.
num + [7] # [5, 2, 42, 30, 7]
print(num) # [5, 2, 42, 30]

### Multiplicar uma lista com um inteiro
[42, 7] * 2 # [42, 7, 42, 7]

### INSERT: podemos adicionar um item em uma posição específica usando o insert (index, item).
num.insert(0, 10) # [10, 5, 2, 42, 30]

## Remoção de elementos
### 1. del: a opção 'del' remove um item da lista com base na posição indicada
del num[0] # [5, 2, 42, 30]

### 2. remove: a opção 'remove' remove um item pelo valor
num.remove(30) # [5, 2, 42]

### 3. pop: remove o último item e retorna esse valor. é possível passar um index.
num.pop() # retorna 42, num = [5, 2]

### 4. clear: remove all items from list
num.clear() # []





"""
References
- https://www.freecodecamp.org/news/lists-in-python-comprehensive-guide/
"""