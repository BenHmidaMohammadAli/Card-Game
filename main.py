import os
import random
import time

from functions import chkobaGamefunctions as ch
from functions import chkobaGamefunctionsRandom as chRandom
from functions import chkobaGamefunctionsAI as chAI

from packages import card, game, gamer

choice = "Hello"

while choice.lower() != "q":
    os.system("clear")
    choice = ch.create_Menu_welcome()
    os.system("clear")
    if choice == "3":
        # quite the game
        choice = ch.quit_game()

    elif choice == "2":
        # Show the gamer who win
        choice = ch.show_historique()

    elif choice == "1":
        # let's play
        # customize the game
        nbrG, score_max, level, new_game = ch.create_menu_custom_game()
        os.system("clear")
        ch.game_details_show(new_game)
        os.system("clear")
        input("Press Enter to Start... ")
        os.system("clear")
        if level == 1:
            #level 1
            while (
                new_game.list_gamers[0].score < new_game.score_max
                and new_game.list_gamers[1].score < new_game.score_max
            ):
                i = 0
                card_available = ch.create_cards_list()
                if i % 2 == 0:
                    new_game, card_available = ch.get_first_chance_card(
                        new_game, card_available
                    )
                while len(card_available) != 0:
                    ch.distribute_cards(new_game, card_available)
                    if i == 0:
                        ch.habat_louta(new_game, card_available)

                    os.system("clear")
                    ch.show_game(new_game, card_available)

                    for i in range(3):
                        # humain play
                        your_card, list_card_you_want_to_get_it = ch.msg_player_mov(
                            new_game
                        )
                        etat_combinition = ch.verify_combination(
                            your_card, list_card_you_want_to_get_it
                        )
                        a = ch.play_well(
                            new_game,
                            your_card,
                            list_card_you_want_to_get_it,
                            etat_combinition,
                        )
                        ch.show_game(new_game, card_available)
                        # AI play
                        chRandom.ai_play_random(new_game)
                        ch.show_game(new_game, card_available)
                i = i + 1
                # if the numbers of cards == 0 so the last killer get the rest of louta cards
                if new_game.list_gamers[0].last_killer == 1:
                    louta_cards = new_game.list_cards_louta
                    for i in louta_cards:
                        new_game.list_gamers[0].box_score.append(i)
                        louta_cards.remove(i)
                    print(
                        "Gamer, You get the rest of cards cause you are the last killer"
                    )
                    time.sleep(3)
                else:
                    louta_cards = new_game.list_cards_louta
                    for i in louta_cards:
                        new_game.list_gamers[1].box_score.append(i)
                        louta_cards.remove(i)
                    print("AI ,You get the rest of cards cause you are the last killer")
                    time.sleep(3)
                # Calcul the score
                ch.calcul_score(new_game)
            else:
                os.system("clear")
                ch.show_and_write_if_gamer_win(new_game)

        elif level == 2 :
            #level 2
            #some code about level  just we will call not the random choice of cards 
            while (
                new_game.list_gamers[0].score < new_game.score_max
                and new_game.list_gamers[1].score < new_game.score_max
            ):
                i = 0
                card_available = ch.create_cards_list()
                if i % 2 == 0:
                    new_game, card_available = ch.get_first_chance_card(
                        new_game, card_available
                    )
                while len(card_available) != 0:
                    ch.distribute_cards(new_game, card_available)
                    if i == 0:
                        ch.habat_louta(new_game, card_available)

                    os.system("clear")
                    ch.show_game(new_game, card_available)

                    for i in range(3):
                        # humain play
                        your_card, list_card_you_want_to_get_it = ch.msg_player_mov(
                            new_game
                        )
                        etat_combinition = ch.verify_combination(
                            your_card, list_card_you_want_to_get_it
                        )
                        a = ch.play_well(
                            new_game,
                            your_card,
                            list_card_you_want_to_get_it,
                            etat_combinition,
                        )
                        ch.show_game(new_game, card_available)
                        # AI play
                        chAI.ai_play_minmax_algo(new_game)
                        ch.show_game(new_game, card_available)
                i = i + 1
                # if the numbers of cards == 0 so the last killer get the rest of louta cards
                if new_game.list_gamers[0].last_killer == 1:
                    louta_cards = new_game.list_cards_louta
                    for i in louta_cards:
                        new_game.list_gamers[0].box_score.append(i)
                        louta_cards.remove(i)
                    print(
                        "Gamer, You get the rest of cards cause you are the last killer"
                    )
                    time.sleep(3)
                else:
                    louta_cards = new_game.list_cards_louta
                    for i in louta_cards:
                        new_game.list_gamers[1].box_score.append(i)
                        louta_cards.remove(i)
                    print("AI ,You get the rest of cards cause you are the last killer")
                    time.sleep(3)
                # Calcul the score
                ch.calcul_score(new_game)
            else:
                os.system("clear")
                ch.show_and_write_if_gamer_win(new_game) 
            
            
            
            
            
            