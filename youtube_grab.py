from credentials import api_key
from apiclient.discovery import build
from credentials import api_key

class playlist_data():
    def __init__(self):
        self.playlist = {}
        self.key = api_key
        self.youtube = build('youtube','v3',developerKey = api_key)
    
    def select_playlist(self,user_id):
        playlist_request = self.youtube.playlists().list(
        part = 'contentDetails, snippet',
        channelId = user_id
        )   
        try:
            pl_response = playlist_request.execute()
        except:
            return playlist_data.select_playlist(self,input(f'User Not Found. Please try again.\n'))
        for counter, item in enumerate (pl_response['items']):
            self.playlist[counter] = [pl_response['items'][counter]['snippet']['title'],pl_response['items'][counter]['id']]