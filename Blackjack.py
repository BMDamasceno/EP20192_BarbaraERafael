import random

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

baralho = {
        '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8, '9':9, '10':10,'Q': 10,'J': 10, 'K': 10, 'ÁS': 11,
        '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8, '9':9, '10':10,'Q': 10,'J': 10, 'K': 10, 'ÁS': 11,
        '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8, '9':9, '10':10,'Q': 10,'J': 10, 'K': 10, 'ÁS': 11,
        '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,'8':8, '9':9, '10':10,'Q': 10,'J': 10, 'K': 10, 'ÁS': 11
        }

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