import numpy as np

import matplotlib.pyplot as plt

from scipy import signal

import matplotlib.animation as animation

from matplotlib.widgets import Button
'''
funções:

rampa = np.arange(tamanho do sinal)
'''


#variáveis editáveis
sinal1 = [6, 1]

sinal2 = [5, 2]

x1 = np.arange(0, sinal1[0], 1)

y1 = np.ones( sinal1[0] ) * sinal1[1]

x2 = np.arange(0, sinal2[0], 1)

y2 = np.ones( sinal2[0] ) * sinal2[1]

#convolução

convolucao = signal.fftconvolve(y1, y2)

x3 = np.arange(0, len(convolucao), 1)

fig, (ax, ax2) = plt.subplots(2, 1)

ax.grid(True)

ax2.grid(True)

scat = ax.scatter(x3, convolucao)

ax2.stem(x1, y1, linefmt='grey', markerfmt='D')

ax2.stem(x2, y2, linefmt = ':')

pause = False

def on_click(event):

    global pause

    pause = not pause

    if pause:
        animacao.event_source.stop()
    
    else:
        animacao.event_source.start()

ax_botao = plt.axes([0.8, 0.01, 0.15, 0.05]) 

botao = Button(ax_botao, 'Play | Pause', color= 'lightgoldenrodyellow', hovercolor='0.975')

botao.on_clicked(on_click)

def animate(i):
        
    global pause

    if not pause:

        x = x3[:i]
        
        y = convolucao[:i]

        xa = x1

        ya = y1[:i]

        data = np.stack([x, y]).T
        
        scat.set_offsets(data)

        return scat

animacao = animation.FuncAnimation(

    fig = fig,

    func = animate,

    frames = 60,

    interval = 1000 # cada ponto aparece a cada 1000ms
)

plt.show()



'''
Referências

https://matplotlib.org/stable/gallery/lines_bars_and_markers/stem_plot.html#sphx-glr-gallery-lines-bars-and-markers-stem-plot-py

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.stem.html#matplotlib.pyplot.stem

https://matplotlib.org/stable/users/explain/animations/animations.html

https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation

Observações:

Embora seja recomendado pela prórpia documentação da biblioteca numpy utilizar o linspace, para esta aplicação,
devido a natureza discreta dos sinais, utilizar o arange já que sempre saberemos o tamanho do vetor e o passo será sempre 1.

A função Stem não existe na classe Funcanimation.
'''