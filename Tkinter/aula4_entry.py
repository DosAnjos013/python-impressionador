import tkinter as tk

janela = tk.Tk()

janela.title("Sistema de busca de cotação de moedas") #Definindo o título da janela

mensagem = tk.Label(janela, text="Sistema de busca de cotação de moedas", bg="black", fg="white", width=50, height=10) #Criando objeto Label com o texto "Sistema de busca de cotação de moedas"

'''
personalização de altura e largura não é em pixel, é em text unity.

bg: Define a cor de fundo do rótulo (Label). Neste caso, "lightgray" define um fundo cinza claro(background).
fg: Define a cor do texto do rótulo (Label). Neste caso, "black" define o texto em preto (foreground).
'''
mensagem.pack() #Adicionando o rótulo à janela
# para qualquer coisa que for feita dentro da janela, serão necessários os dois passos anteriores.

mensagem2 = tk.Label(janela, text="Digite o nome da moeda que deseja consultar a cotação", bg="white", fg="black", width=50, height=10) #Criando objeto Label com o texto "Digite o nome da moeda que deseja consultar a cotação"
mensagem2.pack() #Adicionando o rótulo à janela

moeda = tk.Entry()
moeda.pack() #Adicionando o campo de entrada à janela

janela.mainloop()