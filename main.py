from googleapiclient.discovery import build
import json
from youtube_grab import *
from credentials import api_key
from test import *
from download import *
#UCdnF1w8xarlWwpCNSq260LQ - YT Channel
#UCCbF-Etrc4jivW7CIxeO5lA - YT Channel 
def print_startup():
    print(f'                           _\n'            
          f'  |V| _  _| _    |_  \/   | \ \/ |  _ __\n'
          f'  | |(_|(_|(/_   |_) /    |_/ /  | (_|| |\n')

def options():
    user_input = input(f'What do you want to do?\n'
            f'A - Download playlist as mp3 to folder\n'
            f'B - Download Playlist as mkv to folder\n'
            f'C - Change Directory\n'
            f'D - Download Individual Song\n'
            f'E - Download Individual Video\n'
            f'Q - Quit\n')
    while True:
        if user_input == 'A':
            user_id = input(f'Please input channelID. Refer to instructions on github.\n')
            user.get_playlist(user_id)
            user.select_playlist()
            user.grab_videos()
            user.download_mp3()
            options()
        elif user_input == 'B':
            user_id = input(f'Please in put channelID. Refer to instructions on github.\n')
            user.get_playlist(user_id)
            user.select_playlist()
            user.grab_videos()
            user.download_mkv()
            options()
        elif user_input == 'C':
            user.set_directory()
            options()
        elif user_input == 'D':
            vid_id, vid_title = user.vid_id_exist(input(f'Please input video_id to download your mp3. e.g. https://www.youtube.com/watch?v=6M5jL34kv9s has the video_id: 6M5jL34kv9s\n'))
            print(f'Downloading {vid_title} as mp3 to your specified directory.')
            audio_download(vid_id,user.dir,2)
            options()
        elif user_input == 'E':
            vid_id, vid_title = user.vid_id_exist(input(f'Please input video_id to download your mkv. e.g. https://www.youtube.com/watch?v=6M5jL34kv9s has the video_id: 6M5jL34kv9s\n'))
            print(f'Downloading {vid_title} as mkv to your specified directory.')
            video_download(vid_id,user.dir,2)
            options()
        elif user_input == 'Q':
            quit()
        else: 
            user_input = input(f'Input not detectable. Please type input again.\n')


if __name__ == "__main__":
    print_startup()
    user = playlist_data()
    user.set_directory()
    options()
    