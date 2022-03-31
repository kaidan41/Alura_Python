#Formatação Float

from importlib import find_loader

print("Tentativa {} de {}".format(3,10))

"Tentativa {} de {}".format(3,10)

print("Tentativa {1} de {0}".format(2,10))

print("Preço {}".format(1.59))

print("R$ {:f}".format(1.50))

print("R$ {:.2f}".format(1.50))

print("R$ {:.1f}".format(1.50))

print("R$ {:.2f}".format(1234.50))

print("R$ {:7.2f}".format(45.50))

print("R$ {:07.2f}".format(45.50))

print("R$ {:08.2f}".format(45.50))


#Fomatação inteiro

print("R$ {:07d}".format(4))

print("R$ {:7d}".format(46))


#formatação data

print("Data {:2d}/{:2d}".format(9,4))

print("Data {:02d}/{:02d}".format(9,11))


#interpolação de strings com f-strings

nome = 'Matheus'
print(f'Meu nome é {nome}')

nome = 'Matheus'
print(f'Meu nome é {nome.lower()}')


nome = 'Matheus'
print(f'Meu nome é {nome.upper()}')


    













