#EMILTON PEREIRA MARQUES NETO         P1 C.C. NOITE
#DALINA DANTAS CATARINA                   2023

logado = False
tipo_usuario = None
idade = 0

dados = {}
noticias = []
id = 0

def criarConta():
    global tipo_usuario
    while True:
        user = input("\nUsuario : ")
        if user in dados:
            print("\nEsse nome de Usuario ja existe.\n")
            continue
        senh = input("Senha : ")
        if len(senh) < 8:
            print('\nSua senha precisa ter no mínimo 8 digitos\n')
            continue
        senh1 = input("Confirme a Senha : ")
        if senh != senh1:
            print("\nSenhas nao Coincidem\n")
            continue
        tipo_usuario = input("\nDigite:\nR para criar uma conta de reporter ou\nL para criar uma conta de leitor : ")
        if tipo_usuario.lower() not in ["l", "r"]:
            print("\nTipo de Usuario Invalido.\n")
            continue

        if tipo_usuario.lower() == "r":
            idade = int(input("\nDigite sua idade : "))
            if idade < 18:
                print("\nPara ser Reporter você precisa ter pelo menos 18 anos.\n")
                main()

        print(f"\nUsuario {'Reporter' if tipo_usuario.lower == 'r' else 'Leitor'} cadastrado com Sucesso!")
        dados[user] = {'senha': senh, 'tipo': tipo_usuario}
        return tipo_usuario

def login():
    tent = 3
    for i in range(0, tent):
        global tipo_usuario
        tent -= 1
        login1 = input("\nUsuario : ")
        senha1 = input("Senha : ")
        if dados.get(login1) and dados.get(login1)['senha'] == senha1:
            print(f"\nBem Vindo ao APP Noticias da Catolica, {login1}!")
            tipo_usuario = dados.get(login1)['tipo']
            if tipo_usuario.lower() == "r":
                if reporterMenu():
                    break
            elif tipo_usuario.lower() == "l":
                if leitorMenu():
                    break
        else:
            print(f"\nUsuario ou Senha Incorretos. Você tem mais {tent} Tentativas.")
    main()

def reporterMenu():
    global id
    while True:
        print("_" * 50)
        print("\nEscolha uma opçao para prosseguir\n")
        print("[1] Criar Noticias")
        print("[2] Editar Noticias")
        print("[3] Remover Noticias")
        print("[4] Ver ID Noticias")
        print("[5] Abrir Noticias")
        print("[0] Deslogar")
        pgreporter = input("\n")
        print("_" * 50)
        if pgreporter == "0":
            main()
            break

        if pgreporter == "1":
            noticiaTitu = input("\nDigite o Titulo : ")
            noticiaDesc = input("Digite a Descricao : ")
            noticiaComp = input("Digite a Noticia : ")

            print('Digite a Data: ')
            data_dia = int(input("Dia: "))
            data_mes = int(input('Mês: '))
            data_ano = int(input('Ano: '))
            while True:
                if (data_dia < 1) or (data_dia > 31) or (data_mes < 1) or (data_mes > 12) or (data_ano < 0):
                    print('\nData Inválida!\n')
                    print('Digite novamente: ')
                    data_dia = int(input("Dia: "))
                    data_mes = int(input('Mês: '))
                    data_ano = int(input('Ano: '))
                else:
                    break

            id += 1
            noticias.append(
                {"ID": id, "Titulo": noticiaTitu, "Descricao": noticiaDesc, "Noticia": noticiaComp, "DataDia": data_dia,
                 "DataMes": data_mes, "DataAno": data_ano, "Comentarios": [], "Curtidas": 0})
            print("\nNoticia Enviada com Sucesso!\n")

        elif pgreporter == "2":
            id_edit = int(input("\nDigite o ID da noticia que deseja editar: "))
            for noticia in noticias:
                if noticia['ID'] == id_edit:
                    noticia['Titulo'] = input("Digite o novo titulo: ")
                    noticia['Descricao'] = input("Digite a nova descricao: ")
                    noticia['Noticia'] = input("Digite a nova noticia: ")
                    print("\nNoticia atualizada com sucesso!\n")
                    break
            else:
                print("\nNoticia não encontrada.\n")

        elif pgreporter == "3":
            id_remove = int(input("\nDigite o ID da noticia que deseja remover: "))
            for noticia in noticias:
                if noticia['ID'] == id_remove:
                    confirm = input("\nTem certeza que deseja remover esta noticia? (s/n): ")
                    if confirm.lower() == 's':
                        noticias.remove(noticia)
                        print("\nNoticia removida com sucesso!\n")
                        break
                    elif confirm.lower() == 'n':
                        print("\nOperação cancelada.\n")
                        break
                else:
                    print("\nNoticia não encontrada.\n")

        elif pgreporter == "4":
            if noticias:
                for noticia in noticias:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")

            else:
                print("\nNenhuma noticia foi criada ainda.\n")

        elif pgreporter == "5":
            id_view = int(input("\nDigite o ID da noticia que deseja ver: "))
            for noticia in noticias:
                if noticia['ID'] == id_view:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']} ")
                    break
            else:
                print("\nNoticia não encontrada.\n")
        else:
            print('\nInformação Inválida! \nResponda com 1, 2, 3, 4, 5 ou 0')

