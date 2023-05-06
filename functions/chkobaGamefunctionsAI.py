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


#--------- AI Algo that calculating all Posiblity Functions ---------------

def choice_best_combination (new_game , list_possibility, your_card):
    #best cobination depend value of score 
    length_louta_cards = len(new_game.list_cards_louta)
  
    I_choose_one = False 
    tuple_I_choose =()
    score_of_tuple_max = 0

    for i in list_possibility :        
        score_of_tuple = 0     
        #verif card that we will play with it what can add in score 
        if your_card.symbol == "7 ♦" :
            score_of_tuple = 1    
        #if this card will had "♦" mean in the root of 1 point is the score 
        elif "♦" in your_card.symbol :
            score_of_tuple = 0.025
        #if this card will had "6" mean in the root of 1 point is the score 
        elif "6" in your_card.symbol :
            score_of_tuple = 0.025
        #if this card will had "7" mean in the root of 1 point is the score 
        elif "7" in your_card.symbol :
            score_of_tuple = 0.025     
           
        #if this cards will make him had chkoba mean 1 point is the score, So I will take it and stop 
        # verifing (break) cause in totally of case you will take all cards and take 1 point + others 
        # if exist for example 7 ♦ or others ..3            
        if len(i) == length_louta_cards :
            tuple_I_choose = i[0]
            score_of_tuple_max == 99999
            I_choose_one = True
            break 
        #if combinition is had 1 card 
        elif len(i) == 1:
            #if this card == 7 ♦ wich mean 1 point is the score 
            if i[0].symbol == "7 ♦" :
                score_of_tuple = 1
            #if this card will had "♦" mean in the root of 1 point is the score 
            elif "♦" in i[0].symbol :
                score_of_tuple = 0.025
            #if this card will had "6" mean in the root of 1 point is the score 
            elif "6" in i[0].symbol :
                score_of_tuple = 0.025
            #if this card will had "7" mean in the root of 1 point is the score 
            elif "7" in i[0].symbol :
                score_of_tuple = 0.025     
                
        elif len(i) != 1:
            for j in i :
                card_symbol = j.symbol
                if "7 ♦" in card_symbol :
                    score_of_tuple = score_of_tuple + 1.25
                    
                if "♦" in card_symbol :
                    score_of_tuple = score_of_tuple + 0.025
                    
                if "7" in card_symbol :
                    score_of_tuple = score_of_tuple + 0.025
                    
                if "6" in card_symbol :
                    score_of_tuple = score_of_tuple + 0.025
                    
        if  score_of_tuple >= score_of_tuple_max:
            score_of_tuple_max=score_of_tuple
            I_choose_one = True 
            tuple_I_choose = i

    if I_choose_one == True:
        return score_of_tuple_max, tuple_I_choose
    else : 
        return score_of_tuple_max, list_possibility[0]

def search_list_value(lst , value):
    """Searches for objects in a list that have an attribute named "value" equal to 7"""
    result = []
    for obj in lst:
        if obj.value == value:
            result.append(obj)
    return result

def search_list_symbol(lst , symbol):
    """Searches for objects in a list that have an attribute named "symbol" equal to 7"""
    result = []
    for obj in lst:
        if obj.symbol == symbol:
            result.append(obj)
    return result

def test_if_will_be_a_chkoba(louta_cards , cards_player_to_test):
    total_value_louta = 0
    I_can_get_chkoba = False
    your_card_to_play = None
    
    for obj in louta_cards:
        total_value_louta = total_value_louta + obj.value
        
    for obj in cards_player_to_test :
        if obj.value == total_value_louta :
            I_can_get_chkoba = True 
            your_card_to_play = obj 
            break    

    return I_can_get_chkoba , your_card_to_play
            
