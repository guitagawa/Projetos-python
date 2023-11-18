import random

while True:
    print(40*'=')
    letras="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros="0123456789"
    caracteres="~@#$%^&*()_+{}:>?<-=[]\|;,./"
    senha=''

    tamanho=int(input('senha de quantos digitos:'))

    for i in range(tamanho):
        tipo=random.randint(0,2)

        if tipo==0:
            letra=random.choice(letras)
            senha+=letra
        elif tipo==1:
            numero=random.choice(numeros)
            senha+=numero
        else:
            caractere=random.choice(caracteres)
            senha+=caractere

    print(senha)