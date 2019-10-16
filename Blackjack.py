import random
from collections import namedtuple

APOSTAMINIMA = float(5)


def players ():
    N_players= int(input("Digite o número de jogadores (Máximo quatro): "))
    Players=[]
    numero = 1
    while numero <= N_players:
        player=input("Player {0} digite seu nome: ".format(numero))
        Players.append(player)
        numero+=1
    return Players

def ValorDinheiro (listaplayers,ApostaMinima):
    Player_Dinheiro = {}
    i=0
    while i < len(listaplayers):
        carteira = float(input("Quanto você tem em dinheiro {}? R$:".format(listaplayers[i])))
        if carteira < ApostaMinima :
            while carteira < ApostaMinima:
                carteira = float(input("Valor menor que a aposta. Digite quanto você tem em dinheiro {}? R$:".format(listaplayers[i])))
        Player_Dinheiro[listaplayers[i]] = carteira
        i +=1
    return Player_Dinheiro
def Aposta (ListaComPlayers, PlayersEDinheiro):
    PlayersComAposta = {}
    
    for jogadores in ListaComPlayers:
        VAposta = int(input("{}, quanto você quer apostar?".format(jogadores)))
        while (VAposta<0) or (VAposta>PlayersEDinheiro[jogadores]) or (VAposta<APOSTAMINIMA):
            if VAposta < 0:
                print ("Não é possível apostar um número negativo \n")
                VAposta = int(input("{}, digite um valor positivo para apostar \n Aposta: R$ ".format(jogadores)))
            elif VAposta > PlayersEDinheiro[jogadores]:
                print ("Você não possui dinheiro suficiente. Aposte com outro valor \n")
                VAposta = int(input("{}, digite um valor para apostar: R$ ".format(jogadores)))
            elif VAposta<APOSTAMINIMA:
                print ("Valor abaixo da aposta mínima \n")
                VAposta = int(input("{}, digite um valor mais alto para a aposta \n Aposta: R$".format(jogadores)))
            else:
                PlayersComAposta[jogadores] = VAposta
                PlayersEDinheiro[jogadores] = PlayersEDinheiro[jogadores] - VAposta
                
    return PlayersComAposta

def DistribuiCartas (dealer, ApenasPlayers):
    
    
    return 

def SomaCartas(players, dealer, cartas): 
    PlayersECartas = {}
    
    PlayersECartas[Dealer] = (int(dealer[0][0]) + int(dealer[1][0]))
    for j in players:
        soma = 0
        i = 0
        while i < len(players):
            soma = soma + int(cartas[n][0]) + int(cartas[n+1][0]) 
            i += 1
        PlayersECartas[players[j]] = soma
        
    return PlayersECartas

#Carta = namedtuple('Carta', ['face', 'naipe'])

#faces = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
#naipes = {'Ouro', 'Paus', 'Copas', 'Espada'}
#baralho = []

for i in faces:
    for n in naipes:
        baralho.append([i,n])
random.shuffle(baralho)
   
baralho=[
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        ]



cartas = []
Dealer=[]

n=0
while n<2:
    for p in ListaPlayers:
        C=baralho.pop()
        cartas.append(C)
        
    Ct=baralho.pop()
    Dealer.append(Ct)
    n+=1
    
print("\n{}\n{}, {}".format(ListaPlayers[0],cartas[0],cartas[1]))
n=1
while n<len(ListaPlayers):
    print("\n{}\n{}, {}".format(ListaPlayers[n],cartas[n+1],cartas[n+2])) 
    n+=1
    
print ("\n", cartas)

        
ListaPlayers = players()
print (ValorDinheiro(ListaPlayers,APOSTAMINIMA))
ListaPlayers = players()
print (ValorDinheiro(ListaPlayers,APOSTAMINIMA))

n=0
while n<2:
    for p in ListaPlayers:
        cartas=[]
        Dealer=[]
        cartas.append(baralho.pop(random.choice(baralho)))
    Dealer.append(baralho.pop(random.choice(baralho)))
    n+=1

print("Dealer""\n",Dealer)
for i in ListaPlayers:
    print("{}""\n".format(ListaPlayers[i]),cartas[i])
    

# Verificando se alguem ganhou na primeira rodada
i = 0
while i < len(ListaPlayers):
    if PlayersESoma[ListaPlayers[i]] == 21:
        ValorGanho = ApostaEPlayers[ListaPlayers[i]]*1.5
        print ("Você ganhou de primeira! \n Ganhou R$ {}".format(ValorGanho))
    else:
        i += 1
