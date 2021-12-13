"""Criando o nó de cada elemento da fila"""
class Node:
    
    """Criando o método construtor"""
    def __init__(self, data):
        
        """valores"""
        self.data = data

        """Próximo elemento"""
        self.next = None
