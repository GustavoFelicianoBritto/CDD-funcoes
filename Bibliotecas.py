def imprimirNome(nome):
    print(f"olá, {nome}")

def enumerar(qtd):
    for i in range(qtd+1):
        print(f"{i} "*i)

def contadorVogais(texto):
    vogais=["a","e","i","o","u","á","é","í","ó","ú","à","è","ì","ò","ù","â","ê",
            "î","ô","û","ã","õ"]
    qtdVogais = 0
    texto=texto.lower()
    for i in texto:
        if i in vogais:
            qtdVogais+=1
    print(f"A quantidade de letras do texto é: {qtdVogais}")

def estoque(nome,quantidade,valor):
    preco=quantidade*valor
    print(f"O valor total de {nome} no estoque é: {preco}")


