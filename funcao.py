import random 

def contraPc():
    print('Você escolheu jogar contra o computador!')
    print('Temos as opções:')
    print('1 - a - pedra')
    print('2 - b - papel')
    print('3 - c - tesoura')
    escolha = input('Informe sua escolha ')
    
    if escolha.lower() == 'a' or escolha.lower() == 'pedra':
        escolha = '1'
    elif escolha.lower() == 'b' or escolha.lower() == 'papel':
        escolha = '2'
    elif escolha.lower() == 'c' or escolha.lower() == 'tesoura':
        escolha = '3'

    escolhaPc = str(random.randint(1,3))
    
    if escolha == escolhaPc:
        print('O jogo empatou')
    elif escolha == '1' and escolhaPc == '3':
        print('Você ganhou!\nParabéns')
    elif escolha == '2' and escolhaPc == '1':
        print('Você ganhou!\nParabéns')
    elif escolha == '3' and escolhaPc == '2':
        print('Você ganhou!\nParabéns')
    elif escolha != '1' or escolha != '2' or escolha != '3':
        print('Escolha inválida')
    else:
        print('O computador venceu\nSinto muito!')
        
def contraPessoa():
    print('Você escolheu jogar contra um colega!')
    print('Informem seus nomes!')
    jogador1 = input('Informe seu nome jogador 1 ')
    jogador2 = input('Informe seu nome jogador 2 ')
    
    print('Temos as opções:')
    print('1 - a - pedra')
    print('2 - b - papel')
    print('3 - c - tesoura')
    
    escolha1 = input(f'{jogador1}, informe sua escolha ')
    
    if escolha1.lower() == 'a' or escolha1.lower() == 'pedra':
        escolha1 = '1'
    elif escolha1.lower() == 'b' or escolha1.lower() == 'papel':
        escolha1 = '2'
    elif escolha1.lower() == 'c' or escolha1.lower() == 'tesoura':
        escolha1 = '3'
        
    escolha2 = input(f'{jogador2}, informe sua escolha ')
    
    if escolha2.lower() == 'a' or escolha2.lower() == 'pedra':
        escolha2 = '1'
    elif escolha2.lower() == 'b' or escolha2.lower() == 'papel':
        escolha2 = '2'
    elif escolha2.lower() == 'c' or escolha2.lower() == 'tesoura':
        escolha2 = '3'
    
    print('---------------------')
    print('Vamos iniciar o jogo')
    print('---------------------')
    
    if (escolha1 == '1' and escolha2 == '3') or (escolha1 == '2' and escolha2 == '1') or (escolha1 == '3' and escolha2 == '2'):
        print(f'{jogador1} venceu!')
    elif (escolha1 == '3' and escolha2 == '1') or (escolha1 == '1' and escolha2 == '2') or (escolha1 == '2' and escolha2 == '3'):
        print(f'{jogador2} venceu!')
    elif escolha1 == escolha2:
        print('O jogo empatou')
         
