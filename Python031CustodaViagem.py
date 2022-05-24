d = int(input('De quantos Km será sua viagem? '))
print('O custo da sua viagem será de {:.2f}R$.'.format(d*0.45) if d > 200 else 'O custo da sua viagem será de {:.2f}R$.'.format(d*0.5))
