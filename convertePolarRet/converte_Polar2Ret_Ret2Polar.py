import math, cmath
import numpy as np
from numpy import pi

def menu():         #Menu interativo para realizar varias operações com apenas uma execução
    print("""
            Temos as seguintes opções:
	    (1) = Converter de Polar para Retângular
	    (2) = Converter de Retangular para Polar
	    (0) = Para SAIR

	""")
    return int(input('Escolha uma opção: '))

def getRet():       #Função que coleta do usuário os valores reais e imaginários da forma retangular
    real = float(input("Digite a parte real: "))
    imag = float(input("Digite a parte imaginária: "))
    return real, imag

def getPolar():     #Função que coleta do usuário os valores de módulo e fase da forma polar
    mod = float(input("Digite o módulo R: "))
    fase = float(input("Digite o angulo phi: "))
    return mod, fase

def convRet2Pol(x): #Função de conversão de Retangular para Polar
    modulo = abs(x) #retira o módulo de x, tirando a raiz da soma dos quadrados da parte real e da imaginária
    fase = np.arctan2(x.imag,x.real) * 180 / pi     #Para encontrar a fase em graus, fazemos o arctg da parte imaginaria sobre a real e multiplicamos por 180/pi
    return modulo, fase

def convPol2Ret(modulo,fase):   #Função de conversão de Polar para Retangular
    x = modulo * np.cos(math.radians(fase)) #Para achar a parte real devemos multiplicar o módulo pelo cosseno da fase 
    y = modulo * np.sin(math.radians(fase)) #Para achar a parte real devemos multiplicar o módulo pelo seno da fase
    retangular = complex(x,y)               #Por fim juntamos os dois valores obtidos em apenas uma variável do tipo complexa
    return retangular
    
while True:     #laço de repetição do meno
    escolhaMenu = menu()
    if escolhaMenu == 0:    #condição de saída do programa
        print('Até a próxima!!')
        exit()

    elif escolhaMenu == 1:      #Questão 1: Converte da forma Polar Exponencial para a forma Retangular
        modulo, fase = getPolar()   #Chamamos a função para obter o modulo e a fase
        retangular = convPol2Ret(modulo,fase)   #chamamos a função de conversão para obter o numero na forma retangular
        print('Para ',modulo,'e^j',fase,'-> Convertendo para Coordenada Retangular temos:\n ', retangular)

    elif escolhaMenu == 2:      #Questão 2: Converte de Retangular para polar na forma modulo e fase e na formula exponencial 
        parteReal, parteImag = getRet() #Chamamos a função para obter as partes reais e imaginária do número
        numero = complex(parteReal,parteImag)   #une ambos números para formar um único numero do tipo complexo
        modulo,fase = convRet2Pol(numero)   #Chama a função de conversão de Retangular para polar
        print('Para',numero,'-> Convertendo para Coordenada Polar temos:\n ',modulo,'/__',fase, '=', modulo,'e^j', fase)

    else:   #Se não digitar uma opção válida, o menu irá se repetir
        print('\nEssa não é uma opção válida! Tente Novamente \n')




