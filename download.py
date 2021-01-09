from __future__ import unicode_literals
import youtube_dl 

##METHODS FOR DOWNLOADING THAT ARE USED IN YOUTUBE_GRAB.py

def audio_download(audio_list,location_mp3,version):
    if version == 1:
        for i in range(len(audio_list)):
            try:
                print(f'Downloading {i} -> {audio_list[i][0]}')
                link = ['https://youtube.com/watch?v='+ audio_list[i][1]]
                location = location_mp3 + '/%(title)s.%(ext)s'
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
    else:
        try:
            print(f'Downloading your requested song.')
            link = ['https://youtube.com/watch?v='+ audio_list]
            location = location_mp3 + '/%(title)s.%(ext)s'
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
            print(f'Error Occured when downloading your requested') 

def video_download(video_list,location_mkv,version):
    location = location_mkv + '/%(title)s.%(ext)s'
    if version == 1: 
        for i in range(len(video_list)):
            print(f'Downloading {i} -> {video_list[i][0]}')
            link = ['https://youtube.com/watch?v=' + video_list[i][1]]
            location = location_mkv + '/%(title)s.%(ext)s'
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=webm]/bestvideo+bestaudio',
                'outtmpl': location,
                'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mkv'}],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(link)
    else: 
        link = ['https://youtube.com/watch?v=' + video_list]
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=webm]/bestvideo+bestaudio',
            'outtmpl': location,
            'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv'}],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(link)