from bibliotecas import estoque, limpar

repeat = "s"
produtos=[]
valorunitario=[]
valortotal=[]
cont=0

while repeat != "x":
    limpar()
    produtos.append(input("Digite o nome do produto: "))
    quantidadeProduto=int(input(f"Digite a quantidade de {produtos[cont]}: "))
    valorunitario.append(float(input(f"Digite o valor unitário de {produtos[cont]}: ").replace(',','.')))

    valortotal.append(estoque(produtos[cont],quantidadeProduto,valorunitario[cont]))

    cont+=1
    repeat=str(input("Deseja continuar? X - parar ").lower())

for i in range(len(produtos)):
    print(f"Produto: {produtos[i]} | unidade: {valorunitario[i]:.2f} | valor total: {valortotal[i]:.2f}")
