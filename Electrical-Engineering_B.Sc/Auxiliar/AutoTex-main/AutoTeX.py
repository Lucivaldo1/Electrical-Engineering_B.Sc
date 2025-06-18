from datetime import date

import PySimpleGUI as sg
from PySimpleGUI import (Image, Column, VSeparator, Push)

tema = 'DarkBlack'


def capa():
    sg.theme(tema)   
   

    try:
        with open ('dados.txt','r',encoding='utf-8',) as f:
            linhas = f.readlines()
            nome = linhas[0].strip()
            matricula = linhas[1].strip()
            turma = linhas[2].strip()
            professor = linhas[3].strip()
    except:
        nome = ''
        matricula = ''
        turma = ''
        professor = ''

    layout = [  [sg.Text('Nome:'), sg.InputText(default_text=nome)],
                ########################################
                [sg.Text('Matrícula:'),sg.InputText(default_text=matricula)],
                ########################################
                [sg.Text('Título do experimento: '),sg.InputText()],
                ########################################
                [sg.Text('Número da turma: '),sg.InputText(default_text=turma)],
                #######################################
                [sg.Text('Nome do professsor:'),sg.InputText(default_text=professor)],
                ########################################    
                [Push(), sg.Checkbox('Lembrar de mim',default= True, key='lembrar'),Push()],
                ########################################################
                [sg.Button('Ok'), sg.Button('Cancelar')] ]

    
    window = sg.Window('Capa do relatório', layout, element_justification='r',return_keyboard_events=True, finalize = True)

    window.bind('<Return>', 'Ok')
    window.bind('<Escape>', 'Cancelar')
    
    while True:

        
        event, values = window.read()
        if  event == 'Ok': 
            nome = values[0]
            matricula = values[1]
            titulo = values[2]
            turma = values[3]
            professor = values[4]

            with open('modeloCapa.txt',encoding='utf-8') as f:
                contents = f.read()

            if ('titulo_f' in contents):
                contents = contents.replace('titulo_f',titulo)


            if ('nome_f' in contents):
                contents = contents.replace('nome_f',nome)

            if ('matricula_f' in contents):
                contents = contents.replace('matricula_f',matricula)

            if ('turma_f' in contents):
                contents = contents.replace('turma_f',turma)

            if ('professor_f' in contents):
                contents = contents.replace('professor_f',professor)

            if ('ano_f' in contents):
                ano = date.today().year
                
                contents = contents.replace('ano_f',str(ano))

            if values['lembrar']:
                with open ('dados.txt','w',encoding='utf-8',) as f:
                    f.write(nome + '\n')
                    f.write(matricula + '\n')
                    f.write(turma + '\n')
                    f.write(professor + '\n')
                
            else:
                with open ('dados.txt','w',encoding='utf-8',) as f:
                    f.write('\n')
                    f.write('\n')
                    f.write('\n')
                    f.write('\n')
            

            
            my_popup(contents)
            
            break

        elif event == sg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            break
    
    window.close()


def figura():
    sg.theme(tema)

    layout =[[sg.Text('Título da figura: '), sg.InputText()],
             [sg.Text('Nome do arquivo:'), sg.InputText()],
             [sg.Text('Fonte da figura:'), sg.InputText()],
             [sg.Text('Rótulo (referência cruzada)'), sg.InputText()],
             [sg.Button('Ok'), sg.Button('Cancelar')]
             ]
    figura = sg.Window('Figura', layout, element_justification='r',return_keyboard_events=True, finalize = True)
    

    figura.bind('<Return>', 'Ok')

    figura.bind('<Escape>', 'Cancelar')

    while True:

        event, values =  figura.read()

        if event == 'Ok':
            titulo = values[0]
            arquivo = values[1]
            fonte = values[2]
            label = values [3]

            with open('figura.txt',encoding='utf-8') as f:
                contents = f.read()

            if ('titulo_f' in contents):
                contents = contents.replace('titulo_f',titulo)


            if ('arquivo_f' in contents):
                contents = contents.replace('arquivo_f',arquivo)

            if ('fonte_f' in contents):
                contents = contents.replace('fonte_f',fonte)

            if ('label_f' in contents):
                contents = contents.replace('label_f',label)

           
            
            my_popup(contents)
            figura.close()
            break
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            figura.close()
            break

