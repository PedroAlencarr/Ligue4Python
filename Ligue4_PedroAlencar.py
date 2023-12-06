#Pedro Henrique Alencar Ramos (23204610)
from random import randint

def escolhe_linha(m, jogada):
    tam = len(m) - 1 #começa da ultima linha (6) até chegar na 0
    l_atual = m[tam][jogada]
    while l_atual != space and tam >0:
        tam -=1
        l_atual = m[tam][jogada]
    if l_atual != space:
        return 10 #quer dizer que a coluna está cheia
    else:
        return tam

class Juiz():
    def __init__(self, m, jogador):
        self.matriz = m
        self.jogador_atual = jogador
    
    def mostra_matriz(self):  #função que printa a matriz
        print('------' * 5) #aqui é printado as barras superiores do jogo
        for l in self.matriz:
            for c in l:
                print('|', c, end=' ') #para cada coluna eu printo a barra e depois a própria coluna, a qual pode ser vazia ou com o simbolo de um dos players
            print('|') #printa a ultima barra lateral de cada linha
            print('------' * 5) #printa a linha tracejada inferior de cada linha da matriz
    
    def troca_jogador(self, jogador):
        self.jogador_atual = jogador
        if self.jogador_atual == 'X':
            self.jogador_atual = 'O'
            return self.jogador_atual
        else:
            self.jogador_atual = 'X'
            return self.jogador_atual
    
    def troca_jogador_comp(self, jogador):
        self.jogador_atual = jogador
        if self.jogador_atual == 'X':
            self.jogador_atual = 'C'
            return self.jogador_atual
        else:
            self.jogador_atual = 'X'
            return self.jogador_atual

    def empate(self):#função para determinar se empatou
        contador = 0
        for linha in self.matriz:
            for elemento in linha:
                if elemento != ' ':
                    contador += 1
        if contador == 42: #se todos os elementos da matriz forem diferentes do space, ou seja, 42 elementos, entao empatou, pois não ha mais como jogar
            return True
        return False
    
    def checa_horizontal(self, l_atual, player): #checa se tem 4 simbolos/players iguais seguidos na horizontal
        win = 0 #contador de pontos
        coluna = 0
        while coluna < 7:
            if self.matriz[l_atual][coluna] == player: #posição vai sendo pulada de coluna em coluna sem alterar a linha
                win +=1 #se na posição atual da matriz tiver o simbolo do player recebido como parâmetro, marca ponto
            else:
                win = 0 #se não for igual ao player recebido como parâmetro, win continua/retorna pra 0
            if win == 4: #se tiver 4 wins, ou seja, 4 marcações do player recebido seguidas é True e o jogador ganha
                return True
            coluna +=1    #se não aconteceu a vitoria ainda e a coluna ainda é <7 então a coluna continua aumentando para não ficar em loop infinito
        return False #caso não tenha vitória, retorna falso.
    
    def checa_vertical(self, c_atual, player): #checa se tem 4 simbolos/players iguais seguidos na vertical
        win = 0 #contador de pontos
        linha = 0
        while linha < 6:
            if self.matriz[linha][c_atual] == player: #posição vai sendo pulada de linha em linha sem alterar a coluna 
                win +=1 #se na posição atual da matriz tiver o simbolo do player recebido como parâmetro, marca ponto.
            else:
                win = 0 #se não for igual ao player recebido como parâmetro, win continua/retorna pra 0
            if win == 4: #se tiver 4 wins, ou seja, 4 marcações do player recebido seguidas é True e o jogador ganha
                return True
            linha +=1   #se não aconteceu a vitoria ainda e a linha ainda é <6 então a linha continua aumentando para não ficar em loop infinito  
        return False
    
    def checa_diagonal_p(self, c_atual, l_atual, player): #checa se tem 4 simbolos/players iguais seguidos na diagonal da esquerda para a direita
        win = 0 #contador de pontos
        while c_atual > 0 and l_atual > 0: #aqui é diminuido a posição da diagonal em coluna atual e linha atual, pois ao diminuir os dois na mesma quantidade permanecemos na diagonal correta. 
            c_atual -=1
            l_atual -=1
        while c_atual <= 6 and l_atual <= 5: # aqui é percorrida a diagonal do ponto mais inicial dela (de cima pra baixo, da esquerda pra direita), limitado pelo valor máximo de colunas e linhas
            if self.matriz[l_atual][c_atual] == player: #se na posição atual da diagonal tiver o simbolo do player recebido como parâmetro, marca ponto.
                win +=1 #marca-se pontos
            else:
                win = 0 #se não for igual ao player recebido como parâmetro, win continua/retorna pra 0
            if win == 4:  #se tiver 4 wins, ou seja, 4 marcações do player recebido seguidas é True e o jogador ganha
                return True
            c_atual +=1 #coluna vai sendo aumentada no sentido esquerda para a direita
            l_atual +=1 #linha vai sendo aumentada no sentido de cima pra baixo
        return False
    
    def checa_diagonal_s(self, c_atual, l_atual, player): #checa se tem 4 simbolos/players iguais seguidos na diagonal da direita para a esquerda
        win = 0
        while c_atual <= 5 and l_atual > 0: #aqui é aumentado a posição da diagonal em coluna atual e diminuido em linha atual, pois ao alterar os dois na mesma quantidade permanecemos na diagonal correta. 
            c_atual +=1
            l_atual -=1
        while c_atual >= 0 and l_atual <= 5: #aqui é percorrida a diagonal do ponto mais inicial dela (de cima pra baixo, da direita pra esquerda), limitado pelo valor minimo da coluna e máximo de linhas
            if self.matriz[l_atual][c_atual] == player: #se na posição atual da diagonal tiver o simbolo do player recebido como parâmetro, marca ponto.
                win +=1
            else: 
                win = 0 #se não for igual ao player recebido como parâmetro, win continua/retorna pra 0
            if win == 4:
                return True #se tiver 4 wins, ou seja, 4 marcações do player recebido seguidas é True e o jogador ganha
            c_atual -=1 #coluna vai sendo diminuida no sentido direita para a esquerda
            l_atual +=1 #linha vai sendo aumentada no sentido de cima pra baixo
        return False
    
    def checa_jogada(self, jogada): #checa se a jogada está entre 0 e 6 para que seja o número das colunas.
        if jogada < 0 or jogada > 6:
            return False
        return True
