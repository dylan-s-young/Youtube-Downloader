from __future__ import unicode_literals
import youtube_dl 

##METHODS FOR DOWNLOADING THAT ARE USED IN YOUTUBE_GRAB.py

def audio_download(audio_list,location_mp3):
    for i in range(len(audio_list)):
        try:
            print(f'Downloading {i} -> {audio_list[i][0]}')
            link = ['https://youtube.com/watch?v='+ audio_list[i][1]]
            location = location_mp3 + '/%(title)s.%(ext)s'
            print(link)
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': location,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(link)
        except:
            print(f'Error Occured when downloading {audio_list[i][0]}')

def video_dowload():
    pass