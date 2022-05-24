ano = int(input('Informe um ano: '))
confira = (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)
# faz uma verificação de 4 em 4 anos, verifica se a cada 100 anos é múltiplo ou não e a cada 400 anos é bissexto...
if(confira):
    print('O ano {} é Bissexto !'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))
