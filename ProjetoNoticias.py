#EMILTON PEREIRA MARQUES NETO         P1 C.C. NOITE
#DALINA DANTAS CATARINA

logado = False
tipo_usuario = None
idade = 0

dados = {}
noticias = []
id = 0

while True:
    print("_" * 50)
    print("\nBem vindo(a) ao APP de Noticias da Catolica")
    print("Escolha uma opçao para prosseguir\n")
    print("[1] Criar Conta")
    print("[2] Login")
    print("[0] Sair")
    pg1 = input("\n")
    print("_" * 50)

    if pg1 == "0":
        break

    elif(pg1 != "1") and (pg1 != "2") and (pg1 != "0"):
        
        print("_" * 50)
        print('\nInformação Inválida!')
        print('Responda com 1, 2 ou 0')
        print("_" * 50)

    elif pg1 == "1":
        user = input("Usuario : ")
        if user in dados:
            print("Esse nome de Usuario ja existe.")
            continue
        demenor = False
        reporteron = False
        leitoron = False
        while True:
            if demenor:
                break
            if reporteron or leitoron:
                break
            senh = input("Senha : ")
            if(len(senh) < 8):
                print('Sua senha precisa ter no mínimo 8 digitos')
            elif(len(senh) >= 8):
                senh1 = input("Confirme a Senha : ")
                if senh == senh1:
                    print("_" * 50)
                    tipo_usuario = input("\nDigite:\n'reporter' para criar uma conta de reporter ou\n'leitor' para criar uma conta de leitor : ")
                    while True:
                        if tipo_usuario.lower() not in ["leitor", "reporter"]:
                            print("\nTipo de Usuario Invalido.\n")
                            tipo_usuario = input("\nDigite:\n'reporter' para criar uma conta de reporter ou\n'leitor' para criar uma conta de leitor : ")
                        elif tipo_usuario.lower() in ["leitor", "reporter"]:
                            if tipo_usuario.lower() == "reporter":
                                idade = int(input("Digite sua idade : "))
                                if idade < 18:
                                    print("\nPara ser Reporter você precisa ter pelo menos 18 anos.")
                                    demenor = True
                                    break
                                elif idade >= 18:
                                    print(f"\nUsuario {tipo_usuario} cadastrado com Sucesso!")
                                    dados[user] = senh
                                    reporteron = True
                                    break
                            elif tipo_usuario.lower() == "leitor":
                                print(f"\nUsuario {tipo_usuario} cadastrado com Sucesso!")
                                dados[user] = senh
                                leitoron = True
                                break
                elif senh != senh1:
                    print("\nSenhas nao Coincidem\n")

    elif pg1 == "2":
        while True:
            login1 = input("\nUsuario : ")
            senha1 = input("Senha : ")
            if dados.get(login1) == senha1:
                print("_" * 50)
                print(f"\nBem Vindo ao APP Noticias da Catolica, {login1}!")
                logado = True
                break
            else:
                print("\nUsuario ou Senha Incorretos.")
    if logado:
        break

