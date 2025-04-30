# Créé par charlinesznajderman, le 08/04/2024 en Python 3.7
import pygame
import time
import random
import os

pygame.init()

nbr = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}

calculatrice_dico = {'0' : False, '1' : False, '2' : False, '3' : False, '4' : False, '5' : False, '6' : False, '7' : False,
'8' : False, '9' : False, 'division' : False, 'multiplication' : False, 'soustraction' : False, 'addition' : False, 'EXE' : False, 'RESET' : False}

screen = pygame.display.set_mode((1000, 600))
first_wallpaper = True
calculatrice_wallpaper = False
minuteur_wallpaper = False
minuteur_wallpaper2 = False
chifoumi_wallpaper = False
horloge_wallpaper = False
horloge_wallpaper2 = False


def sauvegarder_variable(valeur):
    with open("variable.txt", "w") as fichier:
        fichier.write(str(valeur))
def charger_variable():
    if os.path.exists("variable.txt"):
        with open("variable.txt", "r") as fichier:
            contenu = fichier.read()
            return int(contenu) if contenu else 0
    else:
        return 0

nbr_coin = charger_variable()

victoire_J = False

y = 150
x = 200

heure = 0
minute = 0
seconde = 0


white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    title = pygame.font.SysFont('Courier', 40)
    reset = pygame.font.SysFont('Courier', 30)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        print(mouse_x, mouse_y)
        time.sleep(0.25)


    if key[pygame.K_SPACE]:
        pygame.quit()
        break

    if first_wallpaper:
        score_J = 0
        score_O = 0

        screen.blit(title.render("HelloWorld", False, (255, 0, 255)), (375, 50))

        minuteur_button = pygame.draw.rect(screen, (255, 255, 255), (350, 175, 290, 50))
        if minuteur_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.ellipse(screen, (255, 0, 0), (300, 185, 30, 30))
        calculatrice_button = pygame.draw.rect(screen, (255, 255, 255), (350, 275, 290, 50))
        if calculatrice_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.ellipse(screen, (255, 0, 0), (300, 285, 30, 30))
        chifoumi_button = pygame.draw.rect(screen, (255, 255, 255), (350, 375, 290, 50))
        if chifoumi_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.ellipse(screen, (255, 0, 0), (300, 385, 30, 30))
        horloge_button = pygame.draw.rect(screen, (255, 255, 255), (350, 475, 290, 50))
        if horloge_button.collidepoint(mouse_x, mouse_y):
            pygame.draw.ellipse(screen, (255, 0, 0), (300, 485, 30, 30))

        screen.blit(title.render("en travaux", False, (0, 0, 0)), (375, 275))
        screen.blit(title.render("minuteur", False, (0, 0, 0)), (400, 175))
        screen.blit(title.render("chifoumi", False, (0, 0, 0)), (400, 375))
        screen.blit(title.render("horloge", False, (0, 0, 0)), (400, 475))

        if calculatrice_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            time.sleep(0.25)
            first_wallpaper = False
            calculatrice_wallpaper = True
        if chifoumi_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            time.sleep(0.125)
            first_wallpaper = False
            time.sleep(0.125)
            chifoumi_wallpaper = True
        if minuteur_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            time.sleep(0.25)
            first_wallpaper = False
            minuteur_wallpaper = True
        if horloge_button.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            time.sleep(0.25)
            first_wallpaper = False
            horloge_wallpaper = True

    if minuteur_wallpaper:

        screen.blit(title.render(str(heure), False, (255, 255, 255)), (250, 275))
        screen.blit(title.render("h", False, (255, 255, 255)), (250, 100))
        reset_h = pygame.draw.rect(screen, (255, 255, 255), (225, 500, 90, 40))
        screen.blit(reset.render("RESET", False, (255, 0, 0)), (225, 505))
        if reset_h.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            heure = 0

        screen.blit(title.render(str(minute), False, (255, 255, 255)), (500, 275))
        screen.blit(title.render("m", False, (255, 255, 255)), (500, 100))
        reset_m = pygame.draw.rect(screen, (255, 255, 255), (475, 500, 90, 40))
        screen.blit(reset.render("RESET", False, (255, 0, 0)), (475, 505))
        if reset_m.collidepoint(mouse_x, mouse_y) and pygame and pygame.mouse.get_pressed()[0]:
            minute = 0

        screen.blit(title.render(str(seconde), False, (255, 255, 255)), (750, 275))
        screen.blit(title.render("s", False, (255, 255, 255)), (750, 100))
        reset_s = pygame.draw.rect(screen, (255, 255, 255), (725, 500, 90, 40))
        screen.blit(reset.render("RESET", False, (255, 0, 0)), (725, 505))
        if reset_s.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            seconde = 0

        heure_p = pygame.draw.rect(screen, (255, 255, 255), (242.5, 350, 40, 40))
        screen.blit(title.render("+", False, (0, 0, 0)), (250, 350))
        heure_m = pygame.draw.rect(screen, (255, 255, 255), (242.5, 200, 40, 40))
        screen.blit(title.render("-", False, (0, 0, 0)), (250, 200))

        ok = pygame.draw.rect(screen, (255, 255, 255), (900, 275, 50, 50))
        screen.blit(title.render("ok", False, (0, 0, 0)), (900, 275))

        minute_p = pygame.draw.rect(screen, (255, 255, 255), (492.5, 350, 40, 40))
        screen.blit(title.render("+", False, (0, 0, 0)), (500, 350))
        minute_m = pygame.draw.rect(screen, (255, 255, 255), (492.5, 200, 40, 40))
        screen.blit(title.render("-", False, (0, 0, 0)), (500, 200))

        seconde_p = pygame.draw.rect(screen, (255, 255, 255), (742.5, 350, 40, 40))
        screen.blit(title.render("+", False, (0, 0, 0)), (750, 350))
        seconde_m = pygame.draw.rect(screen, (255, 255, 255), (742.5, 200, 40, 40))
        screen.blit(title.render("-", False, (0, 0, 0)), (750, 200))

        quit = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 75, 35))
        screen.blit(reset.render("QUIT", False, (0, 0, 0)), (0, 0))
        if quit.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minuteur_wallpaper = False
            first_wallpaper = True

        if heure_p.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            heure += 1
            time.sleep(0.1)
            if heure > 24:
                heure -= 1
        if heure_m.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            heure -= 1
            time.sleep(0.1)
            if heure < 0:
                heure += 1

        if minute_p.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minute += 1
            time.sleep(0.1)
            if minute > 60:
                minute -= 1
        if minute_m.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minute -= 1
            time.sleep(0.1)
            if minute < 0:
                minute += 1

        if seconde_p.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            seconde += 1
            time.sleep(0.1)
            if seconde > 60:
                seconde -= 1
        if seconde_m.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            seconde -= 1
            time.sleep(0.1)
            if seconde < 0:
                seconde += 1

        if ok.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minuteur_wallpaper = False
            minuteur_wallpaper2 = True

    if minuteur_wallpaper2:

        #quit = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 75, 35))
        #screen.blit(reset.render("QUIT", False, (0, 0, 0)), (0, 0))
        if quit.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minuteur_wallpaper2 = False
            first_wallpaper = True

        screen.blit(title.render(str(heure), False, (255, 255, 255)), (250, 275))
        screen.blit(title.render(str(minute), False, (255, 255, 255)), (500, 275))
        screen.blit(title.render(str(seconde), False, (255, 255, 255)), (750, 275))
        screen.blit(title.render("h", False, (255, 255, 255)), (250, 100))
        screen.blit(title.render("m", False, (255, 255, 255)), (500, 100))
        screen.blit(title.render("s", False, (255, 255, 255)), (750, 100))
        if seconde > 0:
                seconde -= 1
                time.sleep(1)
        if seconde == 0 and minute != 0:
            seconde = 59
            minute -= 1
        if heure < 0:
            heure += 1
        if minute == 0 and seconde == 0 and heure != 0:
            minute = 59
            seconde = 59
            heure -= 1
        if heure == 0 and minute == 0 and seconde == 0:
            minuteur_wallpaper2 = False
            first_wallpaper = True


    if calculatrice_wallpaper:

            screen.blit(reset.render("(MAXIMUM 100)", False, (255, 255, 255)), (370, 20))

            quit = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 75, 35))
            screen.blit(reset.render("QUIT", False, (0, 0, 0)), (0, 0))
            if quit.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                first_wallpaper = True
                calculatrice_wallpaper = False


            if key[pygame.K_DOWN]:
                print(calculatrice_dico)
                print(nbr)
                time.sleep(0.5)

            rect_1 = pygame.draw.rect(screen, (255, 255, 255), (x, y, 175, 30))
            if rect_1.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['1'] = True

            rect_2 = pygame.draw.rect(screen, (255, 255, 255), (x, y + 35, 175, 30))
            if rect_2.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['2'] = True

            rect_3 = pygame.draw.rect(screen, (255, 255, 255), (x, y + 70, 175, 30))
            if rect_3.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['3'] = True
                if calculatrice_dico['3']:
                    print(calculatrice_dico)
                    time.sleep(0.5)

            rect_RESET = pygame.draw.rect(screen, (255, 255, 255), (x, y + 140, 175, 30))
            if rect_RESET.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['RESET'] = True
                if calculatrice_dico['RESET']:
                    for valeur in calculatrice_dico.values():
                        valeur = False
                    print(calculatrice_dico)

            rect_4 = pygame.draw.rect(screen, (255, 255, 255), (x + 180, y, 175, 30))
            if rect_4.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['4'] = True

            rect_5 = pygame.draw.rect(screen, (255, 255, 255), (x + 180, y + 35, 175, 30))
            if rect_5.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['5'] = True

            rect_6 = pygame.draw.rect(screen, (255, 255, 255), (x + 180, y + 70, 175, 30))
            if rect_6.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['6'] = True

            rect_0 = pygame.draw.rect(screen, (255, 255, 255), (x + 180, y + 140, 175, 30))
            if rect_0.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['0'] = True

            pygame.draw.rect(screen, (255, 255, 255), (x + 180, y + 105, 175, 30)) #decor

            rect_7 = pygame.draw.rect(screen, (255, 255, 255), (x + 360, y, 175, 30))
            if rect_7.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['7'] = True

            rect_8 = pygame.draw.rect(screen, (255, 255, 255), (x + 360, y + 35, 175, 30))
            if rect_8.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['8'] = True

            rect_9 = pygame.draw.rect(screen, (255, 255, 255), (x + 360, y + 70, 175, 30))
            if rect_9.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['9'] = True

            rect_EXE = pygame.draw.rect(screen, (255, 255, 255), (x + 360, y + 140, 175, 30))
            if rect_EXE.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['EXE'] = True

            rect_addition = pygame.draw.rect(screen, (255, 255, 255), (x + 540, y, 125, 30))
            if rect_addition.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['addition'] = True

            rect_soustraction = pygame.draw.rect(screen, (255, 255, 255), (x + 540, y + 35, 125, 30))
            if rect_soustraction.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['soustraction'] = True

            rect_division = pygame.draw.rect(screen, (255, 255, 255), (x + 540, y + 70, 125, 30))
            if rect_division.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['division'] = True

            rect_multiplication = pygame.draw.rect(screen, (255, 255, 255), (x + 540, y + 105, 125, 30))
            if rect_multiplication.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
                calculatrice_dico['multiplication'] = True