def continue_the_playing_process (new_game ,your_card , list_you_will_get) :
    AI_score_box = new_game.list_gamers[1].box_score
    AI_cards = new_game.list_gamers[1].kaf
    louta_cards = new_game.list_cards_louta 
    
    AI_cards.remove(your_card)
    print(BOLD, GREEN, "AI-PLAYER movement ", RESET)
    time.sleep(4)
    print(BOLD, GREEN, f" AI will play ==> {your_card.symbol}", RESET)
    if len(list_you_will_get)!= 0 :
        new_game.list_gamers[0].last_killer = 0
        new_game.list_gamers[1].last_killer = 1
        AI_score_box.append(your_card)
    else :
        louta_cards.append(your_card)
    time.sleep(4)
   
    c = " "
    
    if len(list_you_will_get) == 1:
        c = c + "  " + list_you_will_get[0].symbol
        AI_score_box.append(list_you_will_get[0])
        louta_cards.remove(list_you_will_get[0])
        if len(louta_cards) == 0:
            AI_score_box.append("chkoba")
            print("CHKOBAAAAAAAAAAA")
            time.sleep(2)
    else :
        i= 0
        while len(list_you_will_get) > i:
            c = c + "  " + list_you_will_get[i].symbol
            AI_score_box.append(list_you_will_get[i])
            louta_cards.remove(list_you_will_get[i])
            
            if len(louta_cards) == 0:
                AI_score_box.append("chkoba")
                print("CHKOBAAAAAAAAAAA")
                time.sleep(2)
            i=i+1
            
    if c != " ": 
        print(BOLD, GREEN, f"Card ==> {c}", RESET)
    else :
        print(BOLD, GREEN, f"Card ==> fine ", RESET)
    time.sleep(4)
            
