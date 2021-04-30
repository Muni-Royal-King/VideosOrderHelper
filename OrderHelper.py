import os
from pytube import *

def MakeOrder(url,fileLocation):
    try:
        playlist = Playlist(url)
        os.chdir(fileLocation)
        counter = 0
        not_download=[]
        print("I am In Working Please Wait .... ")
        for video_name, link in zip(os.walk(os.getcwd()),playlist):
            for video in playlist.videos:
                counter += 1
                if (f"{counter} - {video.title}.mp4") in video_name[2]:
                    print(f'Its Downloaded/Renamed:- Video {counter} - {video.title}.mp4')

                elif video.title+".mp4" in video_name[2]:
                    os.rename(video.title+".mp4",f"{counter} - {video.title}.mp4")
                    print(f"Video: {video.title} Renamed-To : {counter} - {video.title}.mp4")
                else:
                    not_download.append(f"Video: {counter} - {video.title}")
                    print(f"Video: {counter} - {video.title} Not Downloaded Yet / Check Out The Name.")
        for pending_download in not_download:
            print(f"Pending Downloades : {pending_download}")

    except Exception as e :
        print("Check The Internet Connection And Also See The Error Name.")
        print("Error :",e)

    finally:
        print("My Job Done Dear!!")