#inicialização do código do jogo
space = '\U00000020' #código do espaço em string
player = 'O' #simbolo do player 
computador = 'C' #simbolo do computador
ganhou = False #controle de laço
linha_atual = 0
player_name = ''
player_name2 =''
matriz = [
    [space, space, space, space, space, space, space], 
    [space, space, space, space, space, space, space], 
    [space, space, space, space, space, space, space], 
    [space, space, space, space, space, space, space], 
    [space, space, space, space, space, space, space], 
    [space, space, space, space, space, space, space]
    ]
juiz = Juiz(matriz, player) #aqui é criado o objeto juiz que recebe a classe Juiz
#seleção de modo de jogo
modo_jogo = int(input(' Bem vindo!\n Você deseja jogar:\n Humano x Humano (Digite 1)\n Humano x Computador (Digite 2)\n Seleção:'))
while modo_jogo < 1 or modo_jogo > 2: #se o modo de jogo for inválido ele vai ficar pedindo até ser colocad o correto.
    modo_jogo = int(input(' Opção inválida!\n Você deseja jogar:\n Humano x Humano (Digite 1)\n Humano x Computador (Digite 2)\n Seleção:'))
if modo_jogo == 1:
    while player_name =='':
        player_name = input('Digite o nome do primeiro jogador: ')
    while player_name2 =='':
        player_name2 = input('Digite o nome do segundo jogador: ')
elif modo_jogo ==2:
    while player_name =='':
        player_name = input('Digite o nome do jogador: ')
