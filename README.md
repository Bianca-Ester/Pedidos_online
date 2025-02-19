# Pedidos_online

- Descrição Geral
Este projeto é uma simulação de pedidos online para uma lanchonete virtual, desenvolvido em Python. Ele utiliza conceitos fundamentais como listas, dicionários, CRUD (Create, Read, Update, Delete), tratamento de erros, estruturas de repetição e funções. O programa é executado no terminal e permite que o usuário cadastre um login, faça pedidos de diferentes itens, visualize seus pedidos e finalize a compra.

- Funcionalidades do Sistema
O sistema é dividido em dois menus principais:

  Menu de Cadastro/Login
  Menu de Pedidos
  
  1. Menu de Cadastro/Login
    Antes de acessar a lanchonete, o usuário precisa cadastrar um login ou utilizar um já existente.
    
    Opções do Menu de Cadastro/Login:
    Cadastrar novo login (Armazena nome de usuário e senha em um dicionário)
    Fazer login (Valida o usuário e senha antes de acessar o menu de pedidos)
    Visualizar logins cadastrados
    Excluir um login cadastrado
    Se o login for bem-sucedido, o sistema limpa o terminal e direciona o usuário ao menu de pedidos.
    
  2. Menu de Pedidos
    Após o login, o usuário pode navegar no menu da lanchonete, onde encontrará cinco categorias de produtos:
    
    Bebidas
    Sanduíches
    Sobremesas
    Meus Pedidos
    Finalizar Pedido (Fecha o programa)
    Cada categoria possui um sub-menu com os produtos disponíveis, exibindo nome, tamanho, preço e uma opção para escolher a quantidade desejada.
    
    O usuário escolhe um item e informa a quantidade desejada.
    
    O terminal é limpo antes de cada exibição, facilitando a navegação.
    
    Para voltar um passo, basta pressionar qualquer tecla.
  
  3. Meus Pedidos
    Aqui o usuário pode visualizar todos os itens adicionados ao pedido, organizados em ordem de compra.
    
    Cada item tem um ID, permitindo ao usuário:
    
    Excluir um pedido
    Atualizar a quantidade de um pedido
    No final, o valor total do pedido é exibido.
    
  4. Finalizar Pedido
    Essa opção encerra o programa, finalizando a compra.
  
- Tecnologias Utilizadas
  Listas para armazenar os pedidos.
  Dicionários para armazenar logins e produtos.
  Tratamento de Erros para evitar entradas inválidas.
  CRUD para manipulação de logins e pedidos.
  Funções para modularizar o código.
  Estruturas de repetição para navegação nos menus.
