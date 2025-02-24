from time import sleep
from main import menu_inicial
from utils import limpar_terminal

usuarios = []

def login():
    print("-"*15)
    usuario = str(input("Usuário: "))
    senha = str(input("Senha: "))

    for user in usuarios:
        if user['usuario'] == usuario and user['senha'] == senha:
            print("Login efetuado com sucesso!")
            sleep(1)
            limpar_terminal()
            menu_inicial()
            return (user["id"], user["usuario"])

    print("Usuário ou senha inválidos!")
    print()
    print("Deseja voltar ao menu inicial?")
    print("-"*38)
    print("| SE SIM, digite 'sim'                |\n| SE NÃO, digite qualquer outra tecla |")
    print("-"*38)
    voltar = str(input("")).strip()[0]
    if voltar in "Ss":
        limpar_terminal()
        menu()
    else:
        return False

def cadastro():
    print("-"*15)
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "" or senha == "":
        print("Usuário e senha não podem ser vazios!")
        cadastro()

    usuarios.append(
        {
            "id": len(usuarios) + 1,
            "usuario": usuario,
            "senha": senha,
            "produtos": []
        }
    )

    print("-"*15)
    print("Usuário cadastrado com sucesso!")
    sleep(1.5)

def listar_usuarios():
    print("Usuarios cadastrados:")
    print()
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
        return
    
    print("ID | Usuário | Senha")
    for user in usuarios:
        print(f"ID: {user['id']}, Usuário: {user['usuario']}, Senha: {user['senha']}")

def excluir_usuario():
    print("Excluir Usuário")
    try:
        id = int(input("ID do usuário: "))
    except ValueError:
        print("ID inválido!")
        return

    for user in usuarios:
        if user['id'] == id:
            usuarios.remove(user)
            print("Usuário excluído com sucesso!")
            return

    print("Usuário não encontrado.")

def menu():
    print("="*20)
    print("1 - Login")
    print("2 - Cadastro")
    print("3 - Listar Usuários")
    print("4 - Excluir Usuário")
    print("="*20)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        login()
    elif opcao == 2:
        cadastro()
        limpar_terminal()
        menu()
    elif opcao == 3:
        limpar_terminal()
        listar_usuarios()
        sleep(3)
        limpar_terminal() 
        menu()
    elif opcao == 4:
        limpar_terminal()
        listar_usuarios()
        print()
        excluir_usuario()
        limpar_terminal()
        menu()
    else:
        print("Opção inválida!")
        limpar_terminal()
        menu()

menu()

""" Feito por Bianca Ester, Maria Helen, Guilherme Antônio e Mikaelly Batista """