juiz.mostra_matriz() #imprime a matriz
#modo de jogo humano x humano
if modo_jogo == 1: 
    while not ganhou:
        player = juiz.troca_jogador(player)
        #jogada do player 1
        if player == 'X':
            jogada_p1 = int(input(f'{player_name}, digite o número da coluna em que deseja jogar (de 0 a 6):'))
            while not juiz.checa_jogada(jogada_p1): #aqui o juiz está checando se o intervalo de jogada está certo
                    jogada_p1 = int(input(f'{player_name}, digite um número válido (0 a 6) para coluna em que deseja jogar:'))
            linha_atual = escolhe_linha(matriz, jogada_p1) #aqui está sendo checada qual linha da coluna selecionada mais para baixo está vazia
            while linha_atual ==10: #se a coluna está cheia o jogador tem que escolher uma coluna diferente da que está cheia
                jogada_p1 = int(input('Coluna cheia. Digite o número de outra coluna:'))
                linha_atual = escolhe_linha(matriz, jogada_p1)
            matriz[linha_atual][jogada_p1] = player #aqui a posição escolhida da matriz recebe o símbolo do jogador
            juiz.mostra_matriz()#imprime a matriz atualizada
            if ( #checagens do juiz para ver se o jogador 1 ganhou
                juiz.checa_horizontal(linha_atual, player) or
                juiz.checa_vertical(jogada_p1, player) or
                juiz.checa_diagonal_p(jogada_p1, linha_atual, player) or
                juiz.checa_diagonal_s(jogada_p1, linha_atual, player)    
                ):
                    print(f'Parabéns! {player_name} ganhou!')
                    ganhou = True
            if juiz.empate(): #checagem do juiz se empatou
                print('Empatou!')
                ganhou = True
        #jogada player 2
        elif player == 'O':
            jogada_p2 = int(input(f'{player_name2}, digite o número da coluna em que deseja jogar (de 0 a 6):'))
            while not juiz.checa_jogada(jogada_p2): #aqui o juiz está checando se o intervalo de jogada está certo
                    jogada_p2 = int(input(f'{player_name2}, digite um número válido (0 a 6) para coluna em que deseja jogar:'))
            linha_atual = escolhe_linha(matriz, jogada_p2) #aqui está sendo checada qual linha da coluna selecionada mais para baixo está vazia
            while linha_atual ==10: #se a coluna está cheia o jogador tem que escolher uma coluna diferente da que está cheia
                jogada_p2 = int(input('Coluna cheia. Digite o número de outra coluna:'))
                linha_atual = escolhe_linha(matriz, jogada_p2)
            matriz[linha_atual][jogada_p2] = player #aqui a posição escolhida da matriz recebe o símbolo do jogador
            juiz.mostra_matriz()#imprime a matriz atualizada
            if ( #checagens do juiz para ver se o jogador 1 ganhou
                juiz.checa_horizontal(linha_atual, player) or
                juiz.checa_vertical(jogada_p1, player) or
                juiz.checa_diagonal_p(jogada_p2, linha_atual, player) or
                juiz.checa_diagonal_s(jogada_p2, linha_atual, player)    
                ):
                    print(f'Parabéns! {player_name2} ganhou!')
                    ganhou = True
            if juiz.empate(): #checagem do juiz se empatou
                print('Empatou!')
                ganhou = True
#jogo contra o computador
if modo_jogo == 2: 
    while not ganhou:
        player = juiz.troca_jogador_comp(player)
        #jogada do player 1
        if player == 'X':
            jogada_p1 = int(input(f'{player_name}, digite o número da coluna em que deseja jogar (de 0 a 6):'))
            while not juiz.checa_jogada(jogada_p1): #aqui o juiz está checando se o intervalo de jogada está certo
                    jogada_p1 = int(input(f'{player_name}, digite um número válido (0 a 6) para coluna em que deseja jogar:'))
            linha_atual = escolhe_linha(matriz, jogada_p1) #aqui está sendo checada qual linha da coluna selecionada mais para baixo está vazia
            while linha_atual ==10: #se a coluna está cheia o jogador tem que escolher uma coluna diferente da que está cheia
                jogada_p1 = int(input('Coluna cheia. Digite o número de outra coluna:'))
                linha_atual = escolhe_linha(matriz, jogada_p1)
            matriz[linha_atual][jogada_p1] = player #aqui a posição escolhida da matriz recebe o símbolo do jogador
            juiz.mostra_matriz()#imprime a matriz atualizada
            if ( #checagens do juiz para ver se o jogador 1 ganhou
                juiz.checa_horizontal(linha_atual, player) or
                juiz.checa_vertical(jogada_p1, player) or
                juiz.checa_diagonal_p(jogada_p1, linha_atual, player) or
                juiz.checa_diagonal_s(jogada_p1, linha_atual, player)    
                ):
                    print(f'Parabéns! {player_name} ganhou!')
                    ganhou = True
            if juiz.empate(): #checagem do juiz se empatou
                print('Empatou!')
                ganhou = True
        elif player == 'C':
            jogada_comp = randint(0, 6)
            linha_atual = escolhe_linha(matriz, jogada_comp)
            while linha_atual ==10: #se a coluna está cheia o computador vai escolher aleatoriamente até ser o número de uma coluna vazia
                jogada_comp = randint(0, 6)
                linha_atual = escolhe_linha(matriz, jogada_comp)
            matriz[linha_atual][jogada_comp] = player #aqui a posição da matriz recebe o símbolo do computador
            juiz.mostra_matriz() #aqui printa a matriz atualizada
            if (#checagens do juiz para ver se o computador ganhou
                juiz.checa_horizontal(linha_atual, player) or
                juiz.checa_vertical(jogada_comp, player) or
                juiz.checa_diagonal_p(jogada_comp, linha_atual, player) or
                juiz.checa_diagonal_s(jogada_comp, linha_atual, player) 
                ):
                    ganhou = True #aqui a propria variavel de controle encerra o while
                    print('O computador ganhou!')
            if juiz.empate(): #checagem do juiz se empatou
                print('Empatou!')
                ganhou = True #aqui a propria variavel de controle encerra o while