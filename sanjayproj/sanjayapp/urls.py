from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    
# Added on 090117
#    url(r'^sanjayapp/$', views.Mukesh, name='Mukesh'),
     url(r'^detail(?P<apps_id>)/$', views.detail, name='detail'),
     url(r'^Anu/$', views.Anu, name='Anu'),
     url(r'^Neelam/$', views.Neelam, name='Neelam'),
     url(r'^Yuvi/$', views.Yuvi, name='Yuvi'),
     url(r'^album/$', views.album, name='album'),
     url(r'^aboutus/$', views.aboutus, name='aboutus'),
     url(r'^community/$', views.community, name='community'),
     url(r'^contactus/$', views.contactus, name='contactus'),
     url(r'^signup/$', views.signup, name='signup'),
     url(r'^login/$', views.login, name='login'),
     url(r'^components/$', views.components, name='components')
]
