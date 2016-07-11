import wikipedia
import requests

def get_wiki(query):
   wpage={}
   try:
    wpage['title']=(wikipedia.search(query))[0]
    wpage['summary']=wikipedia.summary(wpage['title'])
    try:
      r=requests.get('http://en.wikipedia.org/w/api.php?action=query&titles='+wpage['title']+'&prop=pageimages&format=json&pithumbsize=200')
      json_dict=r.json()
      sub_dict=json_dict['query']['pages']
      wpage['image']=sub_dict[sub_dict.keys()[0]]['thumbnail']['source']
    except:
      wpage['image']="/static/other/noimage.png"
   except:
      wpage['title']=query
      wpage['summary']='No wiki pages found for this query. :('
      wpage['image']="/static/other/noimage.png"
   return wpage




