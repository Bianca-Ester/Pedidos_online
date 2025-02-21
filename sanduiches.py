from utils import apresenta_produtos
from utils import limpar_terminal

from lista_sanduiches import hamburguers
from lista_sanduiches import naturais

from lista_pedidos import pedidos

def menu_sanduiches():

    controlador_fluxo_bebidas = True
    while controlador_fluxo_bebidas:
        limpar_terminal()
        print("================ OPÇÕES ================\n")
        print("1) Hambúrguers")
        print("2) Sanduíches naturais")
        
        print("\n===========================================")
        print("|PARA VOLTAR , DIGITE QUALQUER OUTRA TECLA|")
        print("===========================================")

        try:
            op = int(input("Digite uma opção: "))

            lista = []

            if op == 1:
                lista = hamburguers
            elif op == 2:
                lista = naturais
            else:
                controlador_fluxo_bebidas = False

            controlador_fluxo_listagem_produtos = True
            while controlador_fluxo_listagem_produtos:
                limpar_terminal()
                apresenta_produtos(lista)
            
                try:
                    print("\n========================================")
                    print("|PARA SAIR, DIGITE QUALQUER OUTRA TECLA|")
                    print("========================================\n")

                    id = int(input("Escolha um produto: "))
                
                    if id <= len(lista) and id > 0:
                        und = int(input("Quantidade: "))
                        pedidos.append(
                            {
                                "id": lista[id - 1]['id'],
                                "title": lista[id - 1]['title'],
                                "description": lista[id - 1]['description'],
                                "price": lista[id - 1]['price'],
                                "quantity": und
                            }
                        )
                        input(f"Produto {lista[id - 1]['title']} adicionado.")

                    elif id == 0:
                        controlador_fluxo_listagem_produtos = False                  
                
                except ValueError:
                    controlador_fluxo_listagem_produtos = False  

        except ValueError:
            controlador_fluxo_bebidas = False  

""" Feito por Bianca Ester, Maria Helen, Guilherme Antônio e Mikaelly Batista """