import random
import pygame
import sys

# Inicializace Pygame
pygame.init()
screen = pygame.display.set_mode((1900, 1000))
pygame.display.set_caption("Dobrodružná hra")
font = pygame.font.Font(None, 36)
hlavni_hudba = pygame.mixer.Sound("Hudba\hlavni_hudba.mp3")
les_hudba = pygame.mixer.Sound("Hudba\hudba_les.mp3")
hrad_hudba = pygame.mixer.Sound("Hudba\hudba_hrad.mp3")
jezero_hudba = pygame.mixer.Sound("Hudba\hudba_jezero.mp3")
boss_hudba = pygame.mixer.Sound("Hudba\hudba_boss.mp3")
hit_zvuk = pygame.mixer.Sound("Hudba\hit.mp3")

# Barvy
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Globální proměnné
zivoty = 100
sila = 5

def vykresli_text(text, x, y):
    povrch = font.render(text, True, WHITE)
    screen.blit(povrch, (x, y))

def problikni_obrazovku():
    screen.fill(RED)
    pygame.display.flip()
    pygame.time.wait(100)
    screen.fill(BLACK)
    pygame.display.flip()

def boss1():
    global zivoty, sila
    boss_HP = 50
    boss_hudba.play(-1)  # Spustí hudbu pro bosse
    while boss_HP > 0 and zivoty > 0:
        screen.fill(BLACK)
        vykresli_text(f"Tvé životy: {zivoty}, Tvá síla: {sila}, Bossovy životy: {boss_HP}", 20, 20)
        vykresli_text("1. Zaútočit", 20, 60)
        vykresli_text("2. Krýt se", 20, 100)
        pygame.display.flip()

        volba = cekej_na_vstup(["1", "2"])
        if volba == "1":
            utok_hrace = random.randint(5, 10) + sila
            boss_HP -= utok_hrace

            if boss_HP > 0:
                utok_bosse = random.randint(5, 15)
                zivoty -= utok_bosse
                hit_zvuk.play()
                problikni_obrazovku()

        elif volba == "2":
            obrana = random.randint(1, 10)
            if obrana <= 3:
                utok_bosse = random.randint(5, 15) // 2
                zivoty -= utok_bosse
                hit_zvuk.play()
                problikni_obrazovku()

    boss_hudba.stop()  # Zastaví hudbu pro bosse
    if zivoty > 0:
        return 5
    else:
        return -1

def lokace(texty, odmeny, hudba):
    global sila, zivoty
    hudba.play(-1)  # Spustí hudbu pro lokaci
    screen.fill(BLACK)
    vykresli_text(texty[0], 20, 20)
    vykresli_text("1. " + texty[1], 20, 60)
    vykresli_text("2. " + texty[2], 20, 100)
    pygame.display.flip()

    volba = cekej_na_vstup(["1", "2"])
    if volba == "1":
        if random.randint(1, 2) == 1:
            vykresli_text(texty[3], 20, 140)
            sila += odmeny[0]
            zivoty += odmeny[1]
            pygame.display.flip()
            pygame.time.wait(2000)
            hudba.stop()  # Zastaví hudbu pro lokaci
            return odmeny[2]
        else:
            vykresli_text(texty[4], 20, 140)
            pygame.display.flip()
            pygame.time.wait(2000)
            hudba.stop()  # Zastaví hudbu pro lokaci
            return -1
    elif volba == "2":
        vykresli_text(texty[5], 20, 140)
        pygame.display.flip()
        pygame.time.wait(2000)
        hudba.stop()  # Zastaví hudbu pro lokaci
        return odmeny[3]

def les():
    texty = [
        "Vstoupil jsi do temného lesa.",
        "Zaútočit na vlka", "Uprchnout",
        "Porazil jsi vlka a našel amulet síly!",
        "Vlk tě porazil.",
        "Úspěšně ses vyhnul nebezpečí."
    ]
    odmeny = [2, 0, 2, 0]
    return lokace(texty, odmeny, les_hudba)

def hrad():
    texty = [
        "Přicházíš k opuštěnému hradu.",
        "Vstoupit do sklepení", "Odejít pryč",
        "Našel jsi meč síly!",
        "Spadl jsi do pasti.",
        "Odešel jsi pryč."
    ]
    odmeny = [3, 0, 3, 0]
    return lokace(texty, odmeny, hrad_hudba)

def jezero():
    texty = [
        "Dorazil jsi k tichému jezeru.",
        "Vylovit předmět", "Odpočinout si",
        "Vylovil jsi zlatý šperk!",
        "Spadl jsi do vody.",
        "Odpočíváš a užíváš klid."
    ]
    odmeny = [1, 0, 2, 1]
    return lokace(texty, odmeny, jezero_hudba)


def cekej_na_vstup(povolene_volby):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and "1" in povolene_volby:
                    return "1"
                if event.key == pygame.K_2 and "2" in povolene_volby:
                    return "2"
                if event.key == pygame.K_3 and "3" in povolene_volby:
                    return "3"
                if event.key == pygame.K_4 and "4" in povolene_volby:
                    return "4"

def hlavni():
    global zivoty, sila
    body = 0
    hlavni_hudba.play(-1)  # Spustí hlavní hudbu
    while zivoty > 0:
        screen.fill(BLACK)
        vykresli_text(f"Tvé životy: {zivoty}, Tvá síla: {sila}, Body: {body}", 20, 20)
        vykresli_text("Kam chceš jít?", 20, 60)
        vykresli_text("1. Les", 20, 100)
        vykresli_text("2. Hrad", 20, 140)
        vykresli_text("3. Jezero", 20, 180)
        vykresli_text("4. Boss", 20, 220)
        pygame.display.flip()

        cesta = cekej_na_vstup(["1", "2", "3", "4"])
        hlavni_hudba.stop()  # Zastaví hlavní hudbu při vstupu do lokace
        if cesta == "1":
            vysledek = les()
        elif cesta == "2":
            vysledek = hrad()
        elif cesta == "3":
            vysledek = jezero()
        elif cesta == "4":
            vysledek = boss1()

        if vysledek == -1:
            break
        else:
            body += vysledek

    print(f"Dobrodružství končí. Nasbíral jsi {body} bodů.")

if __name__ == "__main__":
    hlavni()
