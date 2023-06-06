import  PySimpleGUI as sg

sg.theme('HotDogStand ')

Vini = [
    [sg.Text('IMC')],
    [sg.Text('massa '),sg.Input(key='-MASS-',size=(20,2))],
    [sg.Text('altura '),sg.Input(key='-HIGH-',size=(20,2))],
    [sg.Push(),sg.Button('calcular'),sg.Push()]
]

window = sg.Window('IMC' , layout=Vini ,font='Monaco 18')

while True:
    event, values = window.read()
    print(event,values)
    massa = float(values['-MASS-'])
    altura = float(values['-HIGH-'])
    imc = massa/(altura**2)
    sg.Popup(f'Seu reultado é {imc:.2f}', font='22')
    if event == sg.Win_CLOSED or event == 'QUIT':
      break
