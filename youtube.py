from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_resolution_stream = streams.get_highest_resolution()
        highest_resolution_stream.download(output_path=save_path)
        print("video downloaded successfully")
    
    except Exception as e:
        print(e)
        
    
url = "https://www.youtube.com/watch?v=LJ7pzebXX6g"
save_path = "/Users/jerryarhawho/Desktop/python_proj/youtube-downloader"

download_video(url, save_path)
    