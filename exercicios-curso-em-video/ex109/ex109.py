import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {n} é {moeda.metade(n, True)}')
print(f'O dobro de {n} é {moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(n, 13, True)}')