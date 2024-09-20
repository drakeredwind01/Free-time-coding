from pytube import Playlist

# Replace the URL with your playlist URL
playlist_url = 'https://youtube.com/playlist?list=PL4cUxeGkcC9iqfAag3a_BKEX1N43uJutw'
playlist = Playlist(playlist_url)

print(f'Downloading videos from playlist: {playlist.title}')

for video in playlist.videos:
    print(f'Title: {video.title}')
    print(f'URL: {video.watch_url}')
    # If you want to download the video, uncomment the next line
    # video.streams.get_highest_resolution().download()