def leitorMenu():
    while True:
        print("_" * 50)
        print("\nEscolha uma opçao para prosseguir:\n")
        print("[1] Buscar notícia")
        print('[2] Comentar notícia')
        print('[3] Curtir notícia')
        print('[4] Ver Noticias por ID')
        print('[0] Deslogar')
        pgleitor = input("\n")
        print("_" * 50)
        if pgleitor == "0":
            main()
            break

        if (pgleitor == '0'):
            print('Programa Finalizado!')
            break

        elif (pgleitor != '1' and pgleitor != '2' and pgleitor != '3' and pgleitor != '0' and pgleitor != '4'):
            print('\nInformação Inválida!')
            print('Responda com 1, 2, 3, 4 ou 0')

        elif (pgleitor == '1'):
            id_view_2 = int(input('\nDigite o ID da notícia que vc quer buscar: '))
            for noticia in noticias:
                if noticia['ID'] == id_view_2:
                    print(
                        f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: "
                        f"{noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']}\nComentários: {noticia['Comentarios']}\nCurtidas: {noticia['Curtidas']} ")
                    break
            else:
                print("\nNoticia não encontrada.")

        elif (pgleitor == '2'):
            busca = int(input('Digite o ID da notícia que você deseja comentar: '))
            for noticia in noticias:
                if noticia['ID'] == busca:
                    print(
                        f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: "
                        f"{noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']} ")
                    comentario = input('\nDigite o comentário que você deseja adicionar: ')
                    noticia['Comentarios'].append(comentario)
                    print('\nSeu comentário foi adicionado a notícia!')
                else:
                    print("\nNoticia não encontrada.")

        elif (pgleitor == '3'):
            curtida = int(input('Digite o ID da notícia que você deseja curtir: '))
            for noticia in noticias:
                if noticia['ID'] == curtida:
                    noticia['Curtidas'] += 1
                    print('\nSua curtida foi contabilizada!')
                else:
                    print('Notícia não encontrada!')
                break

        elif (pgleitor == '4'):
            if noticias:
                for noticia in noticias:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")

            else:
                print("\nNenhuma noticia foi criada ainda.\n")

def main():
    global tipo_usuario
    while True:
        print("_" * 50)
        print("\nBem vindo(a) ao APP de Noticias da Catolica")
        print("Escolha uma opçao para prosseguir\n")
        print("[1] Criar Conta")
        print("[2] Login")
        print("[0] sair")
        pgmenu = input("")
        print("_" * 50)
        if pgmenu == "0":
            exit()
        elif pgmenu == "1":
            tipo_usuario = criarConta()
            if tipo_usuario.lower() == "r":
                if reporterMenu():
                    break
            elif tipo_usuario.lower() == "l":
                if leitorMenu():
                    break
        elif pgmenu == "2":
            if login():
                break
        else:
            print('\nInformação Inválida! \nResponda com 1, 2 ou 0')
main()