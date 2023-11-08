#IMPORTS
import random
import json
 
#Classes
class Usuario: #define o usuario como um objeto
    def __init__(self,login = 'SemLogin',senha = 'SemSenha',permissoes = 0): #define seus indices para serem salvos e caso nao possua mantem o valor base
        self.login = login
        self.senha = senha
        self.permissoes = permissoes
 
#Funcoes
def get_cadastros(): #vai receber todos os cadastros ja feitos anteriormente
    try: #vai tentar ler o arquivo json mas caso haja algum problema ele ira executar a segunda parte
        with open('dados.json','r') as arquivo:
            usuarios = json.load(arquivo)
        return usuarios
    except: #se houve um erro na leitura ou o json esta corrompido ou nao exite, entao se cria um novo json
        usuarios = []
        return usuarios
 
def set_cadastro(): #vai criar um novo cadastro de um novo usuario
    global usuarios #recebe todos os outros cadastros já criados anteriormente
    print('Para realizar seu cadastro, precisamos de informacoes importantes.\nVoce devera preencher com Login e Senha para realizarmos seu cadastro')
    print('OBS: Cada Login e pessoal, nao e permitido nenhum login identico.')
    u_login = input('Login > ') #entrada Login
    u_senha = input('Senha > ') #entrada Senha
    has_user = False #predefine se existe ou não um usuario com esse Login
    try:
        for userid in range(0,len(usuarios),1): #tenta checar a base de dados de cadastro
            if usuarios[userid]['login'] == u_login or u_login == '':
                has_user = True 
    except:
        has_user = False
    if has_user == False:
        if u_login == '':
            u_login = 'SemLogin'
        if u_senha == '':
            u_senha = 'SemSenha'
            perm = 0
        else:
            perm = 1
        user = Usuario(u_login,u_senha,perm) #cria um novo usuario a partir da informações fornecidas
        usuarios.append(user.__dict__) #une ele a lista de usuarios registrados
        with open('dados.json','w') as arquivo:
            json.dump(usuarios,arquivo, indent=3)
        user_login()
    else:
        print('Login ja existente!!!') #caso já houvesse um login cadastrado assim ele retorna que já existe este login
        entrada()
 
def user_login(): #realizara o login do usuario
    global usuarios,user_id #recebe a lista de cadastros e pega o id do usuario
    print('Para confirmarmos seus dados por favor digite abaixo seu Login e Senha')
    u_login = input('Login > ') #entrada Login
    u_senha = input('Senha > ') #entrada Senha
    verified = False
    if u_login == '':
        u_login = 'SemLogin'
    if u_senha == '':
        u_senha = 'SemSenha'
    for userid in range(0,len(usuarios),1): #checa a base de dados de usuarios
        if usuarios[userid]['login'] == u_login and usuarios[userid]['senha'] == u_senha: #caso login e senha corretos retorna como user valido e coleta seu id
            verified = True
            user_id = userid
            break
    if verified == True: #verifica a autencidade do usuario e introduz a aplicacao
        print(f'Seja Bem-Vindo {usuarios[user_id]['login']}')
        menu()
    else:
        print('Login ou Senha incorretos, tente novamente!!!')
        entrada()

def entrada(): #define o inicio do programa com as opcoes de login e cadastro
    print('Para poder desfrutar desta ferramenta voce precisa antes se conectar com sua conta ou criar um cadastro\n  Digite 1 se - Realizar Login\n  Digite 2 se - Realizar Cadastro')
    opcao = input('> ')
    match opcao: #define a proxima acao de acordo com a opcao
        case '1': user_login()
        case '2': set_cadastro()
        case _ : 
            print('Opcao indisponivel\nTente Novamente!!!\n\n\n')
            entrada()
def menu(): #menu em que apresenta todas as opcoes da aplocacao
    global user_id,usuarios
    match usuarios[user_id]['permissoes']:
        case 0: #demonstra as opcoes para as pessoas que possuem Nivel 0 de Permissao
            print('Por nao possuir senha, suas atividades estao limitadas')
            print('O que deseja fazer?\n  Digite 1 se - Criptografar um texto\n  Digite 2 se - Sair')
            opcao = input('> ')
            match opcao: #define a proxima acao de acordo com a opcao
                case '1':
                    cripto()
                case '2' : return None
                case _ :
                    print('Opcao invalida')
                    menu()
        case 1: #demonstra as opcoes para as pessoas que possuem Nivel 1 de Permissao
            print('O que deseja fazer?\n  Digite 1 se - Criptografar um texto\n  Digite 2 se - Descriptografar um Texto\n  Digite 3 se - Sair')
            opcao = input('> ')
            match opcao: #define a proxima acao de acordo com a opcao
                case '1': cripto()
                case '2': decript()
                case '3' : return None
                case _ :
                    print('Opcao invalida')
                    menu()
        case 2: #demonstra as opcoes para as pessoas que possuem Nivel 2 de Permissao
            print('O que deseja fazer?\n  Digite 1 se - Criptografar um texto\n  Digite 2 se - Descriptografar um Texto\n  Digite 3 se - Configurar a permissao de um Usuario\n  Digite 4 se - Sair')
            opcao = input('> ')
            match opcao: #define a proxima acao de acordo com a opcao
                case '1': cripto()
                case '2': decript()
                case '3': mudar_perm()
                case '4' : return None
                case _ :
                    print('Opcao invalida')
                    menu()

