import random
import sys
import time
trouvé = False
tentatives = 0

print(" ______  _____  ______   ______ _____  ______   _____    ______  ______  ")
print("| |  | \  | |  | |  \ \ | |      | |  | |  \ \ | | \ \  | |     | |  | \ ")
print("| |__|_/  | |  | |  | | | |----  | |  | |  | | | |  | | | |---- | |__| | ")
print("|_|      _|_|_ |_|  |_| |_|     _|_|_ |_|  |_| |_|_/_/  |_|____ |_|  \_\ ")
print("Test the strength of your pin code...")
print(" ")
print("°°°°°°°°°°°°°°°°°")
print("°   Settings    °")
print("°°°°°°°°°°°°°°°°°")
codesecret = str(input("Enter a PIN: "))
caracteres = int(input("Number of digits: "))
grandeur = 10**caracteres-1
tinygrandeur = 10**(caracteres-1)-1
startTime = time.perf_counter()

print("°°°°°°°°°°°°°°°°°")
print("°    Running    °")
print("°°°°°°°°°°°°°°°°°")

while trouvé == False:
    test = str(random.randint(tinygrandeur,grandeur))
    sys.stdout.write(f"\r{test}")
    tentatives += 1

    if test == codesecret:
        endTime = time.perf_counter()
        diff = endTime - startTime
        print("  <- Found !")
        print("°°°°°°°°°°°°°°°°°")
        print("°    Finish!    °")
        print("°°°°°°°°°°°°°°°°°")
        print(f"Found in {tentatives} tries")
        if diff < 60:
            print(f"Calculation time: {diff} s")
        else:
            print(f"Calculation time: {diff/60} min")
        trouvé = True
