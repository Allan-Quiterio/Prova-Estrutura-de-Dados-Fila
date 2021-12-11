from fila import Queue
import os

fila = Queue()
print('-='*30)
print('        Bem vindo ao restaurante Caminho das Indias')
print('-='*30)
print('Olá atendente, vamos lá! Digite o número da mesa: ')
opcao = int(input('Mesa: '))
fila.push(opcao)
print('Mesa registrada com sucesso!')

while True:
    print('\nE agora o que você quer fazer?')
    print('[1] Adicionar mais uma mesa\n[2] Fazer a entrega do pedido')
    print('[3] Qual o próximo pedido que irá sair\n[4] Listar todos os pedidos\n[5] Sair')
    resp = int(input('Opção: '))
    os.system("cls")
        
    if resp < 1 or resp > 5:
        print('Opção não encontrada, por favor digite uma opção válida')
    
    if resp == 5:
        break
    
    elif resp == 1:
        mesa = int(input('Digite o número da mesa: '))
        fila.push(mesa)
        print('Mesa registrada com sucesso!')
    
    elif resp == 2:
        if len(fila) == 0:
            print('Não há pedidos na lista')
        else:
            pedidoEntregue = fila.pop()
            print(f'O pedido da mesa {pedidoEntregue} foi entregue com sucesso!')
    
    elif resp == 3:
        if len(fila) == 0:
            print('Não há pedidos na lista')
        else:
            print(f'O próximo pedido sairá para a mesa {fila.peek()}')
    
    elif resp == 4:
        print('Lista de pedidos: ')
        print(fila)
print('<<<Fechando o sistema, até mais!>>>')
