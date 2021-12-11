from node import Node

class Queue:
    def __init__(self):
        
        """Criando o primeiro e último elemento do nó"""
        self.first = None
        self.last = None

        """Contador da fila"""
        self._count = 0
    
    def push(self, elem):
        newNode = Node(elem)

        """Checando se o último elemento está vazio"""
        if self.last is None:
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        
        """Checando o primeiro elemento"""
        if self.first is None:
            self.first = newNode
        
        """Atualizando o tamanho da fila"""
        self._count += 1
    
    def pop(self):
        """Removendo o nó do topo"""
        if self._count > 0:
            elem = self.first.data
            self.first = self.first.next
            
            """Atualizando o tamanho da fila"""
            self._count -= 1
            return elem
        else:
            IndexError('A fila está vazia')

    """Retorna o topo sem remover"""
    def peek(self):
        if self._count > 0:
            elem = self.first.data
            return elem
        raise IndexError("A fila está vazia")

    """Mostrando o tamanho da fila"""
    def __len__(self):
        return self._count
    
    """Representando o objeto"""
    def __repr__(self):
        if self._count > 0:
            repr = ""
            pointer = self.first
            while(pointer):
                repr = repr + str(pointer.data) + " | "
                pointer = pointer.next
            return repr
        return "Fila Vazia"