def ai_play_minmax_algo(new_game):
    AI_score_box = new_game.list_gamers[1].box_score
    
    gamer1_cards = new_game.list_gamers[0].kaf
    AI_cards = new_game.list_gamers[1].kaf
    louta_cards = new_game.list_cards_louta 
    length_louta_cards = len(louta_cards)
    
    state_of_game = False # not again play and win a cards 
    #♠ - ♥ - ♦ - ♣
    if length_louta_cards != 0 :
        #1st state chkoba  mean 1 point in score so verif we had it  "Chkobaa" and you will get all card in 
        #louta cards list 
        if state_of_game == False :
            I_can_get_chkoba, your_card= test_if_will_be_a_chkoba(louta_cards , AI_cards)
            
            if I_can_get_chkoba == True :
                list_to_play = list(louta_cards)
                continue_the_playing_process(new_game ,your_card , list_to_play) 
                state_of_game = True

        #2st state 7 ♦  mean 1 point in score so verif we had it "El7aya"
        #it's depends if cards of 7 ♦ in ai or louta or gamer1 cards  
        if state_of_game == False :       
            cr7 = card.Card("7 ♦", 7)
            gamer1_have_7aya = False 
            louta_7aya = False 
            AI_have_7aya = False
            
            #Search where is 7 ♦ 
            for i in gamer1_cards:
                if i.value == 7 and i.symbol == "7 ♦" :
                    gamer1_have_7aya = True
                
            for i in louta_cards:
                if i.value == 7 and i.symbol == "7 ♦" :
                    louta_7aya = True
                    
            for i in AI_cards:
                if i.value == 7 and i.symbol == "7 ♦" :
                    AI_have_7aya = True
            
            #Search where is 7 
            gamer1_have_sab3a = False 
            louta_sab3a = False 
            AI_have_sab3a = False  
            for i in gamer1_cards :
                if i.value == 7 :
                    gamer1_have_sab3a = True
                            
            for i in louta_cards :
                if i.value == 7 :
                    louta_sab3a = True 
            
            for i in AI_cards :
                if i.value == 7 :
                    AI_have_sab3a = True
                        
            #Here if AI had 7 7aya and louta there is a 7 
            if AI_have_7aya == True and louta_sab3a == True :
                list_play = []
                your_card = search_list_symbol(AI_cards ,"7 ♦")
                
                possible = search_list_value(louta_cards , 7)
                your_play = possible[0]
                list_play.append(your_play)
                
                continue_the_playing_process (new_game ,your_card, list_play) 
                state_of_game == True
                
            elif AI_have_sab3a == True and louta_7aya == True :
                list_play = []
                possible = search_list_value(AI_cards , 7)
                your_card = possible[0]
                
                your_play = search_list_symbol(louta_cards ,"7 ♦")
                list_play.append(your_play)                
                
                continue_the_playing_process(new_game ,your_card, list_play)            
                state_of_game == True
        
            elif louta_sab3a == True and AI_have_sab3a == True:
                list_play = []
                possible = search_list_value(AI_cards , 7)
                your_card = possible[0]
                
                possible = search_list_value(louta_cards , 7)
                your_play = possible[0]
                list_play.append(your_play)                
                
                continue_the_playing_process(new_game ,your_card, list_play)      
                state_of_game == True   
                
        
        #                           --------------- 
        # in this step if the game stay with state == False 
        # we will talk about this 
        #4rd case max cards get it  mean maybe 1 point in score so verif we had it "Elkarta"
        #4rd case 6 ♠ - ♥ - ♦ - ♣ or 7 ♠ - ♥ - ♣  mean maybe 1 point in score so verif we had it "Bermila"
        #5th case max cards with ♦  mean maybe 1 point in score so verif we had it "Dinari"
        if state_of_game == False :
            test_cards_louta = list(louta_cards)
            card_dont_play = []
            score_max =0
            list_play = []
            for i in AI_cards :
                test_cards_louta.append(i)
                he_can_get_chkoba, card_he_will_play = test_if_will_be_a_chkoba(test_cards_louta , gamer1_cards)
                if he_can_get_chkoba == True :
                    card_dont_play.append(i)
                test_cards_louta.remove(i)
                
            your_cards_possible_toplay = list(set(AI_cards) - set(card_dont_play))
            if len(your_cards_possible_toplay) != 0:
                list_possibility = []
                list_play = []
                for i in range(len(your_cards_possible_toplay)):
                    for length in range(length_louta_cards):
                        a = ch.show_combinations(louta_cards, length+1, your_cards_possible_toplay[i].value)
                        if len(a) != 0 :
                            for x in a :
                                list_possibility.append(x)
                    if len(list_possibility) != 0:
                        score_of_tuple_max, list_play_w  = choice_best_combination (new_game , list_possibility, your_cards_possible_toplay[i])
                        if (score_of_tuple_max >= score_max ) and list_play_w != list_play :
                            score_max = score_of_tuple_max
                            your_card = your_cards_possible_toplay[i]
                            list_play = list_play_w
                            
                if your_card != None : 
                    continue_the_playing_process (new_game ,your_card, list_play) 
                    state_of_game = True
                            
            elif len(your_cards_possible_toplay) == 0:
                your_card = random.choice(AI_cards)
                #random should be != 7 
                continue_the_playing_process (new_game ,your_card , []) 
                state_of_game = True 
                
        #if tel the end the game still blocked we will play as random way 
        if state_of_game == False :
            your_card = random.choice(AI_cards)
            continue_the_playing_process (new_game ,your_card , []) 
            state_of_game = True 
                        
    #if length_louta_cards we will play card != of all cards of the gamer1 cards
    # also this card will not be a valued card 
    elif length_louta_cards == 0 :
        test_cards_louta = list(louta_cards)
        card_dont_play = []
        for i in AI_cards :
            test_cards_louta.append(i)
            he_can_get_chkoba, card_he_will_play = test_if_will_be_a_chkoba(test_cards_louta , gamer1_cards)
            if he_can_get_chkoba == True :
                card_dont_play.append(i)
            test_cards_louta.remove(i)  
                
        your_cards_possible_toplay = list(set(AI_cards) - set(card_dont_play))        
        if len(your_cards_possible_toplay) != 0 :
            your_card = your_cards_possible_toplay[0]
            continue_the_playing_process (new_game ,your_card , []) 
            state_of_game = True 
            
        elif len(your_cards_possible_toplay) == 0 :
            your_card = random.choice(AI_cards)
            continue_the_playing_process (new_game ,your_card , []) 
            state_of_game = True 
        

