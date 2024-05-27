import numpy as np

w  = 120*np.pi

Rf, Xf = 4, 0.38j #parâmetros de impedância em série com o transformador T1

Zth = Rf + Xf #impedância série Thevenin

R1, X1, = 7.6e-3, 3.8e-3j #parametros gerais do transformador

R2, X2 = 33.9e-3, 0.85e-3j #parametros gerais do transformador

Z1 = R1 + X1 #impedancia 1 do transformador 

Z2 = R2 + X2 #impedancia 2 do transformador 

#impedancias "shunt" dos transformadores
ZT1 =  (4320 * 5050j) / (4320 + 5050j)

ZT2 = (432000 * 505000j) / (432000 + 505000j)

ZT3 = (402000 * 607000j) / (402000 + 607000j)

#Cargas
Zc1 = 8400 + (1j* w * 46)

Zc2 = 1175.55 + (1j* w * 6.43)

Zc3 = 529 + (1j * w * 2.9)

#-=-=-=-=-=-=-=-=-=Modelos de Transmissao-=-=-=-=-=-=-=-=-=#

def TransformadorIdeal(N1,N2):
    #esta funcao retorna a matriz de transmissao de um transformador ideal
    #considerando que I2 sai do pelo a diretia

    matriz_Transformador = np.array([[ N1/N2 ,   0   ],
                       [   0   , N2/N1 ]])
    
    return matriz_Transformador

def ImpedanciaSerie(Z):

    matriz_Z = np.array([[ 1 , Z ],
                         [ 0 , 1 ]])

    return matriz_Z

def AdmitanciaShunt(Y):

    matriz_Y = np.array([[ 1 , 0 ],
                         [ Y , 1 ]])
    return matriz_Y

def CircuitoT(Z1, Z2, Y):

    matriz_T = np.array([[ 1 + (Y * Z1) , Z1 + Z2 + (Y * Z1 * Z2) ],
                         [      Y       ,       1 + (Y * Z2)      ]])
    
    return matriz_T

def CircuitoPI(Z, Y1, Y2):

    matriz_Pi = np.array([[ 1 + (Y2 * Z)          ,       Z     ],
                         [ Y1 + Y2 + (Y1* Y2 * Z) , 1 + (Y1 * Z)]])

    return matriz_Pi


def LinhaDeTransmissao(Comprimento):
    
    #a entrada de comprimento deve ser feita em Km

    R = 0.182 * Comprimento

    L = 1j*w * 2.28e-3  * Comprimento

    C1 =  0.0140e-6 * Comprimento

    C = C1/2

    C_fasorial = 1 / (1j*120* np.pi * C)

    Z = R + L

    Y1 = 1 / C_fasorial

    Y2 = 1 / C_fasorial
    return CircuitoPI(Z, Y1, Y2)
   
def Cascata(*matrizes):
    resultado = matrizes[0]
    for matriz in matrizes[1:]:
        resultado = np.dot(resultado, matriz)
    return resultado


def QuadripoloParalelo(matriz1, matriz2):

    Aa, Ba, Ca, Da = matriz1[0][0], matriz1[0][1], matriz1[1][0], matriz1[1][1]

    Ab, Bb, Cb, Db = matriz2[0][0], matriz2[0][1], matriz2[1][0], matriz2[1][1]
    
    den = Ba + Bb

    A = (( Aa * Bb ) + (Ab * Ba ) ) / den

    B = ( Ba * Bb ) / den

    C = ( Ca + Cb + ( ( Aa - Ab )*( Db - Da ) / den ) )

    D = ( (Bb * Da ) + ( Ba * Db )) / den

    matriz_Paralelo = np.array( [[ A , B],
                                 [ C , D]])

    return matriz_Paralelo


def Solver(Quadripolo, carga):

    A, B, C, D = Quadripolo[0][0], Quadripolo[0][1], Quadripolo[1][0], Quadripolo[1][1]

    Equacoes = np.array([[A + (B / carga), 0], [-(C+(D/carga)), 1]])

    Igualdade = np.array([69e3, 0])

    Solucao =  np.linalg.solve(Equacoes, Igualdade) 

    print(f'V = {round(np.abs(Solucao[0]),2)} ∠ {round(np.angle(Solucao[0])*180/np.pi,2)}° V \n')

    print(f'I = {round(np.abs(Solucao[0]/carga),2)} ∠  {round(np.angle(Solucao[0]/carga)*180/np.pi,2)}° A \n') 

    CorrenteGerador = f'Para o gerador I, = {round(np.abs(Solucao[1]),2)} ∠ {round(np.angle(Solucao[1])*180/np.pi,2)}° A'

    return CorrenteGerador

#-=-=-=-=-=-=-=-=-=Quadripolos-=-=-=-=-=-=-=-=-=#

#impedancia em serie com a fonte

serie = ImpedanciaSerie(Zth)

#transformadores

T1 = np.dot(CircuitoT(Z1, Z2, 1/ZT1), TransformadorIdeal(69, 500))

