N_players= int(input("Digite o número de jogadores (Máximo quatro): "))
Players=[]
numero = 1
while numero <= N_players:
    player=input("Player {0} digite seu nome: ".format(numero))
    Players.append(player)
    numero+=1
print(Players)

cartas = {
        '2','3','4','5','6','7','8','9','10','Q','J','K',
        '2','3','4','5','6','7','8','9','10','Q','J','K',
        '2','3','4','5','6','7','8','9','10','Q','J','K',
        '2','3','4','5','6','7','8','9','10','Q','J','K'
        }

Carteira = float(input("Quandos você tem em dinheiro? R$:"))


    