import random
from collections import namedtuple
import time

APOSTAMINIMA = int(5)

def players ():
    N_players= int(input("\nDigite o número de jogadores: "))
    Players=[]
    numero = 1
    while numero <= N_players:
        player=input("\nPlayer {0} digite seu nome: ".format(numero))
        Players.append(player)
        numero+=1
    return Players

def ValorDinheiro (listaplayers,ApostaMinima):
    Player_Dinheiro = {}
    i=0
    while i < len(listaplayers):
        carteira = int(input("\n{}, quanto você tem em dinheiro? R$:".format(listaplayers[i])))
        if carteira < ApostaMinima :
            while carteira < ApostaMinima:
                carteira = int(input("\nValor menor que a aposta. Digite quanto você tem em dinheiro {}? R$:".format(listaplayers[i])))
        Player_Dinheiro[listaplayers[i]] = [carteira]
        i +=1
    return Player_Dinheiro

def ApostaOutrasVezes (ListaComPlayers,PlayersEDinheiro, PlayersComAposta):
    for jogadores in ListaComPlayers:
        VAposta = int(input("\n{}, quanto você quer apostar?".format(jogadores)))
        while (VAposta<0) or (VAposta>=PlayersEDinheiro[jogadores][0]) or (VAposta<APOSTAMINIMA) or VAposta!='fim':
            if VAposta < 0:
                print ("\nNão é possível apostar um número negativo \n")
                VAposta = int(input("{}, digite um valor positivo para apostar \n Aposta: R$ ".format(jogadores)))
            elif VAposta > PlayersEDinheiro[jogadores][0]:
                print ("\nVocê não possui dinheiro suficiente. Aposte com outro valor \n")
                VAposta = int(input("{}, digite um valor para apostar: R$ ".format(jogadores)))
            elif VAposta<APOSTAMINIMA:
                print ("\nValor abaixo da aposta mínima \n")
                VAposta = int(input("\n{}, digite um valor mais alto para a aposta \n Aposta: R$".format(jogadores)))
            else:
                PlayersComAposta[jogadores] = VAposta
            
        PlayersComAposta[jogadores] = VAposta
        ValorNovoCarteira = PlayersEDinheiro[jogadores][0] - VAposta
        PlayersEDinheiro[jogadores]= [ValorNovoCarteira]
                
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
                valorcarta = int(MãoJogadores[jogadores][i])
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
            valor = int(MaoDealer[i])
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
            elif MãoJogadores[NomeJogador][i]=='As':
                soma += 11
                i+=1
            elif MãoJogadores[NomeJogador][i]=='Joker':
                soma == 21
                i += len(MãoJogadores[NomeJogador])
            else:
                valorcarta = float(MãoJogadores[NomeJogador][i])
                soma += valorcarta
                i += 1
        for carta in MãoJogadores[NomeJogador]:
            if soma>21:
                if carta == 'As':
                    soma -= 10
                    
        SomaJogadores[NomeJogador] = soma

        return SomaJogadores


#Lista com os nomes dos players
ListaPlayers = players()

NUMERODEBARALHOS  = int(input("\nQuantos baralhos o jogo terá?\n" ))

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

#Aposta para a primeira rodada
ApostaEPlayers = {}

JogoRodando = "sim"
while JogoRodando == "sim":
    
    for player in ListaPlayers:
        if CarteiraEPlayer[player] == 0:
            ListaPlayers.remove(player)            

    for jogadores in ListaPlayers:
        VAposta = int(input("\n{}, quanto você quer apostar?".format(jogadores)))
        if VAposta == "fim":
            JogoRodando = "parar"
        else:    
            while (VAposta<0) or (VAposta>CarteiraEPlayer[jogadores][0]) or (VAposta<APOSTAMINIMA) or VAposta!='fim':
                if VAposta < 0:
                    print ("\nNão é possível apostar um número negativo \n")
                    VAposta = int(input("{}, digite um valor positivo para apostar \n Aposta: R$ ".format(jogadores)))
                elif VAposta > CarteiraEPlayer[jogadores][0]:
                    print ("\nVocê não possui dinheiro suficiente. Aposte com outro valor \n")
                    VAposta = int(input("{}, digite um valor para apostar: R$ ".format(jogadores)))
                elif VAposta<APOSTAMINIMA:
                    print ("\nValor abaixo da aposta mínima \n")
                    VAposta = int(input("\n{}, digite um valor mais alto para a aposta \n Aposta: R$".format(jogadores)))
                elif VAposta == "fim":
                    JogoRodando = "parar"
            
        ApostaEPlayers[jogadores] = VAposta
