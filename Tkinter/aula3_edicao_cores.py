import tkinter as tk

janela = tk.Tk()

janela.title("Sistema de busca de cotação de moedas") #Definindo o título da janela

mensagem = tk.Label(janela, text="Sistema de busca de cotação de moedas", bg="lightgray", fg="black") #Criando objeto Label com o texto "Sistema de busca de cotação de moedas"

'''
bg: Define a cor de fundo do rótulo (Label). Neste caso, "lightgray" define um fundo cinza claro (background).
fg: Define a cor do texto do rótulo (Label). Neste caso, "black" define o texto em preto (foreground).
'''


mensagem.pack() #Adicionando o rótulo à janela

# para qualquer coisa que for feita dentro da janela, serão necessários os dois passos anteriores.

janela.mainloop()