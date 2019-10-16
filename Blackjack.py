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


def ApostaPrimeiraVez (ListaComPlayers, PlayersEDinheiro):
    PlayersComAposta = {}
    
    for jogadores in ListaComPlayers:
        VAposta = int(input("{}, quanto você quer apostar?\n".format(jogadores)))
        while (VAposta<0) or (VAposta>PlayersEDinheiro[jogadores][0]) or (VAposta<APOSTAMINIMA):
            if VAposta < 0:
                print ("Não é possível apostar um número negativo \n")
                VAposta = int(input("{}, digite um valor positivo para apostar \n Aposta: R$ ".format(jogadores)))
            elif VAposta > PlayersEDinheiro[jogadores][0]:
                print ("Você não possui dinheiro suficiente. Aposte com outro valor \n")
                VAposta = int(input("{}, digite um valor para apostar: R$ ".format(jogadores)))
            elif VAposta<APOSTAMINIMA:
                print ("Valor abaixo da aposta mínima \n")
                VAposta = int(input("{}, digite um valor mais alto para a aposta \n Aposta: R$".format(jogadores)))
            
        PlayersComAposta[jogadores] = VAposta
        ValorNovoCarteira = PlayersEDinheiro[jogadores][0] - VAposta
        PlayersEDinheiro[jogadores]= ValorNovoCarteira
                
    return PlayersComAposta

def Tirar2Cartas (ListaPlayers, baralho):
    Dealer= []
    PlayerComCartas = {}
    n=0
    for jogadores in ListaPlayers:
        PlayerComCartas[jogadores] = [] 
    while n<2:
        for p in ListaPlayers:
            C=baralho.pop()
            PlayerComCartas[p].append(C)
        Ct=baralho.pop()
        Dealer.append(Ct)
        n+=1
    return Dealer, PlayerComCartas


def SomarCartasPrimeiraVez (ListaPlayers, MãoDealer, MãoJogadores):
   
    JogadorESuaSoma = {}
    for jogadores in ListaPlayers:
        soma = 0
        i = 0
        while i < len(MãoJogadores[jogadores]):
            if MãoJogadores[jogadores][i]=='K' or MãoJogadores[jogadores][i]=='Q' or MãoJogadores[jogadores][i]=='J':
               soma +=10
               i += 1
            else:
                valorcarta = float(MãoJogadores[jogadores][i])
                soma += valorcarta
                i += 1
        JogadorESuaSoma[jogadores] = soma
        
    SomaDealer = 0
    i = 0
    while i < len(MãoDealer):
        if MaoDealer[i]=='K' or MaoDealer[i]=='Q' or MaoDealer[i]=='J':
            SomaDealer += 10
            i += 1
        else:
            valor = float(MaoDealer[i])
            SomaDealer += valor
            i += 1
        
    return SomaDealer, JogadorESuaSoma
        
    return PlayersECartas
def SomaDemaisRodadas (ListaPlayers, MãoJogadores, SomaJogadores):
    for NomeJogador in ListaPlayers:
        soma = 0
        i = 0
        while i < len(MãoJogadores[NomeJogador]):
            if MãoJogadores[NomeJogador][i]=='K' or MãoJogadores[NomeJogador][i]=='Q' or MãoJogadores[NomeJogador][i]=='J':
               soma +=10
               i += 1
            else:
                valorcarta = float(MãoJogadores[jogadores][i])
                soma += valorcarta
                i += 1
        SomaJogadores[NomeJogador] = soma
        
        return SomaJogadores


#Lista com os nomes dos players        
ListaPlayers = players()

NUMERODEBARALHOS  = int(input("Quantos baralhos o jogo terá?\n" ))
    
baralho=[
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        2,3,4,5,6,7,8,9,10,'Q','J','K',
        ]*NUMERODEBARALHOS 

#Embaralhando o baralho
random.shuffle(baralho)

#Dicionario em que a chave corresponde ao nome do jogador e o valor é valor da carteira
CarteiraEPlayer = ValorDinheiro(ListaPlayers,APOSTAMINIMA) 
print ("\n", CarteiraEPlayer) #Imprimindo o dicionario para ver se está funcionando

#Aposta para a primeira rodada
ApostaEPlayers = ApostaPrimeiraVez(ListaPlayers, CarteiraEPlayer)
print ("\n", ApostaEPlayers)
print ("\n", CarteiraEPlayer)

#Sorteando as duas cartas do delaer e dos jogadores
MaoDealer = Tirar2Cartas(ListaPlayers, baralho)[0]
MaoJogadores = Tirar2Cartas(ListaPlayers, baralho)[1]
#Imprimindo para verificar se está funcionando    
print ("\n",MaoDealer)
print (MaoJogadores)

# Verificando se alguem ganhou na primeira rodada
 for jogador in ListaPlayers:
    if SomaMaoJogadores[jogador] == 21:
        ValorGanho = ApostaEPlayers[jogador]*1.5
        print ("\n {} ganhou o jogo e recebe R${}".format(jogador,ValorGanho))
        ListaPlayers.remove(jogador)
