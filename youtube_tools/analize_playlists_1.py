from pytube import Playlist
from bs4 import BeautifulSoup
import requests
from datetime import timedelta

def get_playlist_metadata(url):
    """Scrape playlist metadata (creator, views, last updated)"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract playlist title
    title = soup.find('h1', class_='title').text.strip()

    # Extract creator/maker
    maker = soup.find('a', class_='yt-simple-endpoint style-scope yt-formatted-string').text.strip()

    # Extract views
    views_text = soup.find('span', class_='view-count style-scope yt-formatted-string').text.strip()
    views = views_text.split()[0]  # Extract just the number of views

    # Extract last updated
    last_updated_text = soup.find('span', class_='style-scope yt-formatted-string').text.strip()

    return title, maker, views, last_updated_text

def get_video_details(playlist_url):
    playlist = Playlist(playlist_url)
    total_watch_time = timedelta()
    video_details = []

    # Fetch metadata
    playlist_title, maker, views, last_updated = get_playlist_metadata(playlist_url)

    print(f'Playlist Title: {playlist_title}')
    print(f'Maker: {maker}')
    print(f'Last Updated: {last_updated}')
    print(f'Number of Videos: {len(playlist.video_urls)}')
    print(f'Views: {views}')

    for video in playlist.videos:
        video_title = video.title
        video_duration = video.length
        video_runtime = str(timedelta(seconds=video_duration))

        total_watch_time += timedelta(seconds=video_duration)

        video_details.append({
            "title": video_title,
            "runtime": video_runtime,
        })

        print(f'Title: {video_title}')
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
