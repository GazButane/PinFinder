import random
import sys
import time
trouvé = False
tentatives = 0

print(" ______  _____  ______   ______ _____  ______   _____    ______  ______  ")
print("| |  | \  | |  | |  \ \ | |      | |  | |  \ \ | | \ \  | |     | |  | \ ")
print("| |__|_/  | |  | |  | | | |----  | |  | |  | | | |  | | | |---- | |__| | ")
print("|_|      _|_|_ |_|  |_| |_|     _|_|_ |_|  |_| |_|_/_/  |_|____ |_|  \_\ ")
print("°°°°°°°°°°°°°°°°°")
print("°  Patametres   °")
print("°°°°°°°°°°°°°°°°°")
codesecret = str(input("Entrez code: "))
caracteres = int(input("Nombre de digits: "))
grandeur = 10**caracteres-1
startTime = time.perf_counter()

print("°°°°°°°°°°°°°°°°°")
print("°    Running    °")
print("°°°°°°°°°°°°°°°°°")

while trouvé == False:
    test = str(random.randint(0,grandeur))
    sys.stdout.write(f"\r{test}")
    tentatives += 1

    if test == codesecret:
        endTime = time.perf_counter()
        diff = endTime - startTime
        print("  <- Trouvé !")
        print("°°°°°°°°°°°°°°°°°")
        print("°    Finish!    °")
        print("°°°°°°°°°°°°°°°°°")
        print(f"Trouvé en {tentatives} essais")
        print(f"Temps de calcul: {diff} s")
        trouvé = True
