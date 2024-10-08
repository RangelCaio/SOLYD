AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>> Agenda vazia <<<')


def buscar_contato(contato):
    try:
        print('----------------------------------------------------------------------')
        print()
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('E-mail:', AGENDA[contato]['email'])
        print('endereco:', AGENDA[contato]['endereco'])
        print()
    except KeyError:
        print('----------------------------------------------------------------------')
        print(">>> Contato inexistente <<<")
    except Exception as error:
        print('----------------------------------------------------------------------')
        print(">>> Um erro inesperado ocorreu <<<")
        print(error)


def ler_detalhes_contatos():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereco do contato: ')
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print('----------------------------------------------------------------------')
    print(">>>> Contato {} foi adicionado/editado com sucesso <<<<".format(contato))


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print('----------------------------------------------------------------------')
        print(">>> Contato {} excluido com sucesso <<<".format(contato))
    except KeyError:
        print('----------------------------------------------------------------------')
        print(">>> Contato inexistente <<<")
    except Exception as error:
        print('----------------------------------------------------------------------')
        print(">>> Um erro inesperado ocorreu <<<")
        print(error)


def exportar_contato(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato, telefone, email, endereco))
        print('----------------------------------------------------------------------')
        print('>>> Agenda exportada com sucesso <<<')
    except Exception as error:
        print('>>> Algum erro ocorreu ao exportar contatos <<<')
        print(error)


def importar_contato(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('>>> Arquivo nao encontrado <<<')
    except Exception as error:
        print('>>> Algum erro inesperado ocorreu <<<')
        print(error)


def salvar():
    exportar_contato('database.csv');


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('----------------------------------------------------------------------')
        print('>>> Database carregado com sucesso <<<')
        print('>>> {} contatos carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>> Arquivo nao encontrado <<<')
    except Exception as error:
        print('>>> Algum erro inesperado ocorreu <<<')
        print(error)


def imprimir_menu():
    print('----------------------------------------------------------------------')
    print('### MENU ####')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contato para CSV')
    print('7 - Importar contato CSV')
    print('0 - Fechar agenda')
    print('----------------------------------------------------------------------')

carregar()
while True:
    imprimir_menu()
    opcao = input('Escolha uma opcao: ')
    print('----------------------------------------------------------------------')
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
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input("Digite o nome do contato: ")
        try:
            AGENDA[contato]
            print('>>>  Editando contato:', contato)
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(contato, telefone, email, endereco)
        except:
            print('Contato >', contato, '< inexistente')
    elif opcao == '5':
        contato = input("Digite o nome do contato que deseja excluir: ")
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contato(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contato(nome_do_arquivo)
    elif opcao == '0':
        print("Fechando programa")
        break
    else:
        print("Opcao invalida")