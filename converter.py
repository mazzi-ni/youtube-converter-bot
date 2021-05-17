from moviepy.editor import *
from pytube import YouTube
from PIL import Image
import requests
import os
import eyed3

# YouTube(url).streams.filter(only_audio=True).first().download()
def converter(url):
    yt = YouTube(url)
    title = yt.title
    author = yt.author

    print(yt.title)
    print(yt.author)

    im = Image.open(requests.get(yt.thumbnail_url, stream=True).raw)
    im.save('cover.jpeg', 'JPEG')

    yt.streams.first().download()

    global filter_title
    filter_title = title
    if '$' in title:
        filter_title = title.replace('$', '')

    # converter mp4 to mp3
    mp4_file = "./" + filter_title + ".mp4"
    mp3_file = "./" + filter_title + ".mp3"

    print(mp4_file)
    print(mp3_file)


    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()

    # edit metadata
    file = eyed3.load(mp3_file)
    file.tag.title = title
    file.tag.artist = author
    file.tag.images.set(3, open('cover.jpeg','rb').read(), 'image/jpeg')
    file.tag.save()
    os.rename(mp3_file, "./" + title + ".mp3")

    return title
