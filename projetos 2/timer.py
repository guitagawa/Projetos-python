from time import sleep

tempo=int(input('Tempo em segundos:'))

while tempo>=0:
    print(tempo)
    sleep(1)
    tempo-=1

print('tempo acabou')