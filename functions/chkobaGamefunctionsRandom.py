import random
import time
from packages import *
from functions import chkobaGamefunctions as ch

# Setting the color combinations
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

#--------- AI Algo that Randomly work Function ---------------

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
        gamer2_score_box = new_game.list_gamers[1].box_score
    #gamer2_cards = new_game.list_gamers[1].kaf
    louta_cards = new_game.list_cards_louta
    length_louta_cards = len(louta_cards)
    
    state = False
    for length in range(length_louta_cards):
        # card.append(louta_cards[length].get_value())
        a = ch.show_combinations(louta_cards, length + 1, your_card.value)
          
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

