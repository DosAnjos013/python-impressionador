import tkinter as tk

janela = tk.Tk()

janela.title("Sistema de busca de cotação de moedas") #Definindo o título da janela

mensagem = tk.Label(janela, text="Sistema de busca de cotação de moedas") #Criando objeto Label com o texto "Sistema de busca de cotação de moedas"

mensagem.pack() #Adicionando o rótulo à janela

# para qualquer coisa que for feita dentro da janela, serão necessários os dois passos anteriores.

janela.mainloop()