import xmltodict
import pandas as pd
import numpy as np
import openpyxl

with open(r'C:\Users\joa_o\OneDrive\GitHub\python-impressionador\leitura de xml\Mentoria - Leitura de XML e Notas Fiscais com Python\NFs Finais\DANFEBrota.xml', 'rb') as arquivo:
    documento = xmltodict.parse(arquivo)

dic_nfe = documento['nfeProc']['NFe']['infNFe']
valor_total = dic_nfe['total']['ICMSTot']['vNF']
cnpj_vendedor = dic_nfe['emit']['CNPJ']
nome_vendedor = dic_nfe['emit']['xNome']
cpf_consumidor = dic_nfe['dest']['CPF']
nome_consumidor = dic_nfe['dest']['xNome']
lista_de_produtos = []
respostas = {
    'Valor da nota' : [valor_total],
    'CNPJ vendedor' : [cnpj_vendedor],
    'Nome Fantasia vendedor' : [nome_vendedor],
    'CPF consumidor' : [cpf_consumidor],
    'Nome consumidor' : [nome_consumidor],
    'Produtos' : [lista_de_produtos]
}

'''for key, val in respostas.items():
    print(key, val, sep=' -> ')'''

# verificando o valor e o nome de cada produto na Nota

produtos = dic_nfe['det']
for produto in produtos:
    valor_prod = produto['prod']['vProd']
    nome_prod = produto['prod']['xProd']
    lista_de_produtos.append((nome_prod, valor_prod))
'''
for key, value in respostas.items():
    print( key, value, sep=('->'))'''

tabela = pd.DataFrame.from_dict(respostas)
tabela.to_excel('NFs.xlsx')