from django.conf.urls import url
from django.contrib import admin
from twapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.main_page),
    url(r'^search/$',views.result_page),
]