if tipo_usuario == "reporter":
    while True:
        print("_" * 50)
        print("\nEscolha uma opçao para prosseguir\n")
        print("[1] Criar Noticias")
        print("[2] Editar Noticias")
        print("[3] Remover Noticias")
        print("[4] Ver ID Noticias")
        print("[5] Abrir Noticias")
        print("[0] Deslogar")
        pg2 = input("\n")
        print("_" * 50)

        if pg2 == "1":
            noticiaTitu = input("\nDigite o Titulo : ")
            noticiaDesc = input("Digite a Descricao : ")
            noticiaComp = input("Digite a Noticia : ")

            print('Digite a Data: ')
            data_dia = int(input("Dia: "))
            data_mes = int(input('Mês: '))
            data_ano = int(input('Ano: '))
            while True:
                if (data_dia < 1) or (data_dia > 31) or (data_mes < 1) or (data_mes > 12) or (data_ano < 0):
                    print('\nData Inválida!')
                    print('Digite novamente: ')
                    data_dia = int(input("Dia: "))
                    data_mes = int(input('Mês: '))
                    data_ano = int(input('Ano: '))
                else:
                    break
            
            id += 1
            noticias.append({"ID": id,"Titulo": noticiaTitu ,"Descricao": noticiaDesc, "Noticia": noticiaComp, "DataDia": data_dia, "DataMes": data_mes, "DataAno": data_ano})
            print("\nNoticia Enviada com Sucesso!")

        elif pg2 == "2":
            id_edit = int(input("Digite o ID da noticia que deseja editar: "))
            for noticia in noticias:
                if noticia['ID'] == id_edit:
                    noticia['Titulo'] = input("Digite o novo titulo: ")
                    noticia['Descricao'] = input("Digite a nova descricao: ")
                    noticia['Noticia'] = input("Digite a nova noticia: ")
                    print("\nNoticia atualizada com sucesso!")
                    break
            else:
                print("Noticia não encontrada.")

        elif pg2 == "3":
            id_remove = int(input("Digite o ID da noticia que deseja remover: "))
            for noticia in noticias:
                if noticia['ID'] == id_remove:
                    confirm = input("Tem certeza que deseja remover esta noticia? (s/n): ")
                    if confirm.lower() == 's':
                        noticias.remove(noticia)
                        print("\nNoticia removida com sucesso!")
                        break
                    elif confirm.lower() == 'n':
                        print("\nOperação cancelada.")
                        break
                else:
                    print("\nNoticia não encontrada.")

        elif pg2 == "4":
            if noticias:
                for noticia in noticias:
                    print(f"\nID: {noticia['ID']}   Titulo: {noticia['Titulo']}   Descricao: {noticia['Descricao']}   Data: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}")

            else:
                print("\nNenhuma noticia foi criada ainda.")
            
        elif pg2 == "5":
            id_view = int(input("Digite o ID da noticia que deseja ver: "))
            for noticia in noticias:
                if noticia['ID'] == id_view:
                    print(f"\nID: {noticia['ID']}\nTitulo: {noticia['Titulo']}\nDescricao: {noticia['Descricao']}\nData: {noticia['DataDia']}/{noticia['DataMes']}/{noticia['DataAno']}\nNoticia: {noticia['Noticia']} ")
                    break
            else:
                print("\nNoticia não encontrada.")

        elif pg2 == "0":
            logado = False
            tipo_usuario = None
            idade = 0
            while True:
                print("_" * 50)
                print("\nBem vindo(a) ao APP de Noticias da Catolica")
                print("Escolha uma opçao para prosseguir\n")
                print("[1] Criar Conta")
                print("[2] Login")
                print("[0] Sair")
                pg1 = input("\n")
                print("_" * 50)

                if pg1 == "0":
                    break

                elif(pg1 != "1") and (pg1 != "2") and (pg1 != "0"):
                    
                    print("_" * 50)
                    print('\nInformação Inválida!')
                    print('Responda com 1, 2 ou 0')
                    print("_" * 50)

                elif pg1 == "1":
                    user = input("Usuario : ")
                    if user in dados:
                        print("Esse nome de Usuario ja existe.")
                        continue
                    demenor = False
                    reporteron = False
                    leitoron = False
                    while True:
                        if demenor:
                            break
                        if reporteron or leitoron:
                            break
                        senh = input("Senha : ")
                        if(len(senh) < 8):
                            print('Sua senha precisa ter no mínimo 8 digitos')
                        elif(len(senh) >= 8):
                            senh1 = input("Confirme a Senha : ")
                            if senh == senh1:
                                print("_" * 50)
                                tipo_usuario = input("\nDigite:\n'reporter' para criar uma conta de reporter ou\n'leitor' para criar uma conta de leitor : ")
                                while True:
                                    if tipo_usuario.lower() not in ["leitor", "reporter"]:
                                        print("\nTipo de Usuario Invalido.\n")
                                        tipo_usuario = input("\nDigite:\n'reporter' para criar uma conta de reporter ou\n'leitor' para criar uma conta de leitor : ")
                                    elif tipo_usuario.lower() in ["leitor", "reporter"]:
                                        if tipo_usuario.lower() == "reporter":
                                            idade = int(input("Digite sua idade : "))
                                            if idade < 18:
                                                print("\nPara ser Reporter você precisa ter pelo menos 18 anos.")
                                                demenor = True
                                                break
                                            elif idade >= 18:
                                                print(f"\nUsuario {tipo_usuario} cadastrado com Sucesso!")
                                                dados[user] = senh
                                                reporteron = True
                                                break
                                        elif tipo_usuario.lower() == "leitor":
                                            print(f"\nUsuario {tipo_usuario} cadastrado com Sucesso!")
                                            dados[user] = senh
                                            leitoron = True
                                            break
                            elif senh != senh1:
                                print("\nSenhas nao Coincidem\n")

                elif pg1 == "2":
                    while True:
                        login1 = input("\nUsuario : ")
                        senha1 = input("Senha : ")
                        if dados.get(login1) == senha1:
                            print("_" * 50)
                            print(f"\nBem Vindo ao APP Noticias da Catolica, {login1}!")
                            logado = True
                            break
                        else:
                            print("\nUsuario ou Senha Incorretos.")
                if logado:
                    break
            if leitoron:
                reporteron = False
                break
        if not reporteron:
            break

if leitoron:
    print("Leitor Ok")
