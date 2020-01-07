import pygame
from black_screens import *
from starting_screen import *
from settings_screen import *
from choose_screens import *
from wait_screen import *
from cli_socket import *
import threading
import time

pygame.init()
DISPLAY = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#DISPLAY = pygame.display.set_mode((1920,1080))

#start screen and player name input
starting = starting_screen()
starting.draw(DISPLAY)

settings = settings_screen()
settings.draw(DISPLAY)

#connects to raspi
sock = cli_socket("202.161.104.55", 7884)

show_wait = wait_screen(sock) #waiting for players

sock.send(settings.player_names) #sends the player's name to the server
namelist = []

def player_wait(server):
    '''client name is sent and all connected client names are received'''
    global namelist
    while True:
        msg = server.recv()
        if msg == "ok":
            show_wait.stop()
            break

        namelist = msg.split(",")
        show_wait.update(namelist)
    
wait_for_players = threading.Thread(target=player_wait, args=(sock,))
wait_for_players.start()

show_wait.draw(DISPLAY)
say = black_screens()
choose = choose_screens()
i_am_czar = False


while True:
    msg = sock.recv()
    print(msg)
    if msg == "czar":
        say.draw(DISPLAY, "You are the Card Czar.")
        i_am_czar = True
    elif msg == '':
        continue
    else:
        cards, black_card = msg.split("#")
        cards = cards.split("%")

        if cards[0] == "cz_choose":
            del cards[0]
            if i_am_czar:
                choose.czar_choose(DISPLAY, black_card, cards)
                sock.send(choose.selected_card)
            else:
                choose.player_look(DISPLAY, sock, black_card, cards) 
        elif cards[0] == "point":
            del cards[0]
            point_win = cards[0] + " got a point!"
            say.draw(DISPLAY, point_win)
            sock.send("ok")
        elif cards[0] == "win":
            del cards[0]
            winner = cards[0] + " won...Tryhard."
            say.draw(DISPLAY, winner)
            break
        elif cards[0] == "cz_reset":
            i_am_czar = False

        else:
            choose.player_choose(DISPLAY, cards, black_card) 

            print(cards[choose.selected_card])
            sock.send(str(choose.selected_card))
        
        

