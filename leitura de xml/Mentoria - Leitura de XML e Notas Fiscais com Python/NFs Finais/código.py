import xmltodict

with open(r'C:\Users\joa_o\OneDrive\GitHub\python-impressionador\leitura de xml\Mentoria - Leitura de XML e Notas Fiscais com Python\NFs Finais\DANFEBrota.xml', 'rb') as arquivo:
    documento = xmltodict.parse(arquivo)

dic_nfe = documento['nfeProc']['NFe']['infNFe']
print(dic_nfe)
valor_total = dic_nfe['total']['ICMSTot']['vNF']
cnpj_vendedor = dic_nfe['emit']['CNPJ']
nome_vendedor = dic_nfe['emit']['xNome']
cpf_consumidor = dic_nfe['dest']['CPF']
nome_consumidor = dic_nfe['dest']['xNome']

respostas = {
    'Valor da nota' : valor_total,
    'CNPJ vendedor' : cnpj_vendedor,
    'Nome Fantasia vendedor' : nome_vendedor,
    'CPF consumidor' : cpf_consumidor,
    'Nome consumidor' : nome_consumidor
}

for key, val in respostas.items():
    print(key, val, sep=' -> ')