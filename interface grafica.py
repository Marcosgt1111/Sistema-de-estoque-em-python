from tkinter import *

master = Tk()
master.title("Controle de Estoque")
master.geometry("800x500+310+60")

master.iconbitmap(default = "icones\\sky.ico" )
master.resizable(width=1, height=1)

#Variaveis Globais

# Importar imagens
img_fundo = PhotoImage(file ="imagens\\fundo.png")
img_botao = PhotoImage(file ="imagens\\botao.png")

# Criação de labels

lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

# Criação de caixas de entrada

en_token = Entry(master, bd=2, font=("arial", 15),justify=CENTER)
en_token.place(width=390, height=75, x=42, y=55)


# Criação de botões
bt_entrar = Button(master, bd=0, image=img_botao)
bt_entrar.place(width=245, height=63, x=120, y=400)
master.mainloop()
