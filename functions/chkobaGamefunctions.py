import itertools
import os
import random
import time
from datetime import date

from packages import *

# Setting the color combinations
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


def quit_game():
    choice = input("Type (q) to quit, Type other to return to menu ==> ")
    if choice.lower() == "q":
        print(BOLD, GREEN, "See You Again - CARVA5AL STUDIO ")
        time.sleep(3.5)
        exit()
    else:
        os.system("clear")
        choice = create_Menu_welcome()
    return choice


def show_historique():
    f = open("historique.txt", "r")
    i = 1
    for x in f:
        print(BOLD, GREEN, i, "- ", x)
        i = i + 1
    input("Press enter to show the menu... ")
    os.system("clear")
    choice = create_Menu_welcome()
    return choice


def show_combinations(cards, length, summ):
    L = []
    # generate all possible combinations of the input list
    combinations = list(itertools.combinations(cards, length))
    # print out each combination whose sum equals 9
    if length == 1:
        for combo in combinations:
            if combo[0].value == summ:
                L.append(combo)
    else:
        for combo in combinations:
            s = 0
            for i in combo:
                s = s + i.value
            if s == summ:
                L.append(combo)
    return L


def create_cards_list():
    # cards de type coeur
    c1 = card.Card("1 ♥", 1)
    c2 = card.Card("2 ♥", 2)
    c3 = card.Card("3 ♥", 3)
    c4 = card.Card("4 ♥", 4)
    c5 = card.Card("5 ♥", 5)
    c6 = card.Card("6 ♥", 6)
    c7 = card.Card("7 ♥", 7)
    c8 = card.Card("8 ♥", 8)
    c9 = card.Card("9 ♥", 9)
    c10 = card.Card("10 ♥", 10)

    # cards de type carreau
    cr1 = card.Card("1 ♦", 1)
    cr2 = card.Card("2 ♦", 2)
    cr3 = card.Card("3 ♦", 3)
    cr4 = card.Card("4 ♦", 4)
    cr5 = card.Card("5 ♦", 5)
    cr6 = card.Card("6 ♦", 6)
    cr7 = card.Card("7 ♦", 7)
    cr8 = card.Card("8 ♦", 8)
    cr9 = card.Card("9 ♦", 9)
    cr10 = card.Card("10 ♦", 10)

    # cards de type bermila
    b1 = card.Card("1 ♠", 1)
    b2 = card.Card("2 ♠", 2)
    b3 = card.Card("3 ♠", 3)
    b4 = card.Card("4 ♠", 4)
    b5 = card.Card("5 ♠", 5)
    b6 = card.Card("6 ♠", 6)
    b7 = card.Card("7 ♠", 7)
    b8 = card.Card("8 ♠", 8)
    b9 = card.Card("9 ♠", 9)
    b10 = card.Card("10 ♠", 10)

    # cards de type dheben
    d1 = card.Card("1 ♣", 1)
    d2 = card.Card("2 ♣", 2)
    d3 = card.Card("3 ♣", 3)
    d4 = card.Card("4 ♣", 4)
    d5 = card.Card("5 ♣", 5)
    d6 = card.Card("6 ♣", 6)
    d7 = card.Card("7 ♣", 7)
    d8 = card.Card("8 ♣", 8)
    d9 = card.Card("9 ♣", 9)
    d10 = card.Card("10 ♣", 10)

    list_cartes = [
        c1,
        c2,
        c3,
        c4,
        c5,
        c6,
        c7,
        c8,
        c9,
        c10,
        cr1,
        cr2,
        cr3,
        cr4,
        cr5,
        cr6,
        cr7,
        cr8,
        cr9,
        cr10,
        b1,
        b2,
        b3,
        b4,
        b5,
        b6,
        b7,
        b8,
        b9,
        b10,
        d1,
        d2,
        d3,
        d4,
        d5,
        d6,
        d7,
        d8,
        d9,
        d10,
    ]
    return list_cartes


def create_Menu_welcome():
    print(BOLD, GREEN, " Welcome to the best game ever ")
    print(BOLD, GREEN, " Today we will play Tunisian Chkoba ")
    print(" ------------- MENU ------------- ")
    print(" 1- Start new game")
    print(" 2- Best scores ")
    print(" 3- Quit")
    print(" ------------- Carva5al gaming studio ------------- ", RESET)
    # time.sleep(2)
    choice = input(" Write here your choice ")
    return choice


