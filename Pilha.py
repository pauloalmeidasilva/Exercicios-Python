#-------------------------------------------------------------------------------
#Pilha.py
#Classe para a criação e manipulação de Estruturas de Pilha
#-------------------------------------------------------------------------------

##Classe Pilha
class Stack(object):
    """Classe para a criação e manipulação de Pilhas."""

    #Construtor
    def __init__(self, TAMANHO):
        self.vetor = []
        self.tamanho = TAMANHO
        
##Métodos para gerenciamento da pilha

    #Métodos de verificação
    def isEmpty(self):
        """Método que verifica se a pilha está vazia."""
        if len(self.vetor) <= 0:
            return True
        else:
            return False

    def isFull(self):
        """Método que verifica se a pilha está cheia."""
        if len(self.vetor) >= self.tamanho:
            return True 
        else:
            return False

    #Métodos para empilhar e Desempilhar
    def push(self, ITEM):
        """Método que adiciona um item na pilha."""
        if not self.isFull():
            self.vetor.append(ITEM)

    def pop(self):
        """Método que retira um item na pilha.
           Caso este método não seja atribuido a uma variável, ele será descartado."""
        if not self.isEmpty():
            return self.vetor.pop()

    #Métodos que retornam valores
    def peek(self):
        """Método que retorna o último valor da pilha sem perdê-lo."""
        if not self.isEmpty():
            return self.vetor[-1]

    def size(self):
        """Método que retorna quantidade de valores da pilha."""
        return len(self.vetor)

    def show(self):
        """Método que retorna todos os valores da pilha."""
        print(self.vetor)
