import numpy as np

from scipy import stats

import os

#teoria do desvio maximo
class Estatistica: 

    def teoria_Desvio_Maximo_Soma(mediaA, desvioA, mediaB, desvioB):
    
        soma = mediaA + mediaB

        desvio = desvioA + desvioB

        return f'{soma} \pm {desvio}'

    def teoria_Desvio_Maximo_Subtracao(mediaA, desvioA, mediaB, desvioB):
    
        subtracao = mediaA - mediaB

        desvio = desvioA + desvioB

        return f'{subtracao} \pm {desvio}'

    def teoria_Desvio_Maximo_Produto(mediaA, desvioA, mediaB, desvioB):
        
        produto = mediaA * mediaB

        desvio = produto * (np.abs(desvioA/mediaA) + np.abs(desvioB/mediaB))

        return f'{produto} \ pm {desvio}'

    def teoria_Desvio_Maximo_Divisao(mediaA, desvioA, mediaB, desvioB):

        divisao = mediaA / mediaB

        desvio = divisao * (np.abs(desvioA/mediaA) + np.abs(desvioB/mediaB))

        return f'{divisao} \pm {desvio}'

    #teoria do desvio padrao
        
    def teoria_Desvio_Padrao_Soma(mediaA, desvioA, mediaB, desvioB):

        soma = mediaA + mediaB

        desvio = np.sqrt((desvioA**2) + (desvioB**2))

        return f'{soma}, \pm {desvio}'
        

    def teoria_Desvio_Padrao_Subtracao(mediaA, desvioA, mediaB, desvioB):

        subtracao = mediaA - mediaB

        desvio = np.sqrt((desvioA**2) + (desvioB**2))

        return f'{subtracao}, \pm {desvio}'

    def teoria_Desvio_Padrao_Produto(mediaA, desvioA, mediaB, desvioB):

        produto = mediaA * mediaB

        desvio = produto * np.sqrt( (desvioA/mediaA)**2 + (desvioB/mediaB)**2 )

        return f'{produto} \pm {desvio}'

    def teoria_Desvio_Padrao_Divisao(mediaA, desvioA, mediaB, desvioB):

        divisao = mediaA / mediaB

        desvio = divisao * np.sqrt( (desvioA/mediaA)**2 + (desvioB/mediaB)**2 )

        return f'{divisao} \pm {desvio}'
    #estatística geral

    def desvioPadraoDaMedia(dados):
    
        desvio = stats.tstd(dados)/ (np.sqrt(len(dados)))

        return desvio


#Atividades

def atividade1():

    '''
    --------- Gabarito da primeira atividade ---------
    1]
        a) 2
        b) 3
        c) 5 
        d) 3 
        e) 3 (o último zero da medida é devido à notação explícita, critério da meia unidade- não é algarismo significativo)
    2]
        A = 23,17 (3+1 = 4 alg. sig.)
        B = 12,21
        C = -7,51
        D = 0,238
    3]
        a) 24,14 (3+1 = 4 alg. sig.)
        b) 4,169
    4]
        a) A = 8,15912*10^2  e B = 3,453*10^2 (a forma implícita implica na representação da leitura na ordem das unidades)
        b) A = (8,159120 \pm 0,000005) * 10^2 e B = (3,4530 \pm 0,0005) * 10^2
        c) 5
    5]
        A = 5,22 * 10^5
        B = 28,10 * 10^3
        C = 13 * 10^2
        D = 426,68 * 10^4
        E = - 0,3

    '''

    q1 = int(input('Digite o número de erros da primeira questão: '))

    q2 = int(input('Digite o número de erros da segunda questão: '))

    q3 = int(input('Digite o número de erros da terceira questão: '))

    q4 = int(input('Digite o número de erros da quarta questão: '))

    q5 = int(input('Digite o número de erros da quinta questão: '))

    return 10 - (q1*0.4 + q2*0.5 + q3*1 + q4*(2/3) + q5*0.4)

