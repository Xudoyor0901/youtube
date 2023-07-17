import pytube

link = "https://youtu.be/25xUoLye53w"
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("downloader", link)
