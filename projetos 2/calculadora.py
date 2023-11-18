from time import sleep


print(40*'=')
print('BEM VINDO A MINHA CALCULADORA\nFEITO POR:Guilherme Tagawa')
print(40*'=')

nome=input('Digite seu nome:')
print('Iniciando calculadora...')
sleep(0.5)


print(40 * '=')
print(f'Ola {nome} Calculadora iniciada!')
print(40 * '=')
continua='s'
while continua.lower()=='s':

    
    op=int(input('Digite o NÚMERO da operação desejada \n1-Soma\n2-Subtrção\n3-Divisão\n4-Multiplicaçãp\n5-Potencia\n6-Raiz\n:'))
    if op<1 or op>6:
        print('ERROR 400')
        break
    else:
        num1 = float(input('Digite o primeiro número (base):'))
        if op==6 and num1<0:
            print(40 * '=')
            print('ERROR 401')
            print(40 * '=')
            print('Reiniciando...')
            sleep(0.5)
        else:
            num2=float(input('Digite o segundo número (expoente/índice):'))

            if op==1:
                 print(f'{num1} + {num2} = {num1+num2}')
            elif op==2:
                print(f'{num1} - {num2} = {num1-num2}')
            elif op==3 and num2!=0:
                print(f'{num1} / {num2} = {num1/num2}')
            elif op==4:
                print(f'{num1} * {num2} = {num1*num2}')
            elif op==5:
                print(f'Potencia de {num1} na base {num2} = {num1**num2}')
            elif op==6 and num1>0:
                print(f'raiz de {num1} no índice {num2} = {num1**(1/num2)}')
            else:
                print(40 * '=')
                print('ERROR 402')
                print(40 * '=')
            c=1
            while c==1:
                continua=input('Deseja continuar? (s/n):')
                if continua.lower()=='n':
                    c=0
                elif continua.lower()=='s':
                    c=0
                else:
                    print('EROOR 403')


print(40 * '=')
print('FIM\nOBRIGADO POR USAR MINHA CALCULADORA')
print(40 * '=')







