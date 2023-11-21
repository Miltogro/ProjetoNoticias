#EMILTON PEREIRA MARQUES NETO         P1 C.C. NOITE         2023

logado = False
tipo_usuario = None
idade = 0
usuario_logado = None
id = 1
dados = {}
dados['e'] = {'senha': '1', 'tipo': 'r', 'nome': 'TesteNome1'}  # USUÁRIOS PRÉ-CADASTRADOS PARA TESTES
dados['r'] = {'senha': '1', 'tipo': 'l', 'nome': 'TesteNome2'}
noticias = []
noticias.append({
   "ID": 0,
   "Titulo": "Descoberta Científica",
   "Descricao": "Novo tratamento inovador...",
   "Noticia": "Em um avanço notável para a pesquisa médica, cientistas de renome apresentaram hoje um tratamento promissor que pode representar uma virada significativa no campo das doenças neurodegenerativas. Este anúncio surge como uma luz de esperança para milhões de pessoas em todo o mundo que sofrem de condições como Alzheimer, Parkinson e Esclerose Múltipla."
   "A pesquisa, liderada por uma equipe internacional de especialistas em neurociência, concentrou-se no desenvolvimento de terapias inovadoras que visam abordar as causas subjacentes dessas doenças debilitantes, em vez de apenas aliviar os sintomas. Os resultados preliminares indicam um notável sucesso no tratamento, oferecendo uma perspectiva encorajadora para o futuro.",
   "DataDia": 20,
   "DataMes": 11,
   "DataAno": 2023,
   "Autor": "a",
   "Comentarios": ["Empolgante notícia! A esperança de avanços no tratamento de doenças neurodegenerativas é uma luz no fim do túnel para milhões de pessoas em todo o mundo.",
                    "A ciência continua a desafiar os limites, oferecendo perspectivas promissoras para um futuro com menos sofrimento. Parabéns aos cientistas por esse progresso inspirador!"],
   "Curtidas": 23
   
})

noticias.append({
   "ID": 1,
   "Titulo": "Titulo blabla",
   "Descricao": "Descricao blabla",
   "Noticia": "Noticia blablablablablablablablablablablabla",
   "DataDia": 21,
   "DataMes": 11,
   "DataAno": 2023,
   "Autor": "e",
   "Comentarios": ['Massa'],
   "Curtidas": 25
   
})

def criarConta():
    while True:
        nome = str(input("\nDigite seu nome : "))
        while True:
            user = input("Usuario : ")
            if user in dados:
                print("\n\033[31mEsse nome de Usuario ja existe.\n\033[m")
            else:
                break

        while True:
            senh = input("Senha : ")
            senh1 = input("Confirme a Senha : ")

            if len(senh) < 4:
                print('\n\033[31mSua senha precisa ter no mínimo 4 digitos\n\033[m')
            elif senh != senh1:
                print("\n\033[31mSenhas nao Coincidem\n\033[m")
            else:
                break

        while True:
            log = False
            tipo_usuario = input(
                "\nDigite:\nR para criar uma conta de reporter ou\nL para criar uma conta de leitor : ")
            if tipo_usuario.lower() not in ["l", "r"]:
                print("\n\033[31mTipo de Usuario Invalido.\n\033[m")
            if tipo_usuario.lower() == "r":
                idade = int(input("\nDigite sua idade : "))
                if idade < 18:
                    print("\n\033[31mPara ser Reporter você precisa ter pelo menos 18 anos.\n\033[m")
                    main()
                elif idade >= 18:
                    print(f"\n\033[32mUsuario Repórter cadastrado com Sucesso!\033[m")
                    dados[user] = {'senha': senh, 'tipo': tipo_usuario, 'nome': nome}
                    log = True
                    break
            elif tipo_usuario.lower() == "l":
                print(f"\n\033[32mUsuario Leitor cadastrado com Sucesso!\033[m")
                dados[user] = {'senha': senh, 'tipo': tipo_usuario, 'nome': nome}
                log = True
                break

        if log:
            break
    return tipo_usuario


