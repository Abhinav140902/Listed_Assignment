from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

API_KEY = "AIzaSyBQLYW4iRxDdb-EY_Vl54bMkGin4E8C648"

youtube = build('youtube', 'v3', developerKey=API_KEY)

query = "openinapp.co"
max_results = 10000

youtube_channels = []

try:
    search_response = youtube.search().list(
        q=query,
        part='id',
        type='channel',
        maxResults=max_results
    ).execute()

    channel_ids = [item['id']['channelId'] for item in search_response.get('items', [])]

    for channel_id in channel_ids:
        channel_url = f"https://www.youtube.com/channel/{channel_id}"
        youtube_channels.append(channel_url)
        print(channel_url)

except HttpError as e:
    print(f"An HTTP error occurred: {e}")

#JSON
with open("youtube_channels.json", "w") as json_file:
    json.dump(youtube_channels, json_file, indent=4)

