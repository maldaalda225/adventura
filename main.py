import random

# Globální proměnné
zivoty = 100
sila = 5

def uvod():
    print("\nVítej, dobrodruhu!\n")
    print("Stojíš na rozcestí. Máš čtyři možnosti:")
    print("1. Vstoupit do temného lesa.")
    print("2. Vyrazit na starý hrad.")
    print("3. Jít k tichému jezeru.")
    print("4. Postavit se tajemnému bossovi.")
def boss1():
    global zivoty, sila
    boss_HP = 50
    print("\nVítej, dobrodruhu! Dostals ses do tajné lokace a před tebou stojí strašlivý Morlock!\n")
    while boss_HP > 0 and zivoty > 0:
        print(f"\nTvé životy: {zivoty}, Tvá síla: {sila}, Bossovy životy: {boss_HP}")
        volba = input("Chceš (1) zaútočit nebo (2) se krýt? ")

        if volba == "1":
            utok_hrace = random.randint(5, 10) + sila
            boss_HP -= utok_hrace
            print(f"Zaútočil jsi a způsobil {utok_hrace} poškození!")

            if boss_HP > 0:
                utok_bosse = random.randint(5, 15)
                zivoty -= utok_bosse
                print(f"Boss tě zasáhl a způsobil {utok_bosse} poškození!")

        elif volba == "2":
            obrana = random.randint(1, 10)
            if obrana > 3:
                print("Úspěšně ses kryl a snížil poškození!")
            else:
                utok_bosse = random.randint(5, 15) // 2
                zivoty -= utok_bosse
                print(f"Tvá obrana selhala! Boss ti způsobil {utok_bosse} poškození.")
        else:
            print("Neplatná volba. Boss tě napadl!")
            zivoty -= random.randint(5, 15)

    if zivoty > 0:
        print("\nPorazil jsi bosse! Stal ses hrdinou dne!")
        return 5
    else:
        print("\nBoss tě porazil. Dobrodružství končí.")
        return -1
