import funcao
print('⊹ ࣪ ˖ Bem vindo ao JO-KEN-PÔ ⊹ ࣪ ˖')
print('Temos dois modos de jogo')
print('Jogador SOLO - você contra a máquina')
print('1v1 - você contra seu amigo')

print('Modo 1 - Jogo SOLO')
print('Modo 2 - 1v1')
escolha = input('Qual modo vai jogar? ')

if escolha == '1':
    funcao.contraPc()
elif escolha == '2':
    funcao.contraPessoa()
else:
    print('Opção não encontrada')
