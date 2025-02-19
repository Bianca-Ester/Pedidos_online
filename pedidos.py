from utils import limpar_terminal
from time import sleep

from lista_pedidos import pedidos

def meus_pedidos():
    limpar_terminal()
    print("Meus pedidos:")

    cont = 0

    if len(pedidos) > 0:
        for pedido in pedidos:
            cont += 1
            pedido["cont"] = cont
            print(f"{cont} | {pedido['quantity']}x {pedido['title']} R$ {pedido['price']}")

        print(f"\nTotal: R$ {sum([pedido['price'] * pedido['quantity'] for pedido in pedidos]):.2f}\n\n")


        print("1) Excluir um pedido")
        print("2) Atualizar um pedido")

        print("========================================")
        print("|PARA SAIR, DIGITE QUALQUER OUTRA TECLA|")
        print("========================================")

        try:
            op = int(input(""))

            if op == 1:
                id = int(input("Digite o ID do pedido: "))
                remover_pedido(id)
            elif op == 2:
                id = int(input("Digite o ID do pedido: "))
                atualizar_pedido(id)
                
            else:
                 print("Opção inválida.")
        except ValueError:
            return
        
        meus_pedidos()

    else:
        print("Nenhum pedido encontrado.");


def atualizar_pedido(id):
    for i, pedido in enumerate(pedidos):
        if pedido['cont'] == id:
            pedido['quantity'] = int(input("Digite a nova quantidade: "))
            break

def remover_pedido(id):
    for i, pedido in enumerate(pedidos):
        if pedido['cont'] == id:
            del pedidos[i]
            break

""" Feito por Bianca Ester, Maria Helen, Guilherme Antônio e Mikaelly Batista """
