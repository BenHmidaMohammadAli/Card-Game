from packages import game 
from packages import gamer 
from packages import carte 

from functions import chkobaGamefunctions as ch
import os 
import random
import time 

choice = "Hello"

while choice.lower() != 'q' :
    os.system("clear") 
    choice = ch.create_Menu_welcome()
    os.system("clear")
    if choice == "3" : 
        # quite the game
        choice = ch.quit()

    elif choice == "2" : 
        choice = ch.show_historique()

    elif choice == "1": 
        # let's play 
        # customize the game 
        nbrG, scoreMAx, niveau  , new_game= ch.create_Menu_custom_game()
        os.system("clear")
        ch.game_details_show(new_game)
        os.system("clear")

        input("Press Enter to Start... ")
    
        os.system("clear")
        while new_game.list_gamers[0].get_score() < new_game.get_score_max() and new_game.list_gamers[1].get_score()< new_game.get_score_max() :
            i = 0
            cart_disponible = ch.create_cards_list()
            if i % 2 == 0: 
                new_game, cart_disponible = ch.get_first_chance_card(new_game,cart_disponible)
            while len(cart_disponible) != 0:
                
                ch.waza3_awra9(new_game, cart_disponible)
                if i == 0 :
                    ch.habat_louta(new_game , cart_disponible)

                os.system("clear")
                ch.show_game(new_game, cart_disponible)

                for i in range(3):
                # humain play 
                    your_card, list_card_you_want_to_get_it = ch.msg_player_mov(new_game)
                    etat_combinition = ch.verif_combinisation(your_card, list_card_you_want_to_get_it )
                    a  = ch.play_well(new_game, your_card, list_card_you_want_to_get_it, etat_combinition)
                    ch.show_game(new_game, cart_disponible)
                    # AI play 
                    ch.ai_play_random(new_game)
                    ch.show_game(new_game, cart_disponible)
            i = i+1
            ch.calcul_score(new_game)
        else :
            ch.show_and_write_if_gamer_win(new_game)

    
# chkoba 
# li yekil le5ir yhez lkol 











    

   




   
    



        