T2 = np.dot(CircuitoT(Z1, Z2, 1/ZT2), TransformadorIdeal(500, 230))

T3 = np.dot(CircuitoT(Z1, Z2, 1/ZT3), TransformadorIdeal(230, 69))

#Linhas de transmissao

LT1 = LinhaDeTransmissao(100)

LT2 = LinhaDeTransmissao(100)

LT3 = LinhaDeTransmissao(100)

LT4 = LinhaDeTransmissao(80)

#Cargas

CargaZ1 = AdmitanciaShunt(1/Zc1)

CargaZ2 = AdmitanciaShunt(1/Zc2)

CargaZ3 = AdmitanciaShunt(1/Zc3)

#-=-=-=-=-=-=-=-=-=Simulacao da linha sem alterações-=-=-=-=-=-=-=-=-=#

Igualdade = np.array([69e3, 0])

ABCD = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2, CargaZ2, LT4, T3, CargaZ3)

#print(Solver(ABCD, Zc3)) #-> retorna a corrente no gerador

print('-=-'*10, 'Linha de transmissão original', '-=-'*10, '\n')

print('Matriz da linha de transmissão: \n', ABCD,'\n')

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z1 -=-=-=-=-=-=-=-=-=#

ABCD_Z1 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,))

print('Para Z1: \n')

Solver(ABCD_Z1, Zc1)

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z2 -=-=-=-=-=-=-=-=-=#

ABCD_Z2 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2)

print('Para Z2: \n')

Solver(ABCD_Z2, Zc2)

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z3 -=-=-=-=-=-=-=-=-=#

ABCD_Z3 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2, CargaZ2, LT4, T3)

print('Para Z3: \n')

Solver(ABCD_Z3, Zc3)

#-=-=-=-=-=-=-=-=-=Simulacao com ajuste de tap -=-=-=-=-=-=-=-=-=#

T1_tap = np.dot(CircuitoT(Z1, Z2, 1/ZT1), TransformadorIdeal(69, 493.95889))

T2_tap = np.dot(CircuitoT(Z1, Z2, 1/ZT2), TransformadorIdeal(500, 227.718))

T3_tap = np.dot(CircuitoT(Z1, Z2, 1/ZT3), TransformadorIdeal(230, 68.099))

ABCD_tap = Cascata(serie, T1_tap, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2_tap, CargaZ2, LT4, T3_tap, CargaZ3)

print('-=-'*10, 'Linha de transmissão com ajuste de tap', '-=-'*10, '\n')

print('Matriz da linha de transmissão: \n', ABCD_tap,'\n')

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z1 -=-=-=-=-=-=-=-=-=#

ABCD_tap_Z1 = Cascata(serie, T1_tap, QuadripoloParalelo(LT1, LT2,))

print('Para Z1 com ajuste de tap: \n')

Solver(ABCD_tap_Z1, Zc1)

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z2 -=-=-=-=-=-=-=-=-=#

ABCD_tap_Z2 = Cascata(serie, T1_tap, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2_tap)

print('Para Z2 com ajuste de tap: \n')

Solver(ABCD_tap_Z2, Zc2)

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z3 -=-=-=-=-=-=-=-=-=#

ABCD_tap_Z3 = Cascata(serie, T1_tap, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2_tap, CargaZ2, LT4, T3_tap)

print('Para Z3 com ajuste de tap: \n')

Solver(ABCD_tap_Z3, Zc3)

#-=-=-=-=-=-=-=-=-=Simulacao com reatores -=-=-=-=-=-=-=-=-=#

reator1 = AdmitanciaShunt( 1/(1j * w * 600e-3))

reator2 = AdmitanciaShunt( 1/(0.001 + 1j * w * 3))   

reator3 = AdmitanciaShunt( 1/(0.001+ 1j * w * 1.25))  

ABCD_reator = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, reator1, LT3, T2, CargaZ2, reator2, LT4, T3, CargaZ3, reator3)

print('-=-'*10, 'Linha de transmissão com associação de reatores em paralelo com a carga', '-=-'*10, '\n')

print('Matriz da linha de transmissão: \n', ABCD_reator,'\n')

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z1 -=-=-=-=-=-=-=-=-=#

ABCD_reator_Z1 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), CargaZ1)

print('Para Z1 com associuação de reator em paralelo: \n')

Solver(ABCD_reator_Z1, Zc1)

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z2 -=-=-=-=-=-=-=-=-=#

ABCD_reator_Z2 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, reator1, LT3, T2, CargaZ2, reator2)

print('Para Z2 com associuação de reator em paralelo: \n')

Solver(ABCD_reator_Z2, Zc2)

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z3 -=-=-=-=-=-=-=-=-=#

ABCD_reator_Z3 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, reator1, LT3, T2, CargaZ2, reator2, LT4, T3, CargaZ3)

print('Para Z3 com associuação de reator em paralelo: \n')

Solver(ABCD_reator_Z3, Zc3)
