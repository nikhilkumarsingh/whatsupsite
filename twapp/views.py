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
import maskutil

def main_page(request):
    variables = RequestContext(request)
    return render_to_response('twapp/main_page.html',variables)
    

def result_page(request):
    query=request.GET.get('query')
    q,dummy =Search.objects.get_or_create(query=query)
    mask=maskutil.get_masks()
    index=randint(0,len(mask))
    url=WC.wcloud(tw.search_twitter(query),mask[index],query)
    variables = RequestContext(request,{'query':query,'url':url})
    return render_to_response('twapp/result_page.html',variables)





    
        
