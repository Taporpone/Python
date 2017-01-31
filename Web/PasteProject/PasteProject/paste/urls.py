from django.conf.urls import patterns, url
from paste import views

urlpatterns = patterns('',
url(r'^$',views.index,name='index'),
url(r'^about/',views.about,name='about'),
url(r'^mypastas/',views.mypastas,name='mypastas'),
url(r'^profile/',views.profile,name='profile'),
)
