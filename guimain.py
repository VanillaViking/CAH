import pygame
from starting_screen import *
from settings_screen import *
from black_screens import *
from choose_screens import *
from players import *
from cards import *
pygame.init()
DISPLAY = pygame.display.set_mode((1920, 1080))

#SCREENS
starting = starting_screen()
settings = settings_screen()
black_screens =  black_screens()
choose_screens = choose_screens()

#GAME START
starting.draw(DISPLAY)
settings.draw(DISPLAY)

#PLAYERS
PlayerNames = []
temp = settings.player_names.split(",")
for n in temp:
    PlayerNames.append(n.strip())

PLAYERS = [PLAYER(n) for n in PlayerNames]

#BOT PLAYERS
for n in range(settings.number_of_bots):
    name = "BOT" + str(n)
    PLAYERS.append(PLAYER(name))

#ASSIGNING CARDS
for n in range(len(PLAYERS)):
    for s in range(7):
        PLAYERS[n].assign_cards(WHITE.pop(random.randint(0,(len(WHITE)-1))))     #Gives each player random cards

turn = 0
won = False

#MAIN LOOP
while not won:
    if turn >= len(PLAYERS):
        turn = 0
    PLAYERS[turn].toggle_card_czar()
    black_screens.draw(DISPLAY, ("%s is the card czar." % PLAYERS[turn].name))          #show card czar

    black_card = BLACK[random.randint(0,len(BLACK)-1)]      #select random black card

    #PLAYER CHOICE
    player_picks = []
    for n in range(len(PLAYERS)):
        if not PLAYERS[n].is_card_czar and "BOT" not in PLAYERS[n].name:
            black_screens.draw(DISPLAY, ("%s's turn to choose" % PLAYERS[n].name))             #display player
            choose_screens.player_choose(DISPLAY, PLAYERS[n].cards, black_card)       #let them pick
            PLAYERS[n].choose(choose_screens.selected_card)
            print(PLAYERS[n].chosen_card)
        
        #BOT CHOICE
        if "BOT" in PLAYERS[n].name:            
            bot_choice = random.randint(0, len(PLAYERS[n].cards)-1)
            PLAYERS[n].chosen_card += PLAYERS[n].cards.pop(bot_choice)

    #COLLECT PLAYER PICKS    
    for n in range(len(PLAYERS)):
        if not PLAYERS[n].is_card_czar:
            player_picks.append(PLAYERS[n].chosen_card)
    random.shuffle(player_picks)

    #CARD CZAR JUDGEMENT
    for n in range(len(PLAYERS)):
        if PLAYERS[n].is_card_czar:
            black_screens.draw(DISPLAY, ("Time for %s to judge..." % PLAYERS[n].name))              #card czar choses winning card
            if "BOT" not in PLAYERS[n].name:
                choose_screens.czar_choose(DISPLAY, black_card, player_picks)
                winner_card = choose_screens.selected_card
            else:
                winner_card = player_picks[random.randint(0,len(player_picks) - 1)]


    #POINT GOES TO...       
    for n in range(len(PLAYERS)):
        if winner_card == PLAYERS[n].chosen_card:
            black_screens.draw(DISPLAY, ("%s got a point!" % PLAYERS[n].name))
            PLAYERS[n].give_point()

            if PLAYERS[n].points >= settings.maximum_pts:                                   #checking if player has won
                winner = PLAYERS[n].name
                won = True

    #RESETTING...
    for n in range(len(PLAYERS)):
        if not PLAYERS[n].is_card_czar:
            PLAYERS[n].clear_choice()
            PLAYERS[n].get_card()

    PLAYERS[turn].toggle_card_czar()
    turn += 1

#WINNER WINNER CHICKEN DINNER
black_screens.draw(DISPLAY, "%s won the game ...Tryhard." % winner)
