import random
from collections import namedtuple

APOSTAMINIMA = float(5)

def players ():
    N_players= float(input("Digite o número de jogadores (Máximo dois): "))
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
        carteira = float(input("{}, quanto você tem em dinheiro? R$:".format(listaplayers[i])))
        if carteira < ApostaMinima :
            while carteira < ApostaMinima:
                carteira = float(input("Valor menor que a aposta. Digite quanto você tem em dinheiro {}? R$:".format(listaplayers[i])))
        Player_Dinheiro[listaplayers[i]] = [carteira]
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

def ApostaOutrasVezes (ListaComPlayers,PlayersEDinheiro, PlayersComAposta):
    for jogadores in ListaComPlayers:
        VAposta = int(input("{}, quanto você quer apostar?".format(jogadores)))
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


def Tirar1Carta (Player, baralho, PlayerComCartas):
    C = baralho.pop()
    PlayerComCartas[Player].append(C)
    return PlayerComCartas    
        

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


def SomaDemaisRodadas (NomeJogador, MãoJogadores, SomaJogadores):
    soma = 0
    i = 0
    while i < len(MãoJogadores[NomeJogador]):
        if MãoJogadores[NomeJogador][i]=='K' or MãoJogadores[NomeJogador][i]=='Q' or MãoJogadores[NomeJogador][i]=='J':
            soma +=10
            i += 1
        else:
            valorcarta = float(MãoJogadores[NomeJogador][i])
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

#Dicionario em que chave é o nome do jogador e o valor é o valor da carteira
CarteiraEPlayer = ValorDinheiro(ListaPlayers,APOSTAMINIMA) 
print ("\n", CarteiraEPlayer)



JogoRodando = "sim"
while JogoRodando == "sim":
    
    for player in CarteiraEPlayer:
        if CarteiraEPlayer[player] == 0:
            ListaPlayers.remove(player)            

    #Aposta para a primeira rodada
    ApostaEPlayers = ApostaPrimeiraVez(ListaPlayers, CarteiraEPlayer)
    print ("\nJogadores e suas respectivas apostas: \n", ApostaEPlayers)
    print ("\nValores atuais da carteira de cada jogador\n", CarteiraEPlayer)

    MaoDealer = Tirar2Cartas(ListaPlayers, baralho)[0]
    MaoJogadores = Tirar2Cartas(ListaPlayers, baralho)[1]
 
    print ("\nA mão do Dealer é: \n",MaoDealer)
    print (MaoJogadores)


    SomaMaoDealer = SomarCartasPrimeiraVez(ListaPlayers, MaoDealer, MaoJogadores)[0]
    SomaMaoJogadores = SomarCartasPrimeiraVez(ListaPlayers, MaoDealer, MaoJogadores)[1]

    print ("\nA soma da mão do dealer é: \n",SomaMaoDealer)
    print (SomaMaoJogadores)

    #Verificar se algum jogador ganhou na primeira rodada
    for jogador in ListaPlayers:
        if SomaMaoJogadores[jogador] == 21:
            ValorGanho = ApostaEPlayers[jogador]*1.5
            print ("\n {} ganhou o jogo de primeira, você irá receber R${}".format(jogador,ValorGanho))
            respostaJogarDeNovo = input("\nJogar novamente?\n")
            if respostaJogarDeNovo!="sim" or respostaJogarDeNovo!="não":
                while respostaJogarDeNovo!="sim" or respostaJogarDeNovo!="não":
                    respostaJogarDeNovo = input("\nJogar novamente?\n")
                else:
                    JogoRodando = respostaJogarDeNovo    
       
    #Perguntar aos demais jogadores se eles querem mais uma carta
    for jogador in ListaPlayers:
        print ("{}, suas cartas são: \n{}".format(jogador, MaoJogadores[jogador]))
        continua = input("{} quer mais uma carta? \nDigite sim ou não\n".format(jogador))
        while continua != "não":  
        
            if continua == "sim":
                MãoJogadores = Tirar1Carta(jogador, baralho, MaoJogadores)
                SomaMaoJogadores = SomaDemaisRodadas(jogador, MaoJogadores, SomaMaoJogadores)
                print ("\n Suas cartas são \n {} \n totalizando {} pontos".format(MaoJogadores[jogador], SomaMaoJogadores[jogador]))
            
                if SomaMaoJogadores[jogador] < 21:
                    continua = input("{} quer mais uma carta? \nDigite sim ou não\n".format(jogador))
                elif SomaMaoJogadores[jogador] == 21:
                    print ("\n {0} ganhou a partida e recebe R${1}".format(jogador,ApostaEPlayers[jogador]))
                    continua = "não"
                else:
                    print ("\n Suas foram {}, totalizando {} pontos".format(MaoJogadores[jogador], SomaMaoJogadores[jogador]))
                    print ("\n {0} perdeu!".format(jogador))
                    continua = "não"
                
            elif continua != "sim" or continua != "não":
                continua = input("{} quer mais uma carta? \n Digite apenas sim ou não".format(jogador))
            else:
                continua = "não"
                
    #Realizando a interação no terminal para saber se os jogadores irão jogar novamente         
    respostaJogarDeNovo = input("\nJogar novamente?\n")
    if respostaJogarDeNovo!="sim" and respostaJogarDeNovo!="não":
        while respostaJogarDeNovo!="sim" and respostaJogarDeNovo!="não":
            respostaJogarDeNovo = input("\nJogar novamente?\n")
        JogoRodando = respostaJogarDeNovo
        
    else:
        JogoRodando = respostaJogarDeNovo
