import perdepontos
import forca

print("*********************************")
print("Escolha o seu jogo : "               )
print("*********************************")

print("(1) Forca, (2) Adivinhação}")

jogo = int(input("Escolha o seu jogo favorito: "))

if (jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    perdepontos.jogar()
