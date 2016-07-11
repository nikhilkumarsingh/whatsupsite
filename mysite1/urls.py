from django.conf.urls import url,include
from django.contrib import admin
from twapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^about/',views.about_page),
    url(r'^$',views.main_page),
    url(r'^tweets/',views.twitter_page),
    url(r'^videos/$',views.video_page),
    url(r'^download/$',views.video_download_page),
    url(r'^wiki/$',views.wiki_page),
    url(r'^news/$',views.news_page),
]
