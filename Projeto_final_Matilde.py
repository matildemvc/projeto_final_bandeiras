from tkinter import *


azul = "#5A95FC"
vermelho = "#FC5A5A"
amarelo = "#FFE30F"
verde = "#5AFC68"
rosa_claro= "#FFEEFB"
bege="#FDECD0"
cinzento="#C7C7C7"
branco="#FFF7F0"

pagina = Tk()
pagina.title('Quiz de bandeiras')
pagina.geometry('350x500+500+180')
pagina.wm_resizable(width=False, height=False)
pagina.configure(bg=branco)


def limpar_pagina():
    for widget in pagina.winfo_children():
        widget.destroy()

def mostrar_menu_principal():
    limpar_pagina()

    lb_titulo = Label(pagina, text='       Quiz de bandeiras', font='Arial 20 bold', anchor='w', fg=azul, bg=bege)
    lb_titulo.place(width=500, height=100, x=0, y=0)

    button_comecar = Button(pagina, text='Começar', command=mostrar_pagina_comecar, font="Time 16 bold", bg=bege, fg=vermelho)
    button_comecar.place(width=150, height=50, x=95, y=200)

    button_ver = Button(pagina, text='Ver Bandeiras',command=mostrar_pagina_ver_bandeiras, font="Time 16 bold", bg=bege, fg=vermelho)
    button_ver.place(width=150, height=50, x=95, y=270)

def mostrar_pagina_comecar():
    limpar_pagina()
    label = Label(pagina, text='Joga e Aprende', font='Arial 16 bold', bg=branco)
    label.place(width=200, height=50, x=10, y=50)

    botao_voltar= Button(pagina, text='🏠', command= mostrar_menu_principal,bg=bege)
    botao_voltar.place(width=30, height=30, x=290, y=20)

def mostrar_pagina_ver_bandeiras():
    limpar_pagina()
    label = Label(pagina, text='Estuda as Bandeiras', font='Arial 16 bold', bg=branco)
    label.place(width=240, height=50, x=10, y=50)

    botao_voltar = Button(pagina, text='🏠', command=mostrar_menu_principal, bg=bege)
    botao_voltar.place(width=30, height=30, x=290, y=20)

    paises = {
        "Portugal":"Portugal.jpg",
        "Espanha":"Espanha.jpg",
        "França":"França.jpg",
        "Alemanha":"Alemanha.png",
        "Italia":"Italia.png",
        "Reino Unido":"Reino_Unido.png",
        "Estados Unidos":"Estados_Unidos.jpg",
        "Canada":"Canada.jpg",
        "Brasil":"Brasil.jpg",
        "Argentina":"Argentina.jpg",
        "Mexico":"Mexico.jpg",
        "Japao":"Japão.jpg",
        "China":"China.jpg",
        "India":"India.jpg",
        "Coreia do Sul":"Coreia_do_sul.jpg",
        "Australia":"Australia.jpg",
        "Nova Zelandia":"Nova_Zelandia.png",
        "Africa do Sul":"Africa_do_sul.png",
        "Egito":"Egito.png",
        "Nigeria":"Nigeria.jpg",
        "Russia":"Russia.jpg",
        "Ucrania":"Ucrania.png",
        "Turquia":"Turquia.jpg",
        "Grecia":"Grecia.png",
        "Suécia":"Suecia.jpg",
        "Noruega":"Noruega.png",
        "Finlandia":"Finlandia.png",
        "Polónia":"Polonia.png",
        "Paises Baixos":"Paises_baixos.jpg",
        "Suíça":"Suiça.jpg",
        "Angola":"Angola.jpg",
        "Irlanda":"Irlanda.jpg",
        "Armenia":"Armenia.jpg",
        "Peru":"Peru.jpg"
    }

    for pais in paises:
        path = paises[pais]
        imagem = PhotoImage(file=path)

        label_imagem = Label (pagina, bg=bege, image=imagem)
        label_imagem.place(x=85, y=250, width=200, height=400)
        label_imagem.image = imagem

mostrar_menu_principal()

pagina.mainloop()