# Jogo da forca
import random

des_forca = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |  
    |  
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |  
     | 
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

resp = "SIM"
frutas = ['Kiwi', 'Banana', 'Pessego', 'Abacaxi', 'Acerola', 'Amora', 'Carambola', 'Caju', 'Figo', 'Framboesa', 'Goiaba', 'Jaca', 'Laranja', 'Limao', 'Manga', 'Maracuja', 'Melancia', 'Morango', 'Pera']
animais = ['Elefante', 'Girafa', 'Hipopotamo', 'Leao', 'Macaco', 'Ornitorrinco', 'Rinoceronte', 'Tartaruga', 'Tubarao', 'Zebra']
paises = ['Argentina', 'Brasil', 'Canada', 'Dinamarca', 'Egito', 'Franca', 'Grecia', 'Holanda', 'Italia', 'Japao', 'Noruega', 'Portugal', 'Russia', 'Suecia']
objetos = ['Bicicleta', 'Computador', 'Escova', 'Gaveta', 'Janela', 'Lapis', 'Livro', 'Martelo', 'Mesa', 'Porta', 'Relogio', 'Telefone']
cores = ['Azul', 'Amarelo', 'Branco', 'Cinza', 'Laranja', 'Marrom', 'Preto', 'Rosa', 'Roxo', 'Verde', 'Vermelho']
print("Forca\n")
escolha = int(input("Escolha o Tema\n 1. Frutas\n 2. Animais\n 3. Países\n 4. Objetos\n 5. Cores\n"))
while resp == "SIM":
 acertou = False
 chances = 0
 words = []
 letra = 0
 posicao_letra = 0
 if escolha == 1:
     print(des_forca[chances])
     palavra = frutas[random.randint(0, len(frutas)-1)].upper()
     for letra in range(len(palavra)):
         words.append('_ ')
         if letra == len(palavra)-1:
           print(words[letra], '\n', end="")
         else:
           print(words[letra], end="")

 if escolha == 2:
     print(des_forca[chances])
     palavra = animais[random.randint(0, len(animais)-1)].upper()
     for letra in range(len(palavra)):
         words.append('_ ')
         if letra == len(palavra)-1:
           print(words[letra], '\n', end="")
         else:
           print(words[letra], end="")

 if escolha == 3:
     print(des_forca[chances])
     palavra = paises[random.randint(0, len(paises)-1)].upper()
     for letra in range(len(palavra)):
         words.append('_ ')
         if letra == len(palavra)-1:
           print(words[letra], '\n', end="")
         else:
           print(words[letra], end="")

 if escolha == 4:
     print(des_forca[chances])
     palavra = objetos[random.randint(0, len(objetos)-1)].upper()
     for letra in range(len(palavra)):
         words.append('_ ')
         if letra == len(palavra)-1:
           print(words[letra], '\n', end="")
         else:
           print(words[letra], end="")

 if escolha == 5:
     print(des_forca[chances])
     palavra = cores[random.randint(0, len(cores)-1)].upper()
     for letra in range(len(palavra)):
         words.append('_ ')
         if letra == len(palavra)-1:
           print(words[letra], '\n', end="")
         else:
           print(words[letra], end="")


 acertou = False
 while acertou == False and chances < 6:
     l = input("Letra: ").upper()
     print("\n")
     for posicao_letra in range(len(palavra)):
         if l == palavra[posicao_letra]:
             words[posicao_letra] = l
         if posicao_letra == len(palavra) - 1:
             print(words[posicao_letra], '\n', end="")
         else:
             print(words[posicao_letra], '', end="")
     for posicao_letra in palavra:
         if l in  palavra:
             break
         else:
             chances += 1
             break
     print(des_forca[chances])
     acertou = True
     for i in range(len(words)):
         if words[i] == '_ ':
             acertou = False
     if acertou == True:
         print("Parabéns")
         print("\n")
         resp = str(input("Deseja continuar? <SIM/NÃO>\n")).upper()
         if resp == "SIM":
             escolha = int(input("Escolha o Tema\n 1. Frutas\n 2. Animais\n 3. Países\n 4. Objetos\n 5. Cores\n"))
         else:
             print("Nos vemos outra hora!")
     if acertou == False and chances == 6:
        print(f"Errou!\nPalavra: {palavra}")
        resp = str(input("Deseja continuar? <SIM/NÃO>\n")).upper()
        if resp == "SIM":
            escolha = int(input("Escolha o Tema\n 1. Frutas\n 2. Animais\n 3. Países\n 4. Objetos\n 5. Cores\n"))
        else:
            print("Nos vemos outra hora!")