def atividade2():

    '''
    --------- Gabarito da segunda atividade ---------
    1]
        Vv = 31.3949 \pm 0.0014
        Vi = 31.3949 \pm 0.0010

    2]
        Vv = 49.952 \pm 0.014
        Vi = 49.95 \pm 0.09
    3]
        Vv = 11.309 \pm 0.005
        Vi = 11.309 \pm 0.013
    4]
        Vv = 13.220 \pm 0.013
        Vi = 13.220 \pm 0.029 
    5]
        35.11 \pm 0.20

    '''
    q1 = int(input('Digite o número de erros da primeira questão: '))

    q2 = int(input('Digite o número de erros da segunda questão: '))

    q3 = int(input('Digite o número de erros da terceira questão: '))

    q4 = int(input('Digite o número de erros da quarta questão: '))

    q5 = int(input('Digite o número de erros da quinta questão: '))

    return 10 - (q1*0.5 + q2*0.5 + q3*0.5 + q4*0.5 + q5*1)

#Experimentos

def atividade3():
    '''
    --------- Gabarito da terceira atividade ---------
    
    1]
        a) t.d.p = 32,5 \pm 1,1
            t.d.m = 32,5 \pm 1,5

        b) t.d.p = 44,5 \pm 1,6
            t.d.m = 44,5 \pm 2,7
    2]
        a)  t.d.p.: S = 36,7 \pm 2,5
            t.d.m.: S = 36,7 \pm 3,4
        
        b) t.d.p.: D = 109 \pm 9
           t.d.m.: D = 109 \pm 12
    3]
        t.d.p.: S = 13,8 \pm 1,7
        t.d.m.: S = 13,8 \pm 2,1
    4]
        t.d.m.: V = 7.9 \pm 0.8

    5]
        I = (61281 + 0,6 * 10^3) gcm^2

    '''
    
    q1 = int(input('Digite o número de erros da primeira questão: '))

    q2 = int(input('Digite o número de erros da segunda questão: '))

    q3 = int(input('Digite o número de erros da terceira questão: '))

    q4 = int(input('Digite o número de erros da quarta questão: '))

    q5 = int(input('Digite o número de erros da quinta questão: '))

    return 10 - ((q1*0.25) + q2*(0.25) + q3*(0.5) + q4*(2) + q5*(1))
   
def medidas_De_Tempo():
    g = 9.81

    tabela_IA = []

    tabela_IIA = []

    tempos = []

    for distancia in tabela_IA:
      tempos.append(np.sqrt(((distancia/100)*2)/g))
    
    print(f'A média do tempo de reação é: {np.mean(tempos)}')

    print(f'A média do tempo do pêndulo é: {np.mean(tabela_IIA)} e o desvio padrão da média é: {Estatistica.desvioPadraoDaMedia(tabela_IIA)}')

def medidas_De_Comprimento():
    
    tabelaI = [4.3,2.2,3.4] #p/ unidade U 
     #C L H
    tabelaI_desvios = [0.05, 0.05,0.05]

    
    tabelaII =[] #C L H
    
    tabelaII_desvios = []
    

    tabelaIII = [] #Tabela V 


    print('Perímetro: ')

    print(Estatistica.teoria_Desvio_Padrao_Soma(2*tabelaII[0], 2*tabelaII_desvios[0], 2*tabelaII[2], 2*tabelaII_desvios[2]))
    
    print('Área da face maior: ')

    print(Estatistica.teoria_Desvio_Padrao_Produto(tabelaII[0], tabelaII_desvios[0], tabelaII[2], tabelaII_desvios[2]))
    #area = C * H 

    print('Tratamendo estatístico do diâmetro')

    print(f'{np.mean(tabelaIII)} \pm {Estatistica.desvioPadraoDaMedia(tabelaIII)}')

    print('Determinação da unidade U')

    print(Estatistica.teoria_Desvio_Padrao_Divisao(tabelaII[0],Estatistica.desvioPadraoDaMedia(tabelaIII), tabelaI[0], tabelaI_desvios[0]))

def main():

    #medidas_De_Tempo()

    #medidas_De_Comprimento()
    '''
    continuar = 'y'
    while continuar == 'y' or continuar == 'Y':

        print(atividade2())
        continuar = input('continuar?(y/n): ')
        os.system('cls')
    '''
    
   
if __name__ == '__main__':
    main()