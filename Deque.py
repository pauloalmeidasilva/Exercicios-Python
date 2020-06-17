#-------------------------------------------------------------------------------
#Deque.py
#Classe para a criação e manipulação de Estruturas de Deque
#-------------------------------------------------------------------------------

##Classe Fila
class Deck(object):
    """Classe para a criação e manipulação de Deques."""

    #Construtor
    def __init__(self, TAMANHO):
        self.vetor = []
        self.tamanho = TAMANHO

    ##Métodos para gerenciamento da pilha

    #Métodos de verificação
    def isEmpty(self):
        """Método que verifica se o deque está vazio."""
        if len(self.vetor) <= 0:
            return True
        else:
            return False

    def isFull(self):
        """Método que verifica se o deque está cheio."""
        if len(self.vetor) > self.tamanho:
            return True
        else:
            return False

    #Métodos para empilhar e Desempilhar
    def addFront(self, ITEM):
        """Método que adiciona um item no deque."""
        if not self.isFull():
            self.vetor.insert(0, ITEM)

    def addRear(self, ITEM):
        """Método que adiciona um item no deque."""
        if not self.isFull():
            self.vetor.append(ITEM)

    def removeFront(self):
        """Método que retira um item no deque.
           Caso este método não seja atribuido a uma variável, ele será descartado."""
        if not self.isEmpty():
            return self.vetor.pop(0)

    def removeRear(self):
        """Método que retira um item no deque.
           Caso este método não seja atribuido a uma variável, ele será descartado."""
        if not self.isEmpty():
            return self.vetor.pop()

    #Métodos que retornam valores
    def peekFront(self):
        """Método que retorna o primeiro valor do deque sem perdê-lo."""
        if not self.isEmpty():
            return self.vetor[0]

    def peekRear(self):
        """Método que retorna o último valor do deque sem perdê-lo."""
        if not self.isEmpty():
            return self.vetor[-1]

    def size(self):
        """Método que retorna quantidade de valores do deque."""
        return len(self.vetor)
