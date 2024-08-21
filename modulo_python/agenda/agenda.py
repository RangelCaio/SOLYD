AGENDA = {}

AGENDA['joao'] = {
    'telefone': '99999999',
    'email': 'joao@email.com',
    'endereco': 'rua 2, 435',
}

AGENDA['maria'] = {
    'telefone': '99999555',
    'email': 'maria@email.com',
    'endereco': 'rua 4, 425',
}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>> Agenda vazia <<<')


def buscar_contato(contato):
    try:
        print('----------------------------------------')
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('E-mail:', AGENDA[contato]['email'])
        print('endereco:', AGENDA[contato]['endereco'])
        print()
    except KeyError:
        print('----------------------------------------')
        print(">>> Contato inexistente <<<")
    except Exception as error:
        print('----------------------------------------')
        print(">>> Um erro inesperado ocorreu <<<")
        print(error)

def incluir_editar_contato(contato):
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('----------------------------------------')
    print(">>>> Contato {} foi adicionado/editado com sucesso <<<<".format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print('----------------------------------------')
        print(">>> Contato {} excluido com sucesso <<<".format(contato))
    except KeyError:
        print('----------------------------------------')
        print(">>> Contato inexistente <<<")
    except Exception as error:
        print('----------------------------------------')
        print(">>> Um erro inesperado ocorreu <<<")
        print(error)


def imprimir_menu():
    print('----------------------------------------')
    print('### MENU ####')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('0 - Sair do programa')
    print('----------------------------------------')


while True:
    imprimir_menu()
    opcao = input('Escolha uma opcao: ')
    print('----------------------------------------')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input("Digite o nome do contato: ")
        try:
            AGENDA[contato]
            print('>>>  Contato ja existente:', contato)

        except KeyError:

            incluir_editar_contato(contato)
    elif opcao == '4':
        contato = input("Digite o nome do contato: ")
        try:
            AGENDA[contato]
            print('>>>  Editando contato:', contato)

            incluir_editar_contato(contato)
        except:
            print('Contato >', contato, '< inexistente')


    elif opcao == '5':
        contato = input("Digite o nome do contato que deseja excluir: ")
        excluir_contato(contato)
    elif opcao == '0':
        print("Fechando programa")
        break
    else:
        print("Opcao invalida")