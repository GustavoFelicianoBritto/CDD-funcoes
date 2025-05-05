def imprimirNome(nome):
    print(f"olá, {nome}")

def enumerar(qtd):
    for i in range(qtd+1):
        print(f"{i} "*i)

def contador(texto):
    vogais=["a","e","i","o","u"]
    qtdVogais = 0

    for i in texto:
        if i in vogais:
            qtdVogais+=1
    print(f"A quantidade de letras do texto é: {qtdVogais}")
