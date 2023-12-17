# list[start:end:step] -> end is not inclusive

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
########## 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#########-10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# [3, 4, 5, 6, 7]
print(my_list[-7:-2])

# [1,2,3,4,5,6,7]
print(my_list[1:-2])

# [1,2,3,4,5,6,7,8,9]
print(my_list[1:])

# [0,1,2,3,4,5,6,7,8,9]
print(my_list[:])

# [] -> não tem como fazer esse caminho,pois tenta iterar pela esquerda do 2 até o -1 (2 - 1 - 0 ...)
print(my_list[2:-1:-1])

# [2,4,6,8]
print(my_list[2:-1:2])

# [9,8,7,6,5,4,3]
# quando usa o numero negativo começo a iterar em ordem reversa, direita para a esquerda
print(my_list[-1:2:-1])

# [9,8,7,6,5,4,3,2,1,0]
print(my_list[::-1])