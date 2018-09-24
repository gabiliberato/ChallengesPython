# Matriz - Caça Palavras

#Tabela para visualisar o caça palavras
#String
matriz ="""Y C Y G W R P K H O A B U V H
S C I R F Z B M C P M Y C F P
U A F R X T W L O T A S M X C
E J R A G S A V H G L R X G F
K X Z T A P C V J Q M J Y M G
G C X Q E W S I A L A E O I V
I F Y F X V A L P A L H E T A
L E K O U U T I G U A N A O I
V H I H Z U C I F R A C L U B
A R Z H X A L C O G E E U V R
U N B S T M U S I C A T L A A
W R A U J A B I S S N O R I S
C M P L E N P A L C O A H B E
T M F O T Z M P T R E S J R L
F S I K U F P E Q T A M L O J"""

print(matriz, '\n')

#Separa linhas da matriz
m = [k.split() for k in matriz.upper().splitlines()]

#Numero de linhas
nL = len(m)
# numero de colunas
nC = len(m[0])

# matriz resposta preenchida com pontos
resposta = [["." for _ in range(nC)] for __ in range(nL)]


op = input('\n''Jogo Caça Palavras, deseja jogar?' '\n' 'Digite S para sim e N para sair:  ')
op = op.upper()

#Loop
while op != 'N':

    #Recebe a palavra
    palavra = input('\n''Digite a palavra para a busca: ')
    # passa palavra para maiuscula
    palavra = palavra.upper()
    # tamanho da palavra
    N = len(palavra)

    # iteracao nas linhas e colunas
    for linha in range(nL):
        for coluna in range(nC):
            try:
                # se a posicao (x,y+tamanho da palavra) da matriz for igual a palavra
                if ''.join(m[linha][coluna:(coluna+N)]) == palavra:
                  # matriz resposta recebe palavra na posicao (x,y)
                  for k in range(coluna, coluna + N): resposta[linha][k] = m[linha][k]
                if ''.join((q[coluna] for q in m[linha:(linha+N)])) == palavra:
                  for k in range(linha, linha + N): resposta[k][coluna] = m[k][coluna]
            except IndexError: pass

    print(*(' '.join(k) for k in resposta), sep = '\n')
    print(matriz)
    op = input('\n''Jogo Caça Palavras, deseja continuar a jogar?' '\n' 'Digite S para sim e N para sair:')
