from utils import limpar_terminal
from sys import exit
from time import sleep

from lista_pedidos import pedidos

from bebidas import menu_bebidas
from sanduiches import menu_sanduiches
from sobremesas import menu_sobremesas

from pedidos import meus_pedidos

def menu_inicial():
    controlador = True

    while controlador:
        limpar_terminal()
        print("========================================")
        print("|      SEJA BEM-VINDO A LANCHONETE     |")
        print("========================================")

        print("\n================ OPÇÕES ================\n")
        print("1) Bebidas")
        print("2) Sanduíches")
        print("3) Sobremesas")

        if len(pedidos) > 0:
            print("4) Meus pedidos")
            print("5) Finalizar pedido")

        print("\n========================================")
        print("|PARA SAIR, DIGITE QUALQUER OUTRA TECLA|")
        print("========================================")

        op = input("Digite uma opção: ")

        if op == "1":
            limpar_terminal()
            menu_bebidas()
        
        elif op == "2":
            limpar_terminal()
            menu_sanduiches()
        
        elif op == "3":
            limpar_terminal()
            menu_sobremesas()

        elif op == "4":
            if len(pedidos) > 0:
                limpar_terminal()
                meus_pedidos()
            else:
                print("Agradeço a visita! Volte sempre")
                controlador = False
        
        elif op == "5":
            if len(pedidos) > 0:
                sleep(1)
            print("Agradeço a visita! Volte sempre")
            controlador = False

        else:
            print("Agradeço a visita! Volte sempre")
            controlador = False

""" Feito por Bianca Ester, Maria Helen, Guilherme Antônio e Mikaelly Batista """