#            if calculatrice_dico['addition'] == True or calculatrice_dico['soustraction'] == True or calculatrice_dico['division'] == True or calculatrice_dico['multiplication'] == True:


            screen.blit(title.render("1", False, (0, 0, 0)), (275, 145))
            screen.blit(title.render("2", False, (0, 0, 0)), (275, 180))
            screen.blit(title.render("3", False, (0, 0, 0)), (275, 215))
            screen.blit(title.render("4", False, (0, 0, 0)), (455, 145))
            screen.blit(title.render("5", False, (0, 0, 0)), (455, 180))
            screen.blit(title.render("6", False, (0, 0, 0)), (455, 215))
            screen.blit(title.render("0", False, (0, 0, 0)), (455, 250))
            screen.blit(title.render("7", False, (0, 0, 0)), (635, 145))
            screen.blit(title.render("8", False, (0, 0, 0)), (635, 180))
            screen.blit(title.render("9", False, (0, 0, 0)), (635, 215))

            diviser = pygame.font.SysFont('Courier', 30)
            screen.blit(title.render("+", False, (0, 0, 0)), (786, 145))
            screen.blit(title.render("-", False, (0, 0, 0)), (786, 180))
            screen.blit(diviser.render("/", False, (0, 0, 0)), (790, 220))
            screen.blit(title.render("*", False, (0, 0, 0)), (786, 250))

            screen.blit(title.render("EXE", False, (0, 0, 0)), (610, 282.5))
            screen.blit(title.render("RESET", False, (0, 0, 0)), (225, 282.5))

    if chifoumi_wallpaper:

        quit = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 75, 35))
        screen.blit(reset.render("QUIT", False, (0, 0, 0)), (0, 0))
        if quit.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            first_wallpaper = True
            chifoumi_wallpaper = False

        screen.blit(reset.render("ORDI", False, (0, 0, 255)), (470, 240)) #signeOrdi
        screen.blit(title.render(str(score_O), False, (0, 0, 255)), (400, 235))
        screen.blit(reset.render("JOUEUR", False, (0, 0, 255)), (450, 360)) #signeJoueur
        screen.blit(title.render(str(score_J), False, (0, 0, 255)), (590, 355))

        O = ["feuille", "ciseau", "pierre"]
        Jpierre_colour = white
        Jfeuille_colour = white
        Jciseau_colour = white
        Opierre_colour = white
        Ofeuille_colour = white
        Ociseau_colour = white

        screen.blit(reset.render("PIERRE", False, (255, 255, 255)), (200, 300))
        screen.blit(reset.render("FEUILLE", False, (255, 255, 255)), (450, 300))
        screen.blit(reset.render("CISEAU", False, (255, 255, 255)), (700, 300))
        screen.blit(reset.render("VEUILLEZ CLIQUER SUR VOTRE CHOIX", False, (255, 0, 255)), (220, 20))

        pierre_o = pygame.draw.rect(screen, (255, 255, 255), (220, 90, 70, 125))
        feuille_o = pygame.draw.rect(screen, (255, 255, 255), (470, 90, 70, 125))
        ciseau_o = pygame.draw.rect(screen, (255, 255, 255), (720, 90, 70, 125))
        pierre_j = pygame.draw.rect(screen, (255, 255, 255), (220, 410, 70, 125))
        feuille_j = pygame.draw.rect(screen, (255, 255, 255), (470, 410, 70, 125))
        ciseau_j = pygame.draw.rect(screen, (255, 255, 255), (720, 410, 70, 125))

        O_choice = random.choice(O)

        if pierre_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] or feuille_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] or ciseau_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:


            if pierre_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "pierre":  #toutes les combinaisons pour pierre et joueur
                screen.blit(reset.render("EGALITE", False, (255, 255, 255)), (450, 550))
                pygame.display.flip()
                time.sleep(0.8)

            if pierre_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "feuille":
                feuille_o = pygame.draw.rect(screen, (0, 255, 0), (470, 90, 70, 125))
                screen.blit(reset.render("VICTOIRE ORDI", False, (255, 255, 255)), (400, 550))
                pygame.display.flip()
                time.sleep(0.8)
                score_O += 1

            if pierre_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "ciseau":
                pierre_j = pygame.draw.rect(screen, (0, 255, 0), (220, 410, 70, 125))
                screen.blit(reset.render("VICTOIRE JOUEUR", False, (255, 255, 255)), (375, 550))
                pygame.display.flip()
                time.sleep(0.8)
                score_J += 1


            if feuille_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "feuille": #combinaisons pour joueurs et feuille
                screen.blit(reset.render("EGALITE", False, (255, 255, 255)), (450, 550))
                pygame.display.flip()
                time.sleep(0.8)

            if feuille_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "ciseau":
                feuille_o = pygame.draw.rect(screen, (0, 255, 0), (470, 90, 70, 125))
                screen.blit(reset.render("VICTOIRE ORDI", False, (255, 255, 255)), (400, 550))
                pygame.display.flip()
                time.sleep(0.8)
                score_O += 1

            if feuille_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "pierre":
                feuille_j = pygame.draw.rect(screen, (0, 255, 0), (470, 410, 70, 125))
                screen.blit(reset.render("VICTOIRE JOUEUR", False, (255, 255, 255)), (375, 550))
                pygame.display.flip()
                time.sleep(0.8)
                score_J += 1


            if ciseau_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "ciseau": #combinaisons pour joueur et ciseau
                screen.blit(reset.render("EGALITE", False, (255, 255, 255)), (450, 550))
                pygame.display.flip()
                time.sleep(0.8)

            if ciseau_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "pierre":
                pierre_o = pygame.draw.rect(screen, (0, 255, 0), (220, 90, 70, 125))
                screen.blit(reset.render("VICTOIRE ORDI", False, (255, 255, 255)), (400, 550))
                pygame.display.flip()
                time.sleep(0.8)
                score_O += 1

            if ciseau_j.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0] and O_choice == "feuille":
                ciseau_j = pygame.draw.rect(screen, (0, 255, 0), (720, 410, 70, 125))
                screen.blit(reset.render("VICTOIRE JOUEUR", False, (255, 255, 255)), (400, 550))
                pygame.display.flip()
                time.sleep(0.8)
                score_J += 1

            if score_O == 10:
                screen.fill((0, 0, 0))
                screen.blit(title.render("L'ORDI A GAGNE LA PARTIE", False, (255, 255, 255)), (200, 300))
                pygame.display.flip()
                time.sleep(2.5)
                chifoumi_wallpaper = False
                first_wallpaper = True

            if score_J == 10:
                victoire_J = True

            if victoire_J == True:
                screen.fill((0, 0, 0))
                screen.blit(title.render("LE JOUEUR A GAGNE LA PARTIE", False, (255, 255, 255)), (200, 300))
                pygame.display.flip()
                time.sleep(2.5)
                chifoumi_wallpaper = False
                first_wallpaper = True
                victoire_J = False


    if horloge_wallpaper:

        screen.blit(title.render(str(heure), False, (255, 255, 255)), (250, 275))
        screen.blit(title.render("h", False, (255, 255, 255)), (250, 100))
        reset_h = pygame.draw.rect(screen, (255, 255, 255), (225, 500, 90, 40))
        screen.blit(reset.render("RESET", False, (255, 0, 0)), (225, 505))
        if reset_h.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            heure = 0

        screen.blit(title.render(str(minute), False, (255, 255, 255)), (500, 275))
        screen.blit(title.render("m", False, (255, 255, 255)), (500, 100))
        reset_m = pygame.draw.rect(screen, (255, 255, 255), (475, 500, 90, 40))
        screen.blit(reset.render("RESET", False, (255, 0, 0)), (475, 505))
        if reset_m.collidepoint(mouse_x, mouse_y) and pygame and pygame.mouse.get_pressed()[0]:
            minute = 0

        screen.blit(title.render(str(seconde), False, (255, 255, 255)), (750, 275))
        screen.blit(title.render("s", False, (255, 255, 255)), (750, 100))
        reset_s = pygame.draw.rect(screen, (255, 255, 255), (725, 500, 90, 40))
        screen.blit(reset.render("RESET", False, (255, 0, 0)), (725, 505))
        if reset_s.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            seconde = 0

        heure_p = pygame.draw.rect(screen, (255, 255, 255), (242.5, 350, 40, 40))
        screen.blit(title.render("+", False, (0, 0, 0)), (250, 350))
        heure_m = pygame.draw.rect(screen, (255, 255, 255), (242.5, 200, 40, 40))
        screen.blit(title.render("-", False, (0, 0, 0)), (250, 200))

        ok = pygame.draw.rect(screen, (255, 255, 255), (900, 275, 50, 50))
        screen.blit(title.render("ok", False, (0, 0, 0)), (900, 275))

        minute_p = pygame.draw.rect(screen, (255, 255, 255), (492.5, 350, 40, 40))
        screen.blit(title.render("+", False, (0, 0, 0)), (500, 350))
        minute_m = pygame.draw.rect(screen, (255, 255, 255), (492.5, 200, 40, 40))
        screen.blit(title.render("-", False, (0, 0, 0)), (500, 200))

        seconde_p = pygame.draw.rect(screen, (255, 255, 255), (742.5, 350, 40, 40))
        screen.blit(title.render("+", False, (0, 0, 0)), (750, 350))
        seconde_m = pygame.draw.rect(screen, (255, 255, 255), (742.5, 200, 40, 40))
        screen.blit(title.render("-", False, (0, 0, 0)), (750, 200))

        quit = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 75, 35))
        screen.blit(reset.render("QUIT", False, (0, 0, 0)), (0, 0))
        if quit.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            horloge_wallpaper = False
            first_wallpaper = True

        if heure_p.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            heure += 1
            time.sleep(0.1)
            if heure > 24:
                heure = 0
        if heure_m.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            heure -= 1
            time.sleep(0.1)
            if heure < 0:
                heure = 24

        if minute_p.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minute += 1
            time.sleep(0.1)
            if minute > 60:
                minute = 0
        if minute_m.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minute -= 1
            time.sleep(0.1)
            if minute < 0:
                minute = 60

        if seconde_p.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            seconde += 1
            time.sleep(0.1)
            if seconde > 60:
                seconde = 0
        if seconde_m.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            seconde -= 1
            time.sleep(0.1)
            if seconde < 0:
                seconde = 60

        if ok.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            horloge_wallpaper = False
            horloge_wallpaper2 = True

    if horloge_wallpaper2:

            #quit = pygame.draw.rect(screen, (255, 0, 0), (0, 0, 75, 35))
            #screen.blit(reset.render("QUIT", False, (0, 0, 0)), (0, 0))
        if quit.collidepoint(mouse_x, mouse_y) and pygame.mouse.get_pressed()[0]:
            minuteur_wallpaper2 = False
            first_wallpaper = True

        screen.blit(title.render(str(heure), False, (255, 255, 255)), (250, 275))
        screen.blit(title.render(str(minute), False, (255, 255, 255)), (500, 275))
        screen.blit(title.render(str(seconde), False, (255, 255, 255)), (750, 275))
        screen.blit(title.render("h", False, (255, 255, 255)), (250, 100))
        screen.blit(title.render("m", False, (255, 255, 255)), (500, 100))
        screen.blit(title.render("s", False, (255, 255, 255)), (750, 100))
        if seconde < 59:
            seconde += 1
            time.sleep(1)
        if seconde == 59:
            seconde = 0
            minute += 1
        if heure < 0:
            heure += 1
        if minute == 59 and seconde == 59:
            minute = 0
            seconde = 0
            heure += 1
        if heure == 24 and minute == 59 and seconde == 59:
            minuteur_wallpaper2 = False
            first_wallpaper = True


    pygame.display.flip()


pygame.quit()
