from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from youtube_dl import YoutubeDL


DEVELOPER_KEY = "AIzaSyApuFoKxVMRQ2einlsA0rkx2S4WJjJIh34"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_videos(query):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)
  search_response = youtube.search().list(q=query,part="id,snippet",maxResults=7).execute()
  videos = []
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      dict={}
      dict['id']=search_result["id"]["videoId"]
      dict['thumbnail']=search_result['snippet']['thumbnails']['default']['url']
      dict['title']=search_result['snippet']['title']
      videos.append(dict)
  return videos


def get_video_data(video_id):
   data={}
   video_url = 'https://www.youtube.com/watch?v='+video_id
   ydl_opts = {
    'format': 'bestaudio/mp3',
    
    }
   ydl = YoutubeDL(ydl_opts)
   r = ydl.extract_info(video_url, download=False)
   data['aud_url']=r['url']
   

   ydl = YoutubeDL()
   r = ydl.extract_info(video_url, download=False)
   data['vid_url']=r['url']
   data['title']=r['title']
   data['thumbnail']=r['thumbnails'][0]['url']

   return data