def login():
    global usuario_logado
    tent = 4
    for i in range(0, tent):
        tent -= 1
        login1 = input("\nUsuario : ")
        senha1 = input("Senha : ")
        if (login1 in dados) and (senha1 in dados[login1]["senha"]):
            print(f"\n\033[32mBem Vindo ao APP Noticias da Catolica, {dados[login1]['nome']}!\033[m")
            usuario_logado = login1
            if dados[login1]['tipo'] == "r":
                reporterMenu()
                break
            elif dados[login1]['tipo'] == "l":
                leitorMenu()
                break
        if tent > 1:
            print(f"\n\033[31mUsuario ou Senha Incorretos. Você tem mais {tent} Tentativas.\033[m")
        elif tent == 1:
            print(f"\n\033[31mUsuario ou Senha Incorretos. Você tem mais {tent} Tentativa.\033[m")
        elif tent == 0:
            print(f"\n\033[31mUsuario ou Senha Incorretos. Você foi desconectado.\033[m")
    main()


def reporterMenu():
    global id
    while True:
        print("_" * 50)
        print('''\nEscolha uma opçao para prosseguir:\n
        [1] Criar Noticias
        [2] Editar Noticias
        [3] Remover Noticias
        [4] Ver ID Noticias
        [5] Abrir Noticias
        [6] Minhas Noticias Populares
        [7] Baixar Minhas Noticias
        [0] Deslogar''')
        pgReporter = input("\n")
        print("_" * 50)
        if pgReporter == "0":
            main()
            break

        if pgReporter == "1":
            noticiaTitu = input("\nDigite o Titulo : ")
            noticiaDesc = input("Digite a Descricao : ")
            noticiaComp = input("Digite a Noticia : ")

            print('Digite a Data: ')
            while True:
                try:
                    data_dia = int(input('Dia: '))
                    data_mes = int(input('Mês: '))
                    data_ano = int(input('Ano: '))
                except ValueError:
                    print('\033[31mDigite uma Data Válida.\n\033[m')
                    continue

                if (1 <= data_dia <= 31) and (1 <= data_mes <= 12) and (0 < data_ano <= 2023):
                    break
                else:
                    print('\n\033[31mData Inválida!\n\033[m')
                    print('Digite novamente: ')

            id += 1
            noticias.append(
                {"ID": id, "Titulo": noticiaTitu, "Descricao": noticiaDesc, "Noticia": noticiaComp, "DataDia": data_dia,
                "DataMes": data_mes, "DataAno": data_ano, "Comentarios": [], "Curtidas": 0, "Autor": usuario_logado})
            print("\n\033[32mNoticia Enviada com Sucesso!\n\033[m")

        elif pgReporter == "2":
            try:
                id_edit = int(input("\nDigite o ID da noticia que deseja editar: "))
            except ValueError:
                print("\n\033[31mNoticia não encontrada.\n\033[m")
                continue
            for noticia in noticias:
                if noticia['ID'] == id_edit:
                    if noticia['Autor'] != usuario_logado:
                        print("\n\033[31mVocê só pode editar suas próprias notícias.\n\033[m")
                        continue
                    while True:
                        print('Deseja editar a notícia toda? (s/n) ')
                        resposta = input('')
                        if resposta.lower() == 's':
                            noticia['Titulo'] = input("Digite o novo titulo: ")
                            noticia['Descricao'] = input("Digite a nova descricao: ")
                            noticia['Noticia'] = input("Digite a nova noticia: ")
                            while True:
                                try:
                                    noticia['DataDia'] = int(input('Dia: '))
                                    noticia['DataMes'] = int(input('Mês: '))
                                    noticia['DataAno'] = int(input('Ano: '))
                                except ValueError:
                                    print('\033[31mDigite uma Data Válida.\n\033[m')
                                    continue

                                if (1 <= noticia['DataDia'] <= 31) and (1 <= noticia['DataMes'] <= 12) and (0 < noticia['DataAno'] <= 2023):
                                    break
                                else:
                                    print('\n\033[31mData Inválida!\n\033[m')
                                    print('Digite novamente: ')
                            print("\n\033[32mNoticia atualizada com sucesso!\n\033[m")
                            break
                        elif resposta.lower() == 'n':
                            print('\nQual parte da notícia deseja editar?\n'
                                  '[1] - Título\n'
                                  '[2] - Descrição\n'
                                  '[3] - Notícia\n'
                                  '[4] - Data\n')
                            resp_02 = input('')
                            if resp_02 == '1':
                                noticia['Titulo'] = input("Digite o novo titulo: ")
                                print("\n\033[32mNoticia atualizada com sucesso!\n\033[m")
                                break
                            elif resp_02 == '2':
                                noticia['Descricao'] = input("Digite a nova descricao: ")
                                print("\n\033[32mNoticia atualizada com sucesso!\n\033[m")
                                break
                            elif resp_02 == '3':
                                noticia['Noticia'] = input("Digite a nova noticia: ")
                                print("\n\033[32mNoticia atualizada com sucesso!\n\033[m")
                                break
                            elif resp_02 == '4':
                                while True:
                                    try:
                                        noticia['DataDia'] = int(input('Dia: '))
                                        noticia['DataMes'] = int(input('Mês: '))
                                        noticia['DataAno'] = int(input('Ano: '))
                                    except ValueError:
                                        print('\033[31mDigite uma Data Válida.\n\033[m')
                                        continue

                                    if (1 <= noticia['DataDia'] <= 31) and (1 <= noticia['DataMes'] <= 12) and (0 < noticia['DataAno'] <= 2023):
                                        break
                                    else:
                                        print('\n\033[31mData Inválida!\n\033[m')
                                        print('Digite novamente: ')
                                print("\n\033[32mNoticia atualizada com sucesso!\n\033[m")
                                break
                        else:
                            print('\n\033[31mResposta Inválida!\n\033[m')
                #else:
                #    print("\n\033[31mNoticia não encontrada.\n\033[m")

        elif pgReporter == "3":
            try:
                id_remove = int(input("\nDigite o ID da noticia que deseja remover: "))
            except ValueError:
                print("\n\033[31mNoticia não encontrada.\n\033[m")
                continue
            for noticia in noticias:
                if noticia['ID'] == id_remove:
                    if noticia['Autor'] != usuario_logado:
                        print("\n\033[31mVocê só pode remover suas próprias notícias.\n\033[m")
                        continue
                    confirm = input("\nTem certeza que deseja remover esta noticia? (s/n): ")
                    if confirm.lower() == 's':
                        noticias.remove(noticia)
                        print("\n\033[32mNoticia removida com sucesso!\n\033[m")
                        break
                    elif confirm.lower() == 'n':
                        print("\n\033[31mOperação cancelada.\n\033[m")
                        break
                #else:
                #    print("\n\033[31mNoticia não encontrada.\n\033[m")

        elif pgReporter == "4":
            if noticias:
                for noticia in noticias:
                     if noticia['Autor'] == usuario_logado:
                        print("_" * 50)
                        print(f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")

            else:
                print("\n\033[31mNenhuma noticia foi criada ainda.\n\033[m")

        elif pgReporter == "5":
            try:
                id_view = int(input("\nDigite o ID da noticia que deseja ver: "))
            except ValueError:
                print("\n\033[31mNoticia não encontrada.\n\033[m")
                continue
            for noticia in noticias:
                if noticia['ID'] == id_view:
                    if noticia['Autor'] != usuario_logado:
                        print("\n\033[31mVocê só pode ver suas próprias notícias.\n\033[m")
                        continue
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']} ")
                    print("\nComentários:")
                    print(*noticia["Comentarios"], sep="\n")
                    print(f"\nCurtidas: {noticia['Curtidas']} ")
                    break
            else:
                print("\n\033[31mNoticia não encontrada.\n\033[m")

        elif pgReporter == "6":
            minhas_noticias = [noticia for noticia in noticias if noticia['Autor'] == usuario_logado]
            lista_noticias = [(noticia['ID'], noticia['Curtidas']) for noticia in minhas_noticias]
            n = len(lista_noticias)

            for i in range(n):
                for j in range(0, n-i-1):
                    if lista_noticias[j][1] < lista_noticias[j+1][1]:
                        aux = lista_noticias[j]
                        lista_noticias[j] = lista_noticias[j + 1]
                        lista_noticias[j + 1] = aux

            for id, curtidas in lista_noticias:
                for noticia in minhas_noticias:
                    if noticia['ID'] == id:
                        print("_" * 100)
                        print(
                            f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}   Curtidas: {noticia['Curtidas']}")

        elif pgReporter == "7":
            minhas_noticias = [noticia for noticia in noticias if noticia['Autor'] == usuario_logado]
            with open(f'{usuario_logado}_noticias.txt', 'w') as arquivo:
                for noticia in minhas_noticias:
                    arquivo.write(f"ID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nNoticia: {noticia['Noticia']}\nData: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nComentários: {noticia['Comentarios']}\nCurtidas: {noticia['Curtidas']}\n\n")
            print("\n\033[32mNotícias baixadas com sucesso!\n\033[m")

        else:
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4, 5, 6, 7 ou 0\033[m')


def leitorMenu():
    while True:
        print("_" * 50)
        print('''\nEscolha uma opçao para prosseguir:\n
        [1] Buscar notícia
        [2] Comentar notícia
        [3] Curtir notícia
        [4] Ver Noticias por ID
        [5] Notícias Populares
        [0] Deslogar''')
        pgLeitor = input("\n")
        print("_" * 50)

        if (pgLeitor == '0'):
            #main()
            break

        elif (pgLeitor == '1'):
            print("Digite\n"
                  "1 Para procurar por ID\n"
                  "2 Para procurar por Assunto\n")
            pgL1 = str(input(""))
            if pgL1 == "1":
                try:
                    verId2 = int(input('\nDigite o ID da notícia que vc quer buscar: '))
                except ValueError:
                    print("\n\033[31mID não encontrado.\033[m")
                    continue
                for noticia in noticias:
                    if noticia['ID'] == verId2:
                        print(
                            f"\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: "
                            f"{noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']}")
                        print('\nComentários: ')
                        print(*noticia['Comentarios'], sep=", ")
                        print(f"\nCurtidas: {noticia['Curtidas']} ")
                        break
                else:
                    print("\n\033[31mNoticia não encontrada.\033[m")
                

            elif pgL1 == "2":
                try:
                    verId3 = str(input('\nDigite o Assunto que vc quer buscar: '))
                    print("_" * 50)
                except ValueError:
                    print("\n\033[31mAssunto não encontrado.\033[m")
                    continue
                for noticia in noticias:
                    if verId3 in noticia['Noticia']:
                        print(
                            f"\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: "
                            f"{noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']}")
                        print('\nComentários: ')
                        print(*noticia['Comentarios'], sep="\n")
                        print(f"\nCurtidas: {noticia['Curtidas']} ")
                        print("_" * 50)
                    else:
                        None
            else:
                print("\n\033[31mOpcao Invalida.\033[m")

        elif (pgLeitor == '2'):
            comentario = False
            try:
                busca = int(input('Digite o ID da notícia que você deseja comentar: '))
            except ValueError:
                print("\n\033[31mID não encontrado.\033[m")
                continue
            for noticia in noticias:
                if noticia['ID'] == busca:
                    comentario = str(input('\nDigite o comentário que você deseja adicionar: '))
                    noticia['Comentarios'].append(comentario)
                    print('\n\033[32mSeu comentário foi adicionado a notícia!\033[m')
                    comentario = True
                    break
            if not comentario:
                print("\n\033[31mNotícia não encontrada.\n\033[m")

        elif pgLeitor == "3":
            try:
                id_curtida = int(input("\nDigite o ID da notícia que você deseja curtir: "))
            except ValueError:
                print("\n\033[31mNotícia não encontrada.\n\033[m")
                continue
            noticia_encontrada = False
            for noticia in noticias:
                if noticia['ID'] == id_curtida:
                    noticia['Curtidas'] += 1
                    print("\n\033[32mNotícia curtida com sucesso!\n\033[m")
                    noticia_encontrada = True
                    continue
            if not noticia_encontrada:
                print("\n\033[31mNotícia não encontrada.\n\033[m")
                continue
            else:
                continue

        elif (pgLeitor == '4'):
            if noticias:
                for noticia in noticias:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")
            else:
                print("\n\033[31menhuma noticia foi criada ainda.\n\033[m")

        elif pgLeitor == "5":
            lista_noticias = [(noticia['ID'], noticia['Curtidas']) for noticia in noticias]
            n = len(lista_noticias)
            for i in range(n):
                for j in range(0, n-i-1):
                    if lista_noticias[j][1] < lista_noticias[j+1][1]:
                        aux = lista_noticias[j]
                        lista_noticias[j] = lista_noticias[j + 1]
                        lista_noticias[j + 1] = aux

            for id, curtidas in lista_noticias:
                for noticia in noticias:
                    if noticia['ID'] == id:
                        print("_" * 100)
                        print(
                            f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}   Curtidas: {noticia['Curtidas']}")

        else:
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4, 5 ou 0\033[m')


def main():
    global tipo_usuario
    while True:
        print("_" * 50)
        print('''\nBem vindo(a) ao APP de Noticias da Catolica
        Escolha uma opçao para prosseguir\n
        [1] Criar Conta
        [2] Login
        [0] sair''')
        pgMenu = input("")
        print("_" * 50)
        if pgMenu == "0":
            usuario_logado = None
            exit()
        elif pgMenu == "1":
            criarConta()
            '''if tipo_usuario.lower() == "r":
                if reporterMenu():
                    break
            elif tipo_usuario.lower() == "l":
                if leitorMenu():
                    break'''
        elif pgMenu == "2":
            if login():
                break
        else:
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2 ou 0\033[m')


main() 