def create_menu_custom_game():
    print(" ------------- customize your game ------------- ")
    nbrG = 0
    new_game = game.Game([], 0, 0)
    print(BOLD, GREEN, " 1- You will play with AI ", RESET)
    nbrG = 2
    list_gamers = []
    # Your custom player - humain
    new_gamer = gamer.Gamer("")
    print(BOLD, BLUE, f"Create gamer number : 1 ", RESET)
    pseudo = input("Tell me your pseudo : ")
    new_gamer.pseudo =pseudo.upper()
    list_gamers.append(new_gamer)

    # custom player - AI
    new_gamer2 = gamer.Gamer("")
    print(BOLD, BLUE, f"Create gamer number : 2 ", RESET)
    pseudo = "AI-PLAYER"
    print("You will play with : AI-PLAYER ")
    new_gamer2.pseudo  = pseudo
    list_gamers.append(new_gamer2)

    new_game.list_gamers = list_gamers

    score_max = 0
    while score_max != 11 and score_max != 22 and score_max != 2:
        print(BOLD, GREEN, " 2- Choice score max (11 or 22 or 2 to test )", RESET)
        score_max = int(input("Write score max : "))
        new_game.score_max = score_max

    level = 0
    while level != 1 and level != 2:
        print(BOLD, GREEN, " 3- Choose level (1 or 2)", RESET)
        level = int(input("Write score max: "))
        new_game.level = level

    print(" ------------- Carva5al gaming studio ------------- ")

    return nbrG, score_max, level, new_game


def game_details_show(new_game):
    os.system("clear")
    print(" ------------- Game details ------------- ")
    print(BOLD, GREEN, " Score max : ", new_game.score_max, RESET)
    gamer_list = new_game.list_gamers
    i = 1
    for gamer in gamer_list:
        print(
            BOLD, GREEN, f" Gamer {i} : {gamer.pseudo} - score = {gamer.score} ", RESET
        )
        i = i + 1


def get_first_chance_card(new_game, list_disponible):
    carte_random = random.choice(list_disponible)

    print(
        BOLD,
        GREEN,
        f"Your chance, You get this card ! -> [{carte_random.symbol}] ",
        RESET,
    )
    response = input("You accept it ( yes / no ) ")

    # list gamer nbre 1 cards
    gamer_cards = new_game.list_gamers[0].kaf
    # list cards which is louta
    louta_cards = new_game.list_cards_louta

    if response.lower() == "yes":
        gamer_cards.append(carte_random)
        new_game.list_gamers[0].kaf = gamer_cards
        list_disponible.remove(carte_random)

    elif response.lower() == "no":
        louta_cards.append(carte_random)
        new_game.list_cards_louta = louta_cards
        list_disponible.remove(carte_random)

        print("Good luck, You not get the card !")

    return new_game, list_disponible


def habat_louta(new_game, list_awra9_disponible):
    # list cards which is louta
    louta_cards = new_game.list_cards_louta
    while len(louta_cards) < 4:
        carte_random = random.choice(list_awra9_disponible)
        louta_cards.append(carte_random)
        list_awra9_disponible.remove(carte_random)

    new_game.list_cards_louta = louta_cards
    return louta_cards


def distribute_cards(new_game, available_cards_list):
    # list gamer nbre 1 cards
    gamer1_cards = new_game.list_gamers[0].kaf
    # list gamer nbre 1 cards
    gamer2_cards = new_game.list_gamers[1].kaf

    while len(gamer1_cards) < 3:
        carte_random = random.choice(available_cards_list)
        gamer1_cards.append(carte_random)
        available_cards_list.remove(carte_random)
    new_game.list_gamers[0].kaf = gamer1_cards

    while len(gamer2_cards) < 3:
        carte_random = random.choice(available_cards_list)
        gamer2_cards.append(carte_random)
        available_cards_list.remove(carte_random)
    new_game.list_gamers[1].kaf = gamer2_cards

    return gamer1_cards, gamer2_cards


