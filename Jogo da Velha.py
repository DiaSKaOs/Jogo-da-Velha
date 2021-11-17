import os #Limpar tela (cls)
import random #Números aleatórios   
from colorama import Fore, Back, Style #Colorama = cor, fore = cor da frente, back = cor do fundo, style = estilo da fonte

JogarNovamente = "s" #Determina se o jogador vai jogar novamente 
Jogadas = 0 #Número de jogadas que foram feitas no jogo
QuemJoga = 2 # 1 = CPU | 2 = Jogador secundário
MaxJogadas = 9
Vit = "n" #Verifica a vitória
velha = [
    [" ", " ", " "], #Linha0Coluna0/Linha0Coluna1/Linha0Coluna2
    [" ", " ", " "], #Linha1Coluna0/Linha1Coluna1/Linha1Coluna2
    [" ", " ", " "]  #Linha2Coluna0/Linha2Coluna1/Linha2Coluna2
]

#Função que vai ficar responsável pelo gerenciamento do jogo no caso o desenho dele

def tela():
    global velha
    os.system("cls") 
    print("    0   1   2")
    print("0: " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2]) #linha 0  
    print("   -----------")
    print("1: " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2]) #Linha 1 
    print("   -----------")
    print("2: " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2]) #Linha 2
    print("   -----------")
    print(" Jogadas: " + Fore.GREEN + str(Jogadas) + Fore.RESET)

def CPUJoga():
    global Jogadas
    global QuemJoga
    global Vit
    global MaxJogadas
    if QuemJoga == 1 and Jogadas<MaxJogadas:#Procura e verifica se a posição esta vazia
        l = random.randrange(0,3)
        c = random.randrange(0,3)
        while velha [l][c]!= " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[l][c]="O"
        Jogadas+= 1
        QuemJoga = 2

def JogadorJoga():
    global Jogadas
    global QuemJoga
    global Vit
    global MaxJogadas
    if QuemJoga == 2 and Jogadas<MaxJogadas:
        l = int(input("Linha..: "))
        c = int(input("Coluna..: "))
        try:
            velha[l][c]="X"
            QuemJoga = 1
            Jogadas+=1
        except:
            print("Linha e ou coluna invalida")
            Vit="n"

def VerificarVitoria(): #Loop dentro de outro
    global velha
    vitoria = "n"
    simbolos = ["X","O"]
    for s in simbolos: #Verificação do X e O
            vitoria = "n"
            #Verificar Linhas
            il=ic=0 #Indice de Linhas e Colunas
            while il<3:
                soma = 0
                ic = 0 
                while ic<3:
                    if(velha[il][ic]==s):
                        soma+=1
                    ic+=1
                if(soma==3):
                    vitoria = s
                    break
                il+=1
            if(vitoria!="n"):
                break 
            #Verificar Colunas
            il=ic=0 #Indice de Linhas e Colunas
            while ic<3:
                soma = 0
                il = 0 
                while il<3:
                    if(velha[il][ic]==s):
                        soma+=1
                    il+=1
                if(soma==3):
                    vitoria = s
                    break
                ic+=1
            if(vitoria!="n"):
                break 
            #Verificar diagonal 1
            soma = 0
            idiag = 0 #Índice diagonal
            while idiag<3:
                if(velha[idiag][idiag]==s):
                    soma+=1
                idiag+=1
            if(soma==3):
                vitoria=s
                break
            #Verificar diagonal 1
            soma = 0
            idiagl = 0 #Índice diagona Linha
            idiagc = 2 #Índice diagonal Coluna 
            while idiagc>=0:
                if(velha[idiagl][idiagc]==s):
                    soma+=1
                idiagl+=1
                idiagc-=1
            if(soma==3):
                vitoria=s
                break
    return vitoria 

def redefinir():
    global velha
    global Jogadas
    global QuemJoga
    global MaxJogadas
    global Vit     
    Jogadas = 0 #Número de jogadas que foram feitas no jogo
    QuemJoga = 2 # 1 = CPU | 2 = Jogador secundário
    MaxJogadas = 9
    Vit = "n" #Verifica a vitória
    velha = [
        [" ", " ", " "], #Linha0Coluna0/Linha0Coluna1/Linha0Coluna2
        [" ", " ", " "], #Linha1Coluna0/Linha1Coluna1/Linha1Coluna2
        [" ", " ", " "]  #Linha2Coluna0/Linha2Coluna1/Linha2Coluna2
    ]

while(JogarNovamente=="s" or JogarNovamente=="S"): 
    while True:
        tela()
        JogadorJoga()
        CPUJoga()
        tela()
        Vit = VerificarVitoria()
        if(Vit!="n")or(Jogadas>=MaxJogadas):
            break

    print(Fore.RED + "FIM DE JOGO" + Fore.YELLOW)
    if(Vit=="X" or Vit=="O"):
        print("Resultado: Jogador  " + Vit + " Venceu")
    else:
        print("Resultado: Empate")
    JogarNovamente=input(Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
    redefinir()