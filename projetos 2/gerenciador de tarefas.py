lista=[]
continua='s'

while continua.lower()=='s':
    print(40*'=')
    print('O que deseja fazer?')
    print('1-Adicionar um item na lista')
    print('2-remover um item da lista')
    escolha=int(input('Escolha: '))


    if escolha==1:
        item=input('Item para adicionar na lista:')
        lista.append(item)
    elif escolha==2:
        item=input('Item para remover da lista:')

        if item in lista:
            lista.remove(item)
        else:
            print('\nEste item não está na lista\n')
            continue
    else:
       continue

    print(f'\n{lista}\n')
    continua=input('Deseja continuar? (s/n)')

print(f'\nLista final: {lista}\n')

