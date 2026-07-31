import yt_dlp
import os
from tkinter import * 
from tkinter import filedialog as FileDialog
def download_audio(file="urls", folder="music"):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)

        options = {
         'format': 'bestaudio/best',
         'outtmpl': f'{folder}/%(title)s.%(ext)s',
         'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
    }],
}

        with open(file, encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip()]

        print("Downloading Youtube audio...")
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download(urls)

        print("Download completed")
    except Exception as e:
        print(f"An error occurred: {e}")

global url
def select_file():
    url = FileDialog.askopenfilename(
        defaultextension="*.txt",
        filetypes=(("txt",".txt"),)
        )
    
    print(url)