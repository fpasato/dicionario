produto = {
    "nome": "Mouse Gamer",
    "preco": 150,
    "estoque": 20,
    "categoria": "Periféricos"
}

print(produto)

for chave, valor in produto.items():
    print(f'{chave}: {valor}') 