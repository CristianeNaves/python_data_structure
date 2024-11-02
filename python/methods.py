"""
SPLIT
* A função split() é usada para dividir uma string em partes, com base em um delimitador especificado.
STRIP
* A função strip() remove os espaços em branco do início e do final de uma string.
* Ela não divide a string em partes; apenas remove os espaços desnecessários.
* Também remove outros caracteres, por exemplo str.strip('\n') remove todos os /n do inicio e fim
"""

s = "cristiane naves cardoso ".split()
print(s) # ["cristiane", "naves", "cardoso"]

s = "cristiane naves cardoso ".split(" ")
print(s) # ["cristiane", "naves", "cardoso", ""]

"""
ALL -> The Python all() function returns true if all the elements of a given iterable (List, Dictionary, Tuple, set, etc.) are True.
It also returns True if the iterable object is empty.
"""
print(all([True, False])) # False
print(all([])) # True
print(all(True, 'c')) # True
print(all('c')) # True pq string é iterable
print(all([""])) # False
print(all([0,1,1])) # False

"""
NEXT
Python’s next() function returns the next item of an iterator.
"""
l = [1, 2, 3]
l_iter = iter(l)  
print(next(l_iter)) # 1
print(next(l_iter)) # 2
