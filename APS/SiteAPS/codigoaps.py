#IMPORTS, MODULOS
import random
import operator

#VARIAVEIS PRINCIPAIS
usuarios = []
entrou = 0
continuar = 0

#VARIAVEIS DE INPUT
cadastro = 0
u_login = ""
u_senha = ""

#FUNÇÕES
def Login() :
    global usuarios, entrou, u_login, u_senha
    print("Para confirmarmos que você realmente já está cadastrado.\nPreencha os dados abaixo.")
    u_login = str(input("Login > "))
    u_senha = str(input("Senha > ")) 
    if (u_login + u_senha) in usuarios and u_login != "" and u_senha != "":
        entrou = 1
    elif u_login == "" and u_senha == "":
        print("Preencha corretamente as informações de Login e Senha.")
        Login()
    else :
        print("Login ou Senha incorreto(s)\n Tente novamente.")
        Login()

    
def Cadastro() :
    global cadastro, usuarios, entrou, u_login, u_senha
    print("Uma pena que já não tenha sido cadastrado.\nComplete as informações abaixo para que possamos realizar seu cadastro.")
    u_login = str(input("Login > "))
    u_senha = str(input("Senha > "))
    usuarios.append(u_login + u_senha + "/")
    with open('cadastros.txt','r') as salvar:
        usuarios = operator.add(u_login + u_senha + "/",salvar.read())
    with open('cadastros.txt','w') as salvar_2 :
        salvar_2.write(str(usuarios))
    print("Login cadastrado!! Você já está dentro")
    entrou = 1

def Menu() :
    print("O que deseja fazer?\n    Digite 1 se - Criptografar um texto\n    Digite 2 se - Descriptografar um texto")
    opcao = int(input("> "))
    if opcao == 1 :
        alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        chave = random.randint(0,len(alphabet))
        print(f"Sua chave é {chave}")
        texto = str(input("Digite seu texto > "))
        print("")
        listtext = list(texto)
        index = 0
        resposta = []
        while index < len(listtext) :
            if listtext[index] == " ":
                resposta.append(" ")
            elif (len(alphabet))-(alphabet.index(listtext[index])) > chave:
                resposta.append(alphabet[(alphabet.index(listtext[index]))+chave])
            elif (len(alphabet))-(alphabet.index(listtext[index])) <= chave:
                resposta.append(alphabet[(chave) - ((len(alphabet))-(alphabet.index(listtext[index])))])
            else:
                resposta.append(" ")
            index +=1
        print("".join(resposta))
        print("\nProcedimento feito com sucesso!!!") 
        continuar = str(input("Deseja continuar fazendo algo? (y/n) > "))
        if continuar == "y":
            Menu()
        else:
            entrou = 0
            print("\nVocê saiu da aplicação!!!")
    elif opcao == 2 :
        alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        chave = int(input("Digite sua chave > "))
        texto = str(input("Digite seu texto > "))
        print("")
        listtext = list(texto)
        index = 0
        resposta = []
        while index < len(listtext) :
            if listtext[index] == ' ':
                resposta.append(' ')
            else: 
                resposta.append(alphabet[(alphabet.index(listtext[index]))-chave])
            index +=1
        print("".join(resposta))
        print("\nProcedimento feito com sucesso!!!") 
        continuar = str(input("Deseja continuar fazendo algo? (y/n) > "))
        if continuar == "y":
            Menu()
        elif continuar == "n":
            entrou = 0
            print("\nVocê saiu da aplicação!!!")
        else:
            entrou = 0
            print("\nVocê saiu da aplicação!!!")


def Entrada() :
    global u_login
    print("Seja Bem-vindo %s \n" %u_login)

#EXECUÇÃO DO PROGRAMA
try:
    with open('cadastros.txt','r') as inicio :
        usuarios = str(inicio.read())
        usuarios = usuarios.split('/')
except:
    with open('cadastros.txt','w') as inicio :
        None
print("Seja Bem-Vindo\nVocê possui algum cadastro?\n    Digite 1 se - Não possuo cadastro\n    Digite 2 se - Possuo cadastro")
cadastro = int(input("> "))
if cadastro == 1 :
    Cadastro()
elif cadastro == 2 :
    Login()
else :
    print("Opção inválida!!!")

if entrou == 1 :
    Entrada()
    Menu()