def show_game(new_game, available_cards_list):
    os.system("clear")
    # list gamer nbre 1 cards
    gamer1_cards = new_game.list_gamers[0].kaf
    # list gamer nbre 2 cards
    gamer2_cards = new_game.list_gamers[1].kaf
    # list of cards louta
    louta_cards = new_game.list_cards_louta
    new_game.list_gamers[0].score

    number_of_cards_dispo = len(available_cards_list)
    print(
        BOLD,
        GREEN,
        f" ------------------------ Card diponible [{number_of_cards_dispo}] ------------------------ ",
    )
    print(
        BOLD,
        GREEN,
        f" ------------------------ Max Score : [{new_game.score_max}] ------------------------ ",
    )

    print(
        f"-- | {new_game.list_gamers[0].pseudo } : {new_game.list_gamers[0].score } | ----------------- Level : {new_game.level} ----------------- | {new_game.list_gamers[1].pseudo } : {new_game.list_gamers[1].score } | --\n",
        RESET,
    )

    c1 = ""
    c2 = ""
    c3 = ""
    for i in gamer1_cards:
        c1 = c1 + f" [{i.symbol}] "

    for i in gamer2_cards:
        c2 = c2 + f" [{i.symbol}] "

    for i in louta_cards:
        c3 = c3 + f" [{i.symbol}] "

    print(BOLD, BLUE, f"{new_game.list_gamers[0].pseudo }")
    print(BOLD, BLUE, f"{c1}", RESET)
    print("    -------    \n")
    print(BOLD, RED, f" {c3} \n", RESET)
    print("    -------    ")
    print(BOLD, BLUE, f"{new_game.list_gamers[1].pseudo }")
    print(BOLD, BLUE, f"{c2}")
    print(BOLD, GREEN, "-------------------------------------\n")


def msg_player_mov(new_game):
    gamer1_cards = new_game.list_gamers[0].kaf
    louta_cards = new_game.list_cards_louta
    your_card = ""
    list_card_you_want_to_get_it = []

    print(
        BOLD,
        GREEN,
        "The movements in the game will be with cards symbols ==> [♠ - ♥ - ♦ - ♣] ",
        RESET,
    )
    state = False
    while not state:
        your_card = input("Your card you will play ==> ")
        for i in gamer1_cards:
            a = i.symbol
            if i.symbol == your_card:
                state = True
                y_card = i

    print(
        BOLD,
        GREEN,
        "Still Write Cards symbole until fine, So write 'fine' if fine haha ",
        RESET,
    )
    state = False
    while not state:
        card_you_want_to_get_it = input("Card ==> ")
        if card_you_want_to_get_it.lower() == "fine":
            state = True
        else:
            state_2 = True
            for i in louta_cards:
                a = i.symbol
                if i.symbol == card_you_want_to_get_it:
                    list_card_you_want_to_get_it.append(i)
                else:
                    state_2 = True
            if not state_2:
                print(f"This card is False!")

    return y_card, list_card_you_want_to_get_it


def verify_combination(my_play, list_cards):
    my_play_value = my_play.value
    list_cards_value = 0
    for i in list_cards:
        list_cards_value = list_cards_value + i.value
    if my_play_value == list_cards_value:
        return True
    else:
        return False


def play_well(new_game, my_play, cards_list, combination_state):
    # list gamer nbre 1 cards
    gamer1_cards = new_game.list_gamers[0].kaf
    # Score box
    gamer1_score_box = new_game.list_gamers[0].box_score
    # list of cards louta
    louta_cards = new_game.list_cards_louta
    if combination_state:
        gamer1_score_box.append(my_play)
        gamer1_cards.remove(my_play)
        # for this work
        new_game.list_gamers[0].last_killer = 1
        new_game.list_gamers[1].last_killer = 0
        for i in cards_list:
            gamer1_score_box.append(i)
            louta_cards.remove(i)
            if len(louta_cards) == 0:
                gamer1_score_box.append("chkoba")
                print("CHKOBAAAAAAAAAAA")
                time.sleep(2)
    else:
        # add the card to louta cards
        louta_cards.append(my_play)
        new_game.list_cards_louta = louta_cards
        gamer1_cards.remove(my_play)
    return gamer1_score_box