def mudar_perm(): #Area para pessoas de Nivel 2 - Permite com que as pessoas alterem o Nivel de Permissao dos Usuarios
    global usuarios #Traz os dados de Usuarios para dentro da funcao
    print('Escolha o usuario que planeja alterar o nivel de permissao')
    for userid in range(0,len(usuarios)):
        print(usuarios[userid]['login'] + ' - Nivel de Permissao: ' + str(usuarios[userid]['permissoes'])) # mostra as pessoas cadastradas e suas devidas permissoes
    user = input('Nome do Usuario > ') #Entrada de Usuario
    for userid in range(0,len(usuarios),1): #Identifica o usuario na lista de Dados
        if usuarios[userid]['login'] == user:
            print(f'Escolha o novo nivel de permissao para {usuarios[userid]['login']}:\n  Digite 0 se - Apenas Criptografar\n  Digite 1 se - Apenas Criptografar e Descriptografar\n  Digite 2 se - Todas as Permissoes Anteriores e Alterar Permissoes')
            opcao = input('> ') #Entrada de Dados para definir o novo Nivel de Permissao
            match opcao: #define a proxima acao de acordo com a opcao
                case '0':usuarios[userid]['permissoes'] = 0
                case '1':usuarios[userid]['permissoes'] = 1
                case '2':usuarios[userid]['permissoes'] = 2
                case _: 
                    print('Opcao Invalida!!!')
                    mudar_perm()
            with open('dados.json','w') as arquivo: #Salva tidas as alteracoes no arquivo json
                json.dump(usuarios,arquivo, indent=3)
            break
    print("\nProcedimento feito com sucesso!!!")
    continuar()

def cripto(): #Area para pessoas de Nivel 0 - Permite criptografar textos entregando no fim o texto criptografado com sua respectiva chave
    global alfabeto #Traz o alfabeto para a funcao
    chave = random.randint(1,len(alfabeto)) #Gera uma nova Chave para criptografar o texto
    print('Digite o texto que sera criptgrafado:')
    texto = input('> ') #Entrada de Texto
    listtext = list(texto) #Transforma o texto em uma lista
    index = 0
    resposta = []
    while index < len(listtext) : #criptografa o texto
        if listtext[index] == " ":
            resposta.append(" ")
        elif (len(alfabeto))-(alfabeto.index(listtext[index])) > chave:
            resposta.append(alfabeto[(alfabeto.index(listtext[index]))+chave])
        elif (len(alfabeto))-(alfabeto.index(listtext[index])) <= chave:
            resposta.append(alfabeto[(chave) - ((len(alfabeto))-(alfabeto.index(listtext[index])))])
        else:
            resposta.append(" ")
        index +=1
    print('\nRESULTADO:') #Entrega o resultado final
    print(f'Sua chave e {chave}')
    print("".join(resposta))
    print("\nProcedimento feito com sucesso!!!")
    continuar()

def decript(): #Area para pessoas de Nivel 1 - Permite descriptografar o texto
    global alfabeto #Traz o alfabeto para a funcao
    chave = input('Digite sua Chave > ') #Entrada da Chave
    try: #Tenta converter a chave para o tipo int
        chave = int(chave) 
    except:
        print('Chave Invalida')
        decript()
    texto = input('Digite seu Texto > ') #Entrada de Texto Criptografado
    listtext = list(texto) #Transforma o texto em uma lista
    index = 0
    resposta = []
    while index < len(listtext) : #Descriptografa o Texto
        if listtext[index] == ' ':
            resposta.append(' ')
        else: 
            resposta.append(alfabeto[(alfabeto.index(listtext[index]))-chave])
        index +=1
    print('\nRESULTADO:') #Entrega o resultado final
    print("".join(resposta))
    print("\nProcedimento feito com sucesso!!!")
    continuar()

def continuar(): #Questiona se o Usuario deseja continuar ou sair da aplicacao
    opcao = input('\nDeseja continuar na aplicacao? (y/n) > ')
    match opcao: #define a proxima acao de acordo com a opcao
        case 'y': menu()
        case 'n': return None
        case _: 
            print('Opcao Invalida')
            continuar()


alfabeto = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
user_id = None
usuarios = get_cadastros()
entrada()