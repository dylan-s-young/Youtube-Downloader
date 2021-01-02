from googleapiclient.discovery import build
import json
from youtube_grab import *
from credentials import api_key
from test import *
#UCdnF1w8xarlWwpCNSq260LQ

if __name__ == "__main__":
    user_id = input(f'Please input channelID. Refer to instructions on github.\n')
    user = playlist_data()
    user.select_playlist(user_id)

    print(user.playlist)

