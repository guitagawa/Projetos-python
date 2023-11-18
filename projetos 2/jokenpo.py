import random

while True:
    print(40*'=')
    pedra='pedra'
    papel='papel'
    tesoura='tesoura'

    pedra_bot=0
    papel_bot=1
    tesoura_bot=2

    jogador=''

    while jogador!=pedra and jogador!=papel and jogador!=tesoura:
        jogador=input('Escolha uma jogada (pedra,papel,tesoura):')

    bot=random.randint(0,2)

    if bot==pedra_bot:
        print('o bot escolheu pedra')
    elif bot==papel_bot:
        print('o bot escolheu papel')
    elif bot==tesoura_bot:
        print('o bot escolheu tesoura')

    if (jogador==pedra and bot==tesoura_bot) or (jogador==papel and bot==pedra_bot) or (jogador==tesoura and bot==papel_bot):
        print("Você venceu!")
    elif (jogador==pedra and bot==papel_bot) or (jogador==papel and bot==tesoura_bot) or (jogador==tesoura and bot==pedra_bot):
        print('Você perdeu!')
    else:
        print('Empate!')