###
def preencher(MAX_ROWS, MAX_COLS, titulo, fonte, label):
    sg.theme(tema)



    layout = [[sg.Text('Preencha sua tabela')] + [sg.Text('')]] + \
             [[sg.Input('', justification='r', key=(r, c)) for c in range(MAX_COLS)] for r in range(MAX_ROWS)] + \
             [[sg.Button('Ok'), sg.Button('Cancelar')]]

    
    window = sg.Window('Prévia da tabela', layout, default_element_size=(12, 1), element_padding=(1, 1), return_keyboard_events=True, finalize = True)

    window.bind('<Return>','Ok')
    window.bind('<Escape>','Cancelar')

    current_cell = (0, 0)
    while True:  
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':     
            window.close()
            break
        if event == 'Ok':
            
            table = [[values[(row, col)] for col in range(MAX_COLS)] for row in range(MAX_ROWS)] 

            tabela = table
            
            
            
            with open ('tabela.txt','w',encoding='utf-8',) as f:
                f.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n \\begin{table}[h] \n \\caption{')
                f.write(titulo)
                f.write('} \n \\centering \n %%opcional \\begin{adjustwidth}{-2cm}{} \n \\begin{tabular}{|*{')
                f.write(str(MAX_COLS))
                f.write('}{c|}}\\hline \n \n')

                for i in range (0,MAX_ROWS,1):
                            for j in range(0, MAX_COLS,1):
                                f.write('\\thead{')
                                f.write(tabela[i][j])
                                f.write('}')
                                if j < MAX_COLS-1:
                                    f.write(' & ')
                            f.write(" \\\\ \\hline \n \n")
                f.write('\\end{tabular} \n \\caption*{Fonte: ')
                f.write(fonte)
                f.write('}')
                f.write('\n %%opcional\end{adjustwidth}{}\n \\label{')
                f.write(label)
                f.write('}\n \\end{table}\n')
                f.write('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            

            with open('tabela.txt','r',encoding='utf-8',) as f:
                conteudo = f.read()
                
            
            
            my_popup(conteudo)
            window.close()
            break

def tabela():
    sg.theme(tema)

    layout = [[sg.Text('Título:'), sg.InputText()],
              [sg.Text('Fonte dos dados:'), sg.InputText()],
              [sg.Text('Rótulo (referência cruzada)'), sg.InputText()],
              [sg.Text('Nº de linhas:'),Push(), sg.Slider(range=(1,25), default_value=1,size=(40,15),orientation='horizontal', font=('Helvetica',11))],
              [sg.Text('Nº de colunas:'), Push(),sg.Slider(range=(1,25), default_value=1,size=(40,15),orientation='horizontal', font=('Helvetica',11))],
              [Push(),sg.Button('Ok'), Push(),sg.Button('Cancelar'),Push()]
              ]
    janela = sg.Window('Dados para construção da tabela', layout, element_justification ='r',return_keyboard_events=True, finalize = True)

    janela.bind('<Return>','Ok')
    janela.bind('<Escape>', 'Cancelar')
    while True:
        event, values = janela.read()
        
        if event in ('Ok'):
            titulo = values[0]
            fonte = values[1]
            label = values[2]
            linhas = values[3]
            colunas = values[4]
            
           
            linhas = int(linhas)
            colunas = int(colunas)
            
            preencher(linhas, colunas, titulo, fonte, label)
            janela.close()
            break
        if event == 'Cancelar' or event == sg.WIN_CLOSED:
            janela.close()
            break

            
###
def janelaInicial():
    sg.theme(tema)

    lembrar = True

    layout_direita =[[Image(filename='icon.gif')]]

    layout_esquerda = [[Push(),sg.Button(('Capa - F1'),size=(10,1)), Push()],
              [Push(),sg.Button(('Tabela - F2'),size=(10,1)),Push()],
              [Push(),sg.Button(('Figura - F3'),size=(10,1)),Push()],
              [Push(),sg.Button(('Sair - Esc'),size=(10,1)),Push()],
               [sg.Text('Desenvolvido por: Lucivaldo Barbosa')]]
    layout = [[Column(layout_esquerda),
              VSeparator(),
              Column (layout_direita)]]


    janelaPrincipal = sg.Window('AutoTeX - Beta', layout, element_justification = 'r',return_keyboard_events=True, finalize = True)

    janelaPrincipal.bind('<F1>', 'F1')
    janelaPrincipal.bind('<F2>', 'F2')
    janelaPrincipal.bind('<F3>', 'F3')
    janelaPrincipal.bind('<Escape>', 'Escape')
    
    
    while True:
        event, values = janelaPrincipal.read()

        if event in ('Capa - F1', 'F1'):
            capa()
        
        elif event in ('Tabela - F2', 'F2'):
            tabela()
    
        elif event in ('Figura - F3', 'F3'):
            figura()

        if event == sg.WIN_CLOSED or event == 'Sair - Esc': 
            break
        elif event == 'Escape':
            janelaPrincipal.close()
            break

def my_popup(contents):
    layout = [
        [sg.Push(), sg.Button('Ok'), sg.Button('Cancelar')],
        [sg.Push(), sg.Text('Copie o seu texto:'),sg.Push()],
        [sg.Multiline(default_text=contents, size=(400, 400), key='-INPUT-')],
        [sg.Push(), sg.Button('Ok'), sg.Push()]
    ]
    window = sg.Window('Texto copiado', layout, element_justification='r', size=(500, 500), return_keyboard_events=True, finalize=True)
    window.bind('<Return>', 'Ok')
    window.bind('<Escape>', 'Ok')

    while True:
        event, values= window.read() 
        if event == 'Ok' or event == 'Cancelar' or event == sg.WIN_CLOSED:
            window.close()
            break

janelaInicial()
