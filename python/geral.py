# Em herança multipla, se um metodo for herdado de duas classes diferentes, 
# será executado o método da classe que foi passada primeiro como parametro

class Pai:
    def falar(self):
        print("Pai falando")

class Mae:
    def falar(self):
        print("Mae falando")

class Filho(Pai, Mae):
    def falar(self):
        super().falar() # retornará "Pai falando"
        
"""
Função EVAL
A função eval() em Python é usada para avaliar uma expressão ou código Python dinamicamente em 
tempo de execução. Ela recebe uma string contendo uma expressão Python e a executa, retornando o resultado.
* Lembre-se de usar a função eval() com cuidado, pois ela pode executar qualquer código 
Python presente na string fornecida. 
"""
expressao = "3 + 5 * 2"
resultado = eval(expressao)
print(f"Resultado da expressão '{expressao}': {resultado}")
