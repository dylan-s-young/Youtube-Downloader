from googleapiclient.discovery import build
import json
from youtube_grab import *
from credentials import api_key
from test import *
#UCdnF1w8xarlWwpCNSq260LQ - YT Channel

if __name__ == "__main__":
    user_id = input(f'Please input channelID. Refer to instructions on github.\n')
    user = playlist_data()
    user.get_playlist(user_id)
    user.select_playlist()
    user.options()
    

 