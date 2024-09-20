from pytube import Playlist
from datetime import timedelta


def get_video_details(playlist_url):
    playlist = Playlist(playlist_url)
    total_watch_time = timedelta()

    # Fetch playlist metadata using pytube
    playlist_title = playlist.title
    num_of_videos = len(playlist.video_urls)

    print(f'Playlist Title: {playlist_title}')
    print(f'Number of Videos: {num_of_videos}')

    video_details = []

    for video in playlist.videos:
        video_title = video.title
        video_duration = video.length
        video_runtime = str(timedelta(seconds=video_duration))

        total_watch_time += timedelta(seconds=video_duration)

        video_details.append({
            "title": video_title,
            "runtime": video_runtime,
        })

        print(f'Title: {video_title},')
        print(f'Runtime: {video_runtime}\n')

    print(f'Total Watch Time of Playlist: {str(total_watch_time)}')


# URLs of playlists
playlist_urls = [
    'https://www.youtube.com/playlist?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX',
    'https://www.youtube.com/playlist?list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau',
    'https://www.youtube.com/playlist?list=PLVBKjEIdL9bvCdI4l1Emvbezv10GjUaLk',
    'https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p'
]

for url in playlist_urls:
    print(f'Fetching details for playlist: {url}\n')
    get_video_details(url)
    print('-' * 40)
