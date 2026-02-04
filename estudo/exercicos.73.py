times=('Athletico Paranaense', 'Atlético-MG','Bahia','Botafogo','Chapecoense',
'Corinthians','Coritiba', 'Cruzeiro','Flamengo','Fluminense','Grêmio',
'Internacional','Mirassol','Palmeiras','Red Bull Bragantino','Remo ','Santos',
'São Paulo','Vasco da Gama','Vitória')

print('Deseja ver os 5 primeiros da tabela? Digite 1.')
print('Deseja ver os 5 últimos da tabela? Digite 2.')

while True:
    nume=int(input('Opção desejada:'))
    if 1<=nume<=2:
        break
        print('Nenhuma das opçôes foi selecionado!', end='')
    # elif nume=1:
    #     a=(times[0:5])
    
        
    
print(f'O numero digitado foi {times[nume]}')