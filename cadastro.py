from PySimpleGUI import PySimpleGUI as sg

#layout tela
sg.theme('Reddit') #tema

layout =[
    
    [sg.Text("usuario"),sg.Input(key="usuario", size=(20,1))],
    [sg.Text("Senha"),sg.Input(key="senha",password_char="*", size=(20,1))],
    [sg.Checkbox("salvar login?")],
    [sg.Button("Entrar")]
]

#janela

janela = sg.Window("tela de login",layout)

#ler eventos

while True:
   eventos, valores= janela.read()
   if eventos == sg.WINDOW_CLOSED:
       break
   if eventos == "Entrar":
       if valores ["usuario"] == "robert" and valores["senha"] == "12345":
           print("bem vindo ")