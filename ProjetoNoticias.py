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
            print("\n\033[31mEsse nome de Usuario ja existe.\n\033[m")
            continue
        senh = input("Senha : ")
        if len(senh) < 8:
            print('\n\033[31mSua senha precisa ter no mínimo 8 digitos\n\033[m')
            continue
        senh1 = input("Confirme a Senha : ")
        if senh != senh1:
            print("\n\033[31mSenhas nao Coincidem\n\033[m")
            continue
        tipo_usuario = input("\nDigite:\nR para criar uma conta de reporter ou\nL para criar uma conta de leitor : ")
        if tipo_usuario.lower() not in ["l", "r"]:
            print("\n\033[31mTipo de Usuario Invalido.\n\033[m")
            continue

        if tipo_usuario.lower() == "r":
            idade = int(input("\nDigite sua idade : "))
            if idade < 18:
                print("\n\033[31mPara ser Reporter você precisa ter pelo menos 18 anos.\n\033[m")
                main()

        print(f"\n\033[32mUsuario {'Reporter' if tipo_usuario.lower == 'r' else 'Leitor'} cadastrado com Sucesso!\033[m")
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
            print(f"\n\033[32mBem Vindo ao APP Noticias da Catolica, {login1}!\033[m")
            tipo_usuario = dados.get(login1)['tipo']
            if tipo_usuario.lower() == "r":
                if reporterMenu():
                    break
            elif tipo_usuario.lower() == "l":
                if leitorMenu():
                    break
        if tent > 0 and tent > 1:
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
                    print('\n\033[31mData Inválida!\n\033[m')
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
            print("\n\033[32mNoticia Enviada com Sucesso!\n\033[m")

        elif pgreporter == "2":
            id_edit = int(input("\nDigite o ID da noticia que deseja editar: "))
            for noticia in noticias:
                if noticia['ID'] == id_edit:
                    noticia['Titulo'] = input("Digite o novo titulo: ")
                    noticia['Descricao'] = input("Digite a nova descricao: ")
                    noticia['Noticia'] = input("Digite a nova noticia: ")
                    print("\n\033[32mNoticia atualizada com sucesso!\n\033[m")
                    break
            else:
                print("\n\033[31mNoticia não encontrada.\n\033[m")

        elif pgreporter == "3":
            id_remove = int(input("\nDigite o ID da noticia que deseja remover: "))
            for noticia in noticias:
                if noticia['ID'] == id_remove:
                    confirm = input("\nTem certeza que deseja remover esta noticia? (s/n): ")
                    if confirm.lower() == 's':
                        noticias.remove(noticia)
                        print("\n\033[32mNoticia removida com sucesso!\n\033[m")
                        break
                    elif confirm.lower() == 'n':
                        print("\n\033[31mOperação cancelada.\n\033[m")
                        break
                else:
                    print("\n\033[31mNoticia não encontrada.\n\033[m")

        elif pgreporter == "4":
            if noticias:
                for noticia in noticias:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")

            else:
                print("\n\033[31mNenhuma noticia foi criada ainda.\n\033[m")

        elif pgreporter == "5":
            id_view = int(input("\nDigite o ID da noticia que deseja ver: "))
            for noticia in noticias:
                if noticia['ID'] == id_view:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']} ")
                    break
            else:
                print("\n\033[31mNoticia não encontrada.\n\033[m")
        else:
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4, 5 ou 0\033[m')

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
            print('\033[32mPrograma Finalizado!\033[m')
            break

        elif (pgleitor != '1' and pgleitor != '2' and pgleitor != '3' and pgleitor != '0' and pgleitor != '4'):
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4, 5 ou 0\033[m')

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
                    print('\n\033[32mSeu comentário foi adicionado a notícia!\033[m')
                else:
                    print("\n\033[31mNoticia não encontrada.\033[m")

        elif (pgleitor == '3'):
            curtida = int(input('Digite o ID da notícia que você deseja curtir: '))
            for noticia in noticias:
                if noticia['ID'] == curtida:
                    noticia['Curtidas'] += 1
                    print('\n\033[32mSua curtida foi contabilizada!\033[m')
                else:
                    print('\033[31mNotícia não encontrada!\033[m')
                break

        elif (pgleitor == '4'):
            if noticias:
                for noticia in noticias:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")

            else:
                print("\n\033[31menhuma noticia foi criada ainda.\n\033[m")

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
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2 ou 0\033[m')
main()