def ai_play_random(new_game):
    gamer2_score_box = new_game.list_gamers[1].box_score
    gamer2_cards = new_game.list_gamers[1].kaf
    louta_cards = new_game.list_cards_louta
    length_louta_cards = len(louta_cards)
    # AI choose his card to play in random way
    your_card = random.choice(gamer2_cards)
    gamer2_cards.remove(your_card)
    print(BOLD, GREEN, "AI-PLAYER movement ", RESET)
    time.sleep(4)
    print(BOLD, GREEN, f" AI will play ==> {your_card.symbol}", RESET)
    # Now AI will be
    if length_louta_cards == 0:
        louta_cards.append(your_card)
    else:
        # we will find all combinition to take cards from louta
        state = False
        for length in range(length_louta_cards):
            # card.append(louta_cards[length].get_value())
            a = show_combinations(louta_cards, length + 1, your_card.value)
            if len(a) != 0:
                gamer2_score_box.append(your_card)
                time.sleep(4)
                my_play = a[0]
                state = True
                new_game.list_gamers[0].last_killer = 0
                new_game.list_gamers[1].last_killer = 1
                # print(my_play [0])
                c = " "
                for i in my_play:
                    gamer2_score_box.append(i)
                    louta_cards.remove(i)
                    c = c + "  " + i.symbol
                    if len(louta_cards) == 0:
                        gamer2_score_box.append("chkoba")
                        print("CHKOBAAAAAAAAAAA")
                        time.sleep(2)
                print(BOLD, GREEN, f"Card ==> {c}", RESET)
                time.sleep(4)
                break

        if not state:
            time.sleep(4)
            print(BOLD, GREEN, f"Card ==> fine ", RESET)
            time.sleep(4)
            louta_cards.append(your_card)
        time.sleep(3.5)


def calcul_score(new_game):
    gamer1_score_box = new_game.list_gamers[0].box_score
    gamer2_score_box = new_game.list_gamers[1].box_score
    sept_carreau = 0
    nombre_max_box = len(gamer1_score_box)
    max_carreau = 0
    bermila = 0
    chkoba_gamer1 = 0
    chkoba_gamer2 = 0

    for i in gamer1_score_box:
        if i.symbol == "7 ♦":
            sept_carreau = sept_carreau + 1
        if "♦" in i.symbol:
            max_carreau = max_carreau + 1
        if i.value == 6 or i.value == 7:
            bermila = bermila + 1

        if i == "chkoba":
            chkoba_gamer1 = chkoba_gamer1 + 1
            new_game.list_gamers[0].score = new_game.list_gamers[0].score + 1

        for j in gamer1_score_box:
            if j == "chkoba":
                chkoba_gamer2 = chkoba_gamer2 + 1
                new_game.list_gamers[1].score = new_game.list_gamers[1].score + 1

    time.sleep(3)
    if nombre_max_box > 20:
        new_game.list_gamers[0].score = new_game.list_gamers[0].score + 1
        print("Karta pour gamer 1")
    elif nombre_max_box == 20:
        print("Karta Ybaji")
    else:
        new_game.list_gamers[1].score = new_game.list_gamers[1].score + 1
        print("Karta pour AI gamer ")
    time.sleep(3)

    if sept_carreau > 0:
        new_game.list_gamers[0].score = new_game.list_gamers[0].score + 1
        print("7 Haya pour gamer 1")
    else:
        new_game.list_gamers[1].score = new_game.list_gamers[1].score + 1
        print("7 Haya pour AI gamer")
    time.sleep(3)

    if max_carreau > 4:
        new_game.list_gamers[0].score = new_game.list_gamers[0].score + 1
        print("Dinari for gamer 1")
    elif max_carreau == 5:
        print("Dinari Ybaji")
    else:
        new_game.list_gamers[1].score = new_game.list_gamers[1].score + 1
        print("Dinari for AI gamer ")
    time.sleep(3)

    if bermila > 4:
        new_game.list_gamers[0].score = new_game.list_gamers[0].score + 1
        print("Bermila for gamer 1")
    elif bermila == 4:
        print("Bermila Ybaji")
    else:
        new_game.list_gamers[1].score = new_game.list_gamers[1].score + 1
        print("Bermila for AI gamer ")
    time.sleep(3)

    if chkoba_gamer1 != 0:
        print(f"{chkoba_gamer1} Chkobaaa for gamer 1")
        time.sleep(3)

    if chkoba_gamer2 != 0:
        print(f"{chkoba_gamer2} Chkobaaa for AI gamer ")
        time.sleep(3)


def show_and_write_if_gamer_win(new_game):
    score_gamer1 = new_game.list_gamers[0].score
    score_ai = new_game.list_gamers[1].score
    os.system("clear")
    print("Nice Game ")
    time.sleep(3.5)
    if score_gamer1 > score_ai:
        print(f"Good job Gamer : {new_game.list_gamers[0].pseudo }, you win!")
        time.sleep(3.5)
        f = open("historique.txt", "a")
        f.write("\n")
        f.write(f"{new_game.list_gamers[0].pseudo } was win in {date.today()}")
        f.close()
    elif score_gamer1 < score_ai:
        print("Good job AI, you win!")
        time.sleep(3.5)
    else:
        print("Good job AI and you had the some score ")
        time.sleep(3.5)
