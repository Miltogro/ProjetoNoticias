#EMILTON PEREIRA MARQUES NETO         P1 C.C. NOITE
#DALINA DANTAS CATARINA                   2023

logado = False
tipo_usuario = None
idade = 0

dados = {}
dados['e'] = {'senha': '1', 'tipo': 'r'}  #USUÁRIOS PRÉ-CADASTRADOS PARA TESTES
dados['r'] = {'senha': '1', 'tipo': 'l'}
noticias = []

def criarConta():
    while True:
        while True:
            user = input("\nUsuario : ")
            if user in dados:
                print("\n\033[31mEsse nome de Usuario ja existe.\n\033[m")
            else:
                break

        while True:
            senh = input("Senha : ")
            senh1 = input("Confirme a Senha : ")

            if len(senh) < 8:
                print('\n\033[31mSua senha precisa ter no mínimo 8 digitos\n\033[m')
            elif senh != senh1:
                print("\n\033[31mSenhas nao Coincidem\n\033[m")
            else:
                break
    
        while True:
            log = False
            tipo_usuario = input("\nDigite:\nR para criar uma conta de reporter ou\nL para criar uma conta de leitor : ")
            if tipo_usuario.lower() not in ["l", "r"]:
                print("\n\033[31mTipo de Usuario Invalido.\n\033[m")
            if tipo_usuario.lower() == "r":
                idade = int(input("\nDigite sua idade : "))
                if idade < 18:
                    print("\n\033[31mPara ser Reporter você precisa ter pelo menos 18 anos.\n\033[m")
                    main()
                elif idade >= 18:
                    print(f"\n\033[32mUsuario Repórter cadastrado com Sucesso!\033[m")
                    dados[user] = {'senha': senh, 'tipo': tipo_usuario}
                    log = True
                    break
            elif tipo_usuario.lower() == "l":
                print(f"\n\033[32mUsuario Leitor cadastrado com Sucesso!\033[m")
                dados[user] = {'senha': senh, 'tipo': tipo_usuario}
                log = True
                break
            
        if log:
            break
    return tipo_usuario

def login():
    tent = 4
    for i in range(0, tent):
        
        tent -= 1
        login1 = input("\nUsuario : ")
        senha1 = input("Senha : ")
        if (login1 in dados) and (senha1 in dados[login1]["senha"]):
            print(f"\n\033[32mBem Vindo ao APP Noticias da Catolica, {login1}!\033[m")
            if dados[login1]['tipo'] == "r":
                if reporterMenu():
                    break
            elif dados[login1]['tipo'] == "l":
                if leitorMenu():
                    break
        if tent > 1:
            print(f"\n\033[31mUsuario ou Senha Incorretos. Você tem mais {tent} Tentativas.\033[m")
        elif tent == 1:
            print(f"\n\033[31mUsuario ou Senha Incorretos. Você tem mais {tent} Tentativa.\033[m")
        elif tent == 0:
            print(f"\n\033[31mUsuario ou Senha Incorretos. Você foi desconectado.\033[m")
    main()

def reporterMenu():
    id = 0
    while True:
        print("_" * 50)
        print('''\nEscolha uma opçao para prosseguir:\n
        [1] Criar Noticias
        [2] Editar Noticias
        [3] Remover Noticias
        [4] Ver ID Noticias
        [5] Abrir Noticias
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
                "DataMes": data_mes, "DataAno": data_ano, "Comentarios": [], "Curtidas": 0})
            print("\n\033[32mNoticia Enviada com Sucesso!\n\033[m")

        elif pgReporter == "2":
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

        elif pgReporter == "3":
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

        elif pgReporter == "4":
            if noticias:
                for noticia in noticias:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")

            else:
                print("\n\033[31mNenhuma noticia foi criada ainda.\n\033[m")

        elif pgReporter == "5":
            id_view = int(input("\nDigite o ID da noticia que deseja ver: "))
            for noticia in noticias:
                if noticia['ID'] == id_view:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']} ")
                    print("\nComentários:")
                    print(*noticia['Comentarios'], sep=", ")
                    print(f"\nCurtidas: {noticia['Curtidas']} ")
                    break
            else:
                print("\n\033[31mNoticia não encontrada.\n\033[m")
        else:
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4, 5 ou 0\033[m')

def leitorMenu():
    while True:
        print("_" * 50)
        print('''\nEscolha uma opçao para prosseguir:\n
        [1] Buscar notícia
        [2] Comentar notícia
        [3] Curtir notícia
        [4] Ver Noticias por ID
        [0] Deslogar''')
        pgLeitor = input("\n")
        print("_" * 50)

        if (pgLeitor == '0'):
            print('\033[32mPrograma Finalizado!\033[m')
            break

        elif (pgLeitor == '1'):
            verId2 = int(input('\nDigite o ID da notícia que vc quer buscar: '))
            for noticia in noticias:
                if noticia['ID'] == verId2:
                    print(
                        f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: "
                        f"{noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']}")
                    print('\nComentários: ')
                    print(*noticia['Comentarios'], sep=", ")
                    print(f"\nCurtidas: {noticia['Curtidas']} ")
                    break
            else:
                print("\n\033[31mNoticia não encontrada.\033[m")

        elif (pgLeitor == '2'):
            busca = int(input('Digite o ID da notícia que você deseja comentar: '))
            for noticia in noticias:
                if noticia['ID'] not in busca:
                    print("\n\033[31mDigite um ID Válido.\033[m")
                elif noticia['ID'] == busca:
                    comentario = input('\nDigite o comentário que você deseja adicionar: ')
                    noticia['Comentarios'].append(comentario)
                    print('\n\033[32mSeu comentário foi adicionado a notícia!\033[m')
                else:
                    print("\n\033[31mNoticia não encontrada.\033[m")

        elif (pgLeitor == '3'):
            curtida = int(input('Digite o ID da notícia que você deseja curtir: '))
            for noticia in noticias:
                if noticia['ID'] not in curtida:
                    print("\n\033[31mDigite um ID Válido.\033[m")
                elif noticia['ID'] == curtida:
                    noticia['Curtidas'] += 1
                    print('\n\033[32mSua curtida foi contabilizada!\033[m')
                else:
                    print('\033[31mNotícia não encontrada!\033[m')
                break

        elif (pgLeitor == '4'):
            if noticias:
                for noticia in noticias:
                    print("_" * 50)
                    print(
                        f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")
            else:
                print("\n\033[31menhuma noticia foi criada ainda.\n\033[m")

        else:
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2, 3, 4 ou 0\033[m')
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
            exit()
        elif pgMenu == "1":
            tipo_usuario = criarConta()
            if tipo_usuario.lower() == "r":
                if reporterMenu():
                    break
            elif tipo_usuario.lower() == "l":
                if leitorMenu():
                    break
        elif pgMenu == "2":
            if login():
                break
        else:
            print('\n\033[31mInformação Inválida! \nResponda com 1, 2 ou 0\033[m')
main()