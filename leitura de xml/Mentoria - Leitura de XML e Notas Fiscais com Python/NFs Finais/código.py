import xmltodict
import pandas as pd
import numpy as np
import openpyxl

def le_danfe_xml(nota):
    with open(nota, 'rb') as arquivo:
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
    return respostas

import os

lista_arquivos = os.listdir('Mentoria - Leitura de XML e Notas Fiscais com Python/NFs Finais')

#mandando pro excel
'''tabela = pd.DataFrame.from_dict(respostas)
tabela.to_excel('NFs.xlsx')'''


#leitura de nota de serviço:

def le_xml_servico(nota):
    with open(nota, 'rb') as arquivo:
        documento = xmltodict.parse(arquivo)
    print(documento)

    dic_nfe = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']

    valor_total = dic_nfe['Servico']['Valores']['ValorServicos']
    cnpj_vendedor = dic_nfe['PrestadorServico']['IdentificacaoPrestador']['Cnpj']
    nome_vendedor = dic_nfe['PrestadorServico']['NomeFantasia']
    cpf_consumidor = dic_nfe['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']
    nome_consumidor = dic_nfe['TomadorServico']['RazaoSocial']
    servicos = dic_nfe['Servico']['Discriminacao']

    respostas = {
        'Valor da nota' : [valor_total],
        'CNPJ vendedor' : [cnpj_vendedor],
        'Nome Fantasia vendedor' : [nome_vendedor],
        'CPF consumidor' : [cpf_consumidor],
        'Nome consumidor' : [nome_consumidor],
        'Serviços' : [servicos]
    }

    return respostas

# verificando arquivos xml de tipos diferentes

for arquivo in lista_arquivos:
    if 'xml' in arquivo:
        if 'DANFE' in arquivo:
           print('DANFE:')
           print(le_danfe_xml(f'Mentoria - Leitura de XML e Notas Fiscais com Python/NFs Finais/{arquivo}'))
        else:
            print('SERVIÇO:')
            print(le_xml_servico)

