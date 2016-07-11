from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import loader
from django.contrib.auth import logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from twapp.models import User,Search
from random import randint
import twitterapi as tw
import WC
import ytube
import wiki
import news

@login_required
def main_page(request):
    variables = RequestContext(request,{'user':request.user})
    return render_to_response('twapp/main_page.html',variables)
    
@login_required
def twitter_page(request):
    query=request.GET.get('query')
    q,dummy =Search.objects.get_or_create(query=query,user=request.user)
    text,tweets=tw.search_twitter(query)
    wcurl=WC.wcloud(text,query)
    variables = RequestContext(request,{'user':request.user,'query':query,'wcurl':wcurl,'tweets':tweets})
    return render_to_response('twapp/twitter_page.html',variables)

@login_required
def video_page(request):
    query=request.GET.get('query')
    q,dummy =Search.objects.get_or_create(query=query,user=request.user)
    videos=ytube.get_videos(query)
    variables = RequestContext(request,{'user':request.user,'query':query,'videos':videos})
    return render_to_response('twapp/video_page.html',variables)

@login_required   
def video_download_page(request):
    video_id=request.GET.get('id')
    data=ytube.get_video_data(str(video_id))
    variables = RequestContext(request,{'user':request.user,'data':data})
    return render_to_response('twapp/video_download_page.html',variables)    

@login_required
def wiki_page(request):
    query=request.GET.get('query')
    q,dummy =Search.objects.get_or_create(query=query,user=request.user)
    wpage=wiki.get_wiki(query)
    variables = RequestContext(request,{'user':request.user,'query':query,'wpage':wpage})
    return render_to_response('twapp/wiki_page.html',variables)

@login_required
def news_page(request):
    query=request.GET.get('query')
    q,dummy =Search.objects.get_or_create(query=query,user=request.user)
    content=news.get_news(query)
    wcurl=WC.wcloud((' '.join(x['title'] + x['content_snippet'] for x in content[:7])),query)
    variables = RequestContext(request,{'user':request.user,'query':query,'content':content,'wcurl':wcurl})
    return render_to_response('twapp/news_page.html',variables)
    
def about_page(request):
    variables = RequestContext(request,{'user':request.user})
    return render_to_response('twapp/about_page.html',variables)









    
    
        
