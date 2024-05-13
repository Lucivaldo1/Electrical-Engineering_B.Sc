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
   
#acho q n precisa da cascata
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

#-=-=-=-=-=-=-=-=-=Matriz de transmissao-=-=-=-=-=-=-=-=-=#

ABCD = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2, CargaZ2, LT4, T3, CargaZ3)

#print('Matriz da linha de transmissão: \n', ABCD)

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z3 -=-=-=-=-=-=-=-=-=#

A = ABCD[0][0]

B = ABCD[0][1]

C = ABCD[1][0]

D = ABCD[1][1]

Eqs = np.array([[A + (B /Zc3), 0], [-(C+(D/Zc3)), 1]])

Igualdade = np.array([69e3*np.sqrt(2), 0])

solucao = np.linalg.solve(Eqs, Igualdade) #o erro esta aqui

print(f'Para a carga Z3, V = {round(np.abs(solucao[0]),4)} ∠ {np.angle(solucao[0])} V')

print(f'Para a carga Z3, I = {np.abs(solucao[0]/Zc3)} ∠  {np.angle(solucao[0]/Zc3)} A ') #aqui esta correto

#-=-=-=-=-=-=-=-=-=solucao do sitema para Z2 -=-=-=-=-=-=-=-=-=#

ABCD_Z2 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1, LT3, T2, CargaZ2)

A2 = ABCD_Z2[0][0]

B2 = ABCD_Z2[0][1]

C2 = ABCD_Z2[1][0]

D2 = ABCD_Z2[1][1]

Eqs2 = np.array([[A2 + (B2 /Zc2), 0], [-(C2+(D2/Zc2)), 1]])

Igualdade2 = np.array([69e3*np.sqrt(2), 0])

solucao2 = np.linalg.solve(Eqs2, Igualdade2)

print(f'Para a carga Z2, V = {np.abs(solucao2[0])} ∠ {np.angle(solucao2[0])} V')

print(f'Para a carga Z2, I = {np.abs(solucao2[0]/Zc2)} ∠  {np.angle(solucao2[0]/Zc2)} A') #aqui esta correto


#-=-=-=-=-=-=-=-=-=solucao do sitema para Z1 -=-=-=-=-=-=-=-=-=#

ABCD_Z3 = Cascata(serie, T1, QuadripoloParalelo(LT1, LT2,), 
                         CargaZ1)

A3 = ABCD_Z3[0][0]

B3 = ABCD_Z3[0][1]

C3 = ABCD_Z3[1][0]

D3 = ABCD_Z3[1][1]

Eqs3 = np.array([[A3 + (B3 /Zc1), 0], [-(C3+(D3/Zc1)), 1]])

Igualdade3 = np.array([69e3*np.sqrt(2), 0])

solucao3 = np.linalg.solve(Eqs3, Igualdade3)

print(f'Para a carga Z1, V = {np.abs(solucao3[0])} ∠ {np.angle(solucao3[0])} V')

print(f'Para a carga Z1, I = {np.abs(solucao3[0]/Zc1)} ∠  {np.angle(solucao3[0]/Zc1)} A') #aqui esta correto

