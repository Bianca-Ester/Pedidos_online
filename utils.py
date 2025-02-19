from os import system

def limpar_terminal():
    system('cls')

def apresenta_produtos(lista):
    limpar_terminal()
    for produto in lista:
        print(f"{produto['id']} | {produto['title']} - R$ {produto['price']:.2f}\n")
