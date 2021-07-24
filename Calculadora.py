from tkinter import *

janela = Tk()
janela.title('Calculadora Simples')

e = Entry(janela, width=35, bg='white', borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# e.insert(0, 'Enter your name: ')
def criar_botao(numero):
    atual = e.get()
    e.delete(0, END)
    e.insert(0, str(atual) + str(numero))

def botao_limpar():
    e.delete(0, END)


def botao_igual():
    segundo_numero = e.get()
    e.delete(0, END)
    if operacao == 'adição':
        e.insert(0, f_num + int(segundo_numero))
    if operacao == 'subtração':
        e.insert(0, f_num - int(segundo_numero))
    if operacao == 'multiplicação':
        e.insert(0, f_num * int(segundo_numero))
    if operacao == 'divisão':
        e.insert(0, f_num / int(segundo_numero))

def botao_adicao():
    primeiro_numero = e.get()
    global f_num
    global operacao
    operacao = 'adição'
    f_num = int(primeiro_numero)
    e.delete(0, END)

def botao_subtracao():
    primeiro_numero = e.get()
    global f_num
    global operacao
    operacao = 'subtracão'
    f_num = int(primeiro_numero)
    e.delete(0, END)

def botao_multiplicacao():
    primeiro_numero = e.get()
    global f_num
    global operacao
    operacao = 'multiplicação'
    f_num = int(primeiro_numero)
    e.delete(0, END)

def botao_divisao():
    first_number = e.get()
    global f_num
    global operacao
    operacao = 'divisão'
    f_num = int(first_number)
    e.delete(0, END)

# Definir botoes
button_1 = Button(janela, text='1', padx=40, pady=20, command=lambda: criar_botao(1))
button_2 = Button(janela, text='2', padx=40, pady=20, command=lambda: criar_botao(2))
button_3 = Button(janela, text='3', padx=40, pady=20, command=lambda: criar_botao(3))
button_4 = Button(janela, text='4', padx=40, pady=20, command=lambda: criar_botao(4))
button_5 = Button(janela, text='5', padx=40, pady=20, command=lambda: criar_botao(5))
button_6 = Button(janela, text='6', padx=40, pady=20, command=lambda: criar_botao(6))
button_7 = Button(janela, text='7', padx=40, pady=20, command=lambda: criar_botao(7))
button_8 = Button(janela, text='8', padx=40, pady=20, command=lambda: criar_botao(8))
button_9 = Button(janela, text='9', padx=40, pady=20, command=lambda: criar_botao(9))
button_0 = Button(janela, text='0', padx=40, pady=20, command=lambda: criar_botao(0))
button_ad = Button(janela, text='+', padx=38, pady=20, command=botao_adicao)
button_subtract = Button(janela, text='-', padx=40, pady=20, command=botao_subtracao)
button_multiply = Button(janela, text='x', padx=40, pady=20, command=botao_multiplicacao)
button_divide = Button(janela, text='/', padx=40, pady=20, command=botao_divisao)
button_equal = Button(janela, text='=', padx=88, pady=20, command=botao_igual)
button_clear = Button(janela, text='Clear', padx=80, pady=20, command=botao_limpar)

#Colocar na tela
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_ad.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=1, column=3)
button_divide.grid(row=2, column=3)
button_equal.grid(row=4, column=1, columnspan=2)

janela.mainloop()