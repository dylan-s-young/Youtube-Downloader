from googleapiclient.discovery import build
import json
from youtube_grab import *
from credentials import api_key
from test import *
#UCdnF1w8xarlWwpCNSq260LQ - YT Channel
def options():
    user_input = input(f'What do you want to do?\n'
            f'DL - Download playlist to audio folder.\n'
            f'R - Write playlist songs to playlist.\n'
            f'Q - Quit\n')
    while True:
        if user_input == 'DL':
            pass
        elif user_input == 'R':
            pass 
        elif user_input == 'Q':
            quit()
        else: 
            user_input = input(f'Input not detectable. Please type input again.')





if __name__ == "__main__":
    user_id = input(f'Please input channelID. Refer to instructions on github.\n')
    user = playlist_data()
    user.get_playlist(user_id)
    user.select_playlist()
    user.grab_vidoes()
    options()