from credentials import api_key
from apiclient.discovery import build
from credentials import api_key
from test import *
from download import *

class playlist_data():
    def __init__(self):
        self.playlist = {} #  Stores Playlist Results. Key = (n+1) :Value = 0:TITLE - 1:PLAYLISTID
        self.key = api_key # API Key From Youtube 
        self.youtube = build('youtube','v3',developerKey = api_key)
        self.playlist_selection = "" # Stores Playlist ID
        self.videos = {} #Stores Videos - Key = (n+1) : Value ==  0:Title, 1: Videoid
        self.dir = '' #Stores Directory where videos will be installed. 
        self.user_id = ''
    
    def get_playlist(self, user_id):
        self.user_id = user_id
        pl_request = self.youtube.playlists().list(
        part = 'contentDetails, snippet',
        channelId = user_id,
        maxResults = 50
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
    def grab_vidoes(self):
        nextPageToken = None
        count = 0
        while True:
            
            pl_item_request = self.youtube.playlistItems().list(
                part = 'contentDetails',
                playlistId = self.playlist_selection, #Playlist that was selected
                maxResults = 50, # Get 50 Results 
                pageToken = nextPageToken
            )
            pl_response = pl_item_request.execute() 

            for item in pl_response['items']:
                video_id = item['contentDetails']['videoId'] #Video_id from playlist
                req_vids = self.youtube.videos().list( #request for title 
                    part = 'snippet',
                    id = video_id  
                )
                vid_request = req_vids.execute() #Executes request for video information
                try:
                    vid_title = vid_request['items'][0]['snippet']['title'] # Sets video title to variable
                    print(f'Adding {count} - {vid_title} to download list.')
                    self.videos[count] = [vid_title,video_id]
                    count += 1    
                except: 
                    print(f'Video Deleted or privated. ')
                
            
            nextPageToken = pl_response.get('nextPageToken')
            if not nextPageToken: #Breaks while loop when there are no more songs in playlist.
                break
    def download_videos(self): #WILL COME BACK TO THIS LATER
        try: 
            self.dir = input(f'Please Enter directory where you want these videos installed.')
        except: 
            pass
    
    def download_mp3(self):
        print(f'Starting the Download')
        audio_download(self.videos,self.dir) #From Download.py
    
    def set_directory(self): #method to change directory
        self.dir = is_path()

    
    