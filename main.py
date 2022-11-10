import random
import sys
trouvé = False
tentatives = 0

codesecret = str(input("Entrez code"))
print("°°°°°°°°°°°°°°°°°")
print("°  Patametres   °")
print("°°°°°°°°°°°°°°°°°")
caracteres = int(input("Nombre de digits: "))
grandeur = 10**caracteres-1

print("°°°°°°°°°°°°°°°°°")
print("°    Running    °")
print("°°°°°°°°°°°°°°°°°")

while trouvé == False:
    test = str(random.randint(0,grandeur))
    sys.stdout.write(f"\r{test}")
    tentatives += 1

    if test == codesecret:
        print(f"  <- Trouvé en {tentatives} essais !")
        trouvé = True
