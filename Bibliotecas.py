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
    return nome,preco

def posNegNeutro(num):

    if num==0:
        return "Z"
    elif num<0:
        return "N"
    else:
        return "P"

def Soma(num1,num2):
    resultado = num1+num2
    print(f"{num1} + {num2} = {resultado}")

def Soma2(*todosnumeros):
    resultado=0
    for i in range(len(todosnumeros)):
        resultado+=todosnumeros[i]
    print(resultado)

def textoQteInverter(texto):

    textLen = len(texto)

    for i in range(textLen-1,-1,-1):
        print(texto[i],end="")
    print()
    print(textLen)

def verificarRepeticao(lista):
    novaLista=[]
    for i in lista:
        letterAp = 0
        for j in range(0,len(lista)):
            if i == lista[j]:
                letterAp+=1
        if letterAp==1:
            novaLista.append(i)
    print(novaLista)

def novaVerificacao(lista):
    novalista=[]
    for i in lista:
        if i not in novalista:
            novalista.append(i)
    print(novalista)






