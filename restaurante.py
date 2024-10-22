import os #para limpar o terminal

lista_de_restaurantes = [{'nome':'Café Mania', 'categoria':'Café', 'situacao':False}, {'nome':'Piano-Bar', 'categoria':'Bar', 'situacao':True}, {'nome':'Steampunk Bar', 'categoria':'Bar temático', 'situacao':True}]

def exibir_nome():
    print('==== 𝙎𝙖𝙗𝙤𝙧 𝙀𝙭𝙥𝙧𝙚𝙨𝙨 ====\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Encerrar\n')

def sair_app():
    exibir_subtitulo('Saindo do app...')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Informe o nome do restaurante: ') #vai ser salva como string
    categoria = input(f'Informe o nome da categoria do restaurante {nome_restaurante}: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'situacao':False} #False pq todo restaurante começa inativo na plataformaa
    lista_de_restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
    voltar_menu()


def listar_restaurante():
    exibir_subtitulo('Restaurantes cadastrados')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Situação'}\n')


    for restaurante in lista_de_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        situacao = 'Ativado' if restaurante['situacao'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {situacao}') #ljust para deixar o tamanho de tudo igual
    voltar_menu()

def alterar_estado_restaurante():
    exibir_subtitulo('Alterar estado do restaurante')
    nome_restaurante = input('Informe o nome do restaurante que você deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in lista_de_restaurantes:
        if (nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            restaurante['situacao'] = not restaurante['situacao']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['situacao'] else f'O restaurante {nome_restaurante} foi desativado com sucesso.' #ternário
            print(mensagem)


    if (not restaurante_encontrado):
        print('O restaurante não foi encontrado.')
    voltar_menu()


def escolher_opcao():
    try:
        opcao = int(input('==== Escolha uma opção: '))
        #snake case: opcao_escolhida
        print(f'Você escolheu a opção {opcao}') 

        if (opcao == 1):
            cadastrar_restaurante()
        elif (opcao == 2):
            listar_restaurante()
        elif (opcao == 3):
            alterar_estado_restaurante()
        elif (opcao == 4):
            os.system('cls')
            sair_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()