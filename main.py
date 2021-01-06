from googleapiclient.discovery import build
import json
from youtube_grab import *
from credentials import api_key
from test import *
#UCdnF1w8xarlWwpCNSq260LQ - YT Channel
#UCCbF-Etrc4jivW7CIxeO5lA - YT Channel 
def print_yd():
    print(f'                           _\n'            
          f'  |V| _  _| _    |_  \/   | \ \/ |  _ __\n'
          f'  | |(_|(_|(/_   |_) /    |_/ /  | (_|| |\n')

def options():
    user_input = input(f'What do you want to do?\n'
            f'DA - Download playlist to audio folder.\n'
            f'DV - Download videos to video folder.\n'
            f'Q - Quit\n')
    while True:
        if user_input == 'DA':
            user.download_mp3()
            options()
        elif user_input == 'DV':
            pass 
        elif user_input == 'Q':
            quit()
        else: 
            user_input = input(f'Input not detectable. Please type input again.\n')


if __name__ == "__main__":
    print_yd()
    user_id = input(f'Please input channelID. Refer to instructions on github.\n')
    user = playlist_data()
    user.get_playlist(user_id)
    user.select_playlist()
    user.grab_vidoes()
    options()