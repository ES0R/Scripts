


from pytube import YouTube
from sys import argv
import os

if not os.path.exists("Vidoes"):
    os.mkdir("Vidoes")
os.chdir('Vidoes')

link = argv[1]
yt = YouTube(link)

title = yt.title

video = yt.streams.get_highest_resolution()
video.download()

if title:
    print("{0} succesfully downloaded to: {1}".format(title,os.getcwd()))