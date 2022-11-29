import PySimpleGUI as sg



def encriptar(text,chave):
    base = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    cripto = ''
    for word in text:
        posicion = base.find(word)
        posicion += chave
        if(posicion > len(base)):
            posicion = posicion - len(base)
        cripto = cripto + base[posicion]
    return cripto

def decriptar(text,chave):
    base = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    cripto = ''
    for word in text:
        posicion = base.find(word)
        posicion -= chave
        if posicion < 0:
            posicion = len(base)- abs(posicion)
        cripto = cripto + base[posicion]
    return cripto
def janela_prinipal():
    sg.theme('DarkBrown1')
    layout = [
        [sg.Text('SEJA BEM VINDOS')],
        [sg.Text('Digite a chave de 0 ate 25:'),
         sg.Input(key='Chave',size=2)],
        [sg.Text('Digite o texto:')],
        [sg.Input(key='Mensagem')],
        [[sg.Button('ENCRIPTAR'),sg.Button('DESNCRIPTAR')]]
    ]
    return sg.Window('SIFRA DE CESAR',layout=layout,finalize=True,size=(1200,600))

def janela_encri():
    txt= values ['Mensagem']
    chv= values ['Chave']
    c=int(chv)
    if c>25:
        c=25

    layout=[
        [sg.Text('TEXTO ENCRIPTOGRAVADO')],
        [sg.Text(f'{encriptar(txt,c)}\n')],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('SIFRA DE CESAR', layout=layout,finalize=True,size=(1200,600))
def janela_desemcri():
    txt= values ['Mensagem']
    chv= values ['Chave']
    if chv==' ':
        chv=0
    c=int(chv)
    if c>25:
        c=25


    layout=[
        [sg.Text('TEXTO DESENCRIPTOGRAVAR')],
        [sg.Text(decriptar(txt,c))],
        [sg.Button('VOLTAR')]
    ]
    return sg.Window('SIFRA DE CESAR', layout=layout,finalize=True,size=(1200,600))

#ordenar todas as janelas
janela1,janela2,janela3=janela_prinipal(),None,None

#janela pricipal
while True:
    window,event,values=sg.read_all_windows()
    #evento fechar

    if window==janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela3 and event == sg.WIN_CLOSED:
        break
    #evento  da janela 1 pra janela 2 ou 3
    if window== janela1 and event == 'ENCRIPTAR':
        janela2 = janela_encri()
        janela1.hide()
    if window== janela2 and event =='VOLTAR':
        janela2.hide()
        janela1.un_hide()

    if window== janela1 and event =='DESNCRIPTAR':
        janela3 = janela_desemcri()
        janela1.hide()
    if window== janela3 and event =='VOLTAR':
        janela3.hide()
        janela1.un_hide()
