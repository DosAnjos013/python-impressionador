import tkinter as tk

janela = tk.Tk()

janela.rowconfigure(0, weight=1) # Configurando a linha 0 da janela para ter peso 1, permitindo que ela se expanda verticalmente.
janela.columnconfigure([0, 1], weight=1) # Configurando as colunas 0 e 1

janela.title("Sistema de busca de cotação de moedas") #Definindo o título da janela

mensagem = tk.Label(janela, text="Sistema de busca de cotação de moedas", bg="black", fg="white", width=50, height=10) #Criando objeto Label com o texto "Sistema de busca de cotação de moedas"

'''
personalização de altura e largura não é em pixel, é em text unity.

bg: Define a cor de fundo do rótulo (Label). Neste caso, "lightgray" define um fundo cinza claro(background).
fg: Define a cor do texto do rótulo (Label). Neste caso, "black" define o texto em preto (foreground).
'''
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW") # metodo grid() para organizar os widgets em uma grade, especificando a linha e a coluna onde o widget será colocado.

mensagem2 = tk.Label(janela, text="Digite o nome da moeda que deseja consultar a cotação", bg="white", fg="black", width=50, height=10) #Criando objeto Label com o texto "Digite o nome da moeda que deseja consultar a cotação"
mensagem2.grid(row=1, column=0, sticky="NSEW") #Adicionando o rótulo à janela

moeda = tk.Entry()
moeda.grid(row=1, column=1) #Adicionando o campo de entrada à janela

janela.mainloop()