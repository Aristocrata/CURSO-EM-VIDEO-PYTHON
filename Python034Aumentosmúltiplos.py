s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    a = (11/10)*s
else:
    a = (23/20)*s
print(f'O funcionário passou a ganhar R${a:.2f}')
# na linha 3 e 5 eu simplifiquei as frações 110/100 e 115/100