#        ValorNovoCarteira = CarteiraEPlayer[jogadores][0]
#        CarteiraEPlayer[jogadores]= [ValorNovoCarteira]
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
        print ("\n{}, suas cartas são: \n{}".format(jogador, MaoJogadores[jogador]))
        continua = input("\n{} quer mais uma carta? \nDigite sim ou não\n".format(jogador))
        if continua == 'fim':
            print('O jogo foi encerrado')
            time.sleep(3)
            exit()
            JogoRodando = "parar"
        while continua != "não":  
        
            if continua == "sim":
                MãoJogadores = Tirar1Carta(jogador, baralho, MaoJogadores)
                SomaMaoJogadores = SomaDemaisRodadas(jogador, MaoJogadores, SomaMaoJogadores)
                print ("\n Suas cartas são \n {} \n totalizando {} pontos".format(MaoJogadores[jogador], SomaMaoJogadores[jogador]))
            
                if SomaMaoJogadores[jogador] < 21:
                    continua = input("\n{} quer mais uma carta? \nDigite sim ou não\n".format(jogador))
                    if continua == 'fim':
                        print('O jogo foi encerrado')
                        continua = "não"
              
                elif SomaMaoJogadores[jogador] == 21:
                    print ("\n {0} ganhou a partida e recebe R${1}".format(jogador,ApostaEPlayers[jogador]))
                    continua = "não"
                    
                else:
                    print ("\n Suas foram {}, totalizando {} pontos".format(MaoJogadores[jogador], SomaMaoJogadores[jogador]))
                    print ("\n {0} perdeu!".format(jogador))
                    continua = "não"
                
            elif continua != "sim" or continua != "não":
                continua = input("\n{} quer mais uma carta? \n Digite apenas sim ou não".format(jogador))
                if continua == 'fim':
                    print('O jogo foi encerrado')
                    JogoRodando = "parar"
                
            else:
                continua = "não"
    #Retirando as caras para o Dealer, porém a soma deve ser menor que 17            
    while SomaMaoDealer <= 17:
        C = baralho.pop()
        MaoDealer.append(C) 
        soma = 0
        i = 0
        while i < len(MaoDealer):
            if MaoDealer[i]=='K' or MaoDealer[i]=='Q' or MaoDealer[i]=='J':
                soma +=10
                i += 1
            else:
                valorcarta = int(MaoDealer[i])
                soma += valorcarta
                i += 1
        SomaMaoDealer = soma
        
    print ("\nA mão do Dealer é: \n",MaoDealer)
    print ("\n",SomaMaoDealer)
    
    #Mostrando os resultados    
    print ("\nResultado final") 
    for jogadores in SomaMaoJogadores:
        if SomaMaoJogadores[jogadores] <= 21:
            if SomaMaoJogadores[jogadores] > SomaMaoDealer:
                print ("\n{} ganhou o jogo do Dealer!".format(jogadores))
                print ("\nVocê obteve {} pontos.".format(SomaMaoJogadores[jogadores]))
                ValorNovoCarteira = CarteiraEPlayer[jogadores][0] + ApostaEPlayers[jogadores]
                CarteiraEPlayer[jogadores]= [ValorNovoCarteira]
                print ("\n{} recebe R${}\nAgora você tem R${} ".format(jogadores,ApostaEPlayers[jogadores],CarteiraEPlayer[jogadores]))
                
            elif SomaMaoJogadores[jogadores] == SomaMaoDealer:
                print ("\n{} empatou com o Dealer!".format(jogadores))
                print ("\n Você obteve {} pontos.".format(SomaMaoJogadores[jogadores]))
                print ("\n{} recebeu seu dinheiro de volta\nVocê tem R${}".format(jogadores,CarteiraEPlayer[jogadores])) 
            else:
                print ("\n{} perdeu para o Dealear!".format(jogadores))
                print ("\n Você obteve {} pontos.".format(SomaMaoJogadores[jogadores]))
                ValorNovoCarteira = CarteiraEPlayer[jogadores][0] - ApostaEPlayers[jogadores]
                CarteiraEPlayer[jogadores]= [ValorNovoCarteira]
                print ("\n{} perdeu R${}\nAgora você tem R${} ".format(jogadores,ApostaEPlayers[jogadores],CarteiraEPlayer[jogadores]))
                
    
    respostaJogarDeNovo = input("\nJogar novamente?\n")
    while respostaJogarDeNovo!="sim" and respostaJogarDeNovo!="não":
         respostaJogarDeNovo = input("\nJogar novamente?\n")
    JogoRodando = respostaJogarDeNovo

        
        
