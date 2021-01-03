from credentials import api_key
from apiclient.discovery import build
from credentials import api_key
from test import *

class playlist_data():
    def __init__(self):
        self.playlist = {} #Stores 0:TITLE - 1:PLAYLISTID
        self.key = api_key
        self.youtube = build('youtube','v3',developerKey = api_key)
        self.playlist_selection = ""
    
    def get_playlist(self,user_id):
        pl_request = self.youtube.playlists().list(
        part = 'contentDetails, snippet',
        channelId = user_id
        )   
        try:
            pl_response = pl_request.execute()
        except:
            return playlist_data.get_playlist(self,input(f'User Not Found. Please try again.\n'))
        for counter, item in enumerate (pl_response['items']):
            self.playlist[counter] = [pl_response['items'][counter]['snippet']['title'],pl_response['items'][counter]['id']]
        
    def select_playlist(self):
        for key,value in self.playlist.items():
            print(f'{key} -> {value[0]}')
        while True: 
            try:
                playlist_input = is_digit(input(f'Please select a playlist to download.\n'))
                self.playlist_selection = self.playlist[playlist_input][1]
                break
            except KeyError:
                print(f'Input exceeds playlist count. Try again.')
    
    def options(self):
        pl_item_request = self.youtube.playlistItems().list(
            part = 'contentDetails',
            playlistId = self.playlist_selection #Playlist that was selected
        )
        pl_response = pl_item_request.execute()
        for item in pl_response['items']:
            print(item['contentDetails']['videoId'])
            print()
            