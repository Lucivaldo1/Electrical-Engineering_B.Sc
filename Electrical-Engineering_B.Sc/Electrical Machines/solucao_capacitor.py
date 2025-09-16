import numpy as np
'''
exemplo 1961
p = 4
f = 60
s = 0.5
V = 110
a = 1.18
Z1a = 7.14 +3.22j +3 -14.5j
Z1m = 2.02 + 2.79j
Z2 = 4.12 + 2.12j
Xm = 66.8j
questão 4 da lista:
p = 4
f = 60
s = 0.0328
V = 115
a = 0.916
Z1a = 10.7 + 2.43j
Z1m = 2.54 + 2.9j
Z2 = 2.36 + 1.73j
Xm = 59.13j
Ploss = 44.4
#10.3 kothari

Z2 = 14.3 + 6.84j
Xm = 138.5j
s = 1
V = 220
a = 1.25
Z1a = 15.5 +13.5j - 257j
Z1m = 9.2 +8.7j
p = 6
f = 50

#exemplo 10.5 kothari
Z1a = 5.16 - 225.6j
Z1m = 4.2 + 11.3j
Z2 = 7.48 + 7.2j
Xm = 250j
s = 0.04
V = 220
a = 1.05

p = 4
f = 50
Ploss = 45

#questao 10.2
p = 4
f = 60
s = 0.5
V = 110
a = 1.18
Z1a = 7.14 +3.22j +3 -14.5j
Z1m = 2.02 + 2.79j
Z2 = 4.12 + 2.12j
Xm = 66.8j

#questao 5 da lista
Z1m = 5.7 + 6.5j
Z1a = 9.62 + 10.06j -133j
Z2 = 8.86 + 5.08j
Xm = 85.65j
a = 1.244
s = 1
V = 115
f = 60
p = 4
Ploss = 41.9
'''
#questao 5 da lista
Z1m = 5.7 + 6.5j
Z1a = 9.62 + 10.06j -133j
Z2 = 8.86 + 5.08j
Xm = 85.65j
a = 1.244
s = 1
V = 115
f = 60
p = 4
Ploss = 41.9

def Z(Z2, Xm):
    
    Zf = ((np.real(Z2)/s + np.imag(Z2)*1j) * Xm)/ (np.real(Z2)/s + np.imag(Z2)*1j+Xm)
    Zb = ((np.real(Z2)/(2-s) + np.imag(Z2)*1j)*Xm)/(np.real(Z2)/(2-s) + np.imag(Z2)*1j+Xm)
    return Zf, Zb
Zf, Zb = Z(Z2, Xm)
def Vm(V, a):
    Vmf = 0.5*V*(1-1j/a)
    Vmb = 0.5*V*(1+1j/a)
    return Vmf, Vmb
Vmf, Vmb = Vm(V, a)
def Z0Zd(Z1a, Z1m, a):
    Z0 = 0.5*(Z1a/(a**2) + Z1m)
    Zd = 0.5*(Z1a/(a**2) - Z1m)
    return Z0, Zd

Z0,Zd = Z0Zd(Z1a, Z1m, a)

Imf = (Vmf*(Z0+Zb) + Vmb*Zd) / ((Z0+Zf)*(Z0+Zb) - Zd**2)
Imb = (Vmb*(Z0+Zf) + Vmf*Zd) / ((Z0+Zf)*(Z0+Zb) - Zd**2)

def ImIa(Imf, Imb,a):
    Im = Imf + Imb
    Ia = (1j/a)*(Imf - Imb)
    return Im, Ia
Im,Ia = ImIa(Imf, Imb,a)
Il = Im + Ia
Pgf = np.real(Zf)*2 * np.abs(Imf)**2 
Pgb = 2 * np.abs(Imb)**2 * np.real(Zb)
Pin = np.abs(Il)*V*np.cos(np.angle(Il))
Pm = 2*(np.real(Zf)*np.abs(Imf)**2 -(np.real(Zb)*np.abs(Imb)**2)) 
Peixo = Pgf - Pgb - Ploss
T = 2/((120*f/p)*2*np.pi/60)* (np.real(Zf)*np.abs(Imf)**2 -(np.real(Zb)*np.abs(Imb)**2))
def results():
    print(f'Zf = {Zf}')
    print(f'Zb = {Zb}')
    print(f'Vmf = {Vmf} = {np.abs(Vmf)}/_ {np.angle(Vmf)*180/(np.pi)}')
    print(f'Vmb = {Vmb} = {np.abs(Vmb)}/_ {np.angle(Vmb)*180/(np.pi)}')
    print(f'Z0 = {Z0}')
    print(f'Zd = {Zd}')
    print(f'Imf = {Imf} = {np.abs(Imf)}/_ {np.angle(Imf)*180/(np.pi)}')
    print(f'Imb = {Imb} = {np.abs(Imb)}/_ {np.angle(Imb)*180/(np.pi)}')
    print(f'Im = {Im}  = {np.abs(Im)}/_ {np.angle(Im)*180/(np.pi)}')
    print(f'Ia = {Ia}  = {np.abs(Ia)}/_ {np.angle(Ia)*180/(np.pi)}')
    print(f'Il = {Il} = {np.abs(Il)}/_ {np.angle(Il)*180/(np.pi)}')
    print(f'Pgf = {Pgf}')
    print(f'Pgb = {Pgb}')
    print(f'Pm = {Pm}')
    print(f'Pin = {Pin}')
    print(f'Peixo = {Peixo}')
    print(f'Rendimento = {Peixo/Pin}')
    print(f'Tstart = {T}')
    return ''
print(results())
