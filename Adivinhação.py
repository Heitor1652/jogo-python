import random
numero_secreto= random.randint(1,100)
print("ADIVINHE O NÚMERO")
print("tente adivinhar um número de 1 a 100.")
tentativas = 0 
while True:
    palpite= int(input("escolha um número:"))
    tentativas += 1 
    if palpite < numero_secreto:
      print("Tente um número maior...")
    elif palpite > numero_secreto:
      print("tente um número menor...")
    else:
      print("Parabens, você acertou!")
      print("tentativas:", tentativas)
      break
