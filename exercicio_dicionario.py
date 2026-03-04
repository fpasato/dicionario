# produto = {
#     "nome": "Mouse Gamer",
#     "preco": 150,
#     "estoque": 20,
#     "categoria": "Periféricos"
# }

produto = {}

produto['nome'] = input('Qual o nome do produto? ')
produto["preco"]=float(input('Qual o preço do produto? '))
produto["estoque"]= int(input('Qual a quantidade de produtos? '))
produto["categoria"]= input('Qual a categoria do produto? ')


# for chave, valor in produto.items():
#     print(f'{chave}: {valor}') 

print(produto)
print()
print(f'Produto: {produto["nome"]}')
print(f"Preço: R${produto["preco"]:.2f}")