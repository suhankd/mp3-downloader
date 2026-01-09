import os
import yt_dlp

def download(url):

    configs = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': 'audio/%(title)s.%(ext)s',
        'noplaylist': True
    }

    if not os.path.exists('audio'):
        os.makedirs('audio')

    downloader = yt_dlp.YoutubeDL(configs)

    info = downloader.extract_info(url, download=True)
    filename = downloader.prepare_filename(info).replace('webm','mp3')

if __name__ == "__main__":

    with open("links.txt", "r") as file:

        urls = [line.strip() for line in file]

        for url in urls:

            download(url)