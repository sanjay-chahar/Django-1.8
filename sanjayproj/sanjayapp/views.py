from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Host
from .models import Apps
from .models import Musician
from .models import Album

def base(request):
    musician_list = Musician.objects.all()
    context = { "musician_list": musician_list}
    return render(request, 'sanjayapp/base.html', context) 


def index(request):
#    return HttpResponse("Hello, world. You're at the sanjayapp index.")
# Added on 050117
     all_hosts = Host.objects.all()
     html = ''
     for host in all_hosts:
        url = '/sanjayapp/' + str(host.name) + '/'
        html += '<a href="' + url + '">' + host.name + '</a><br>'
     return HttpResponse(html)
    
# Added on 090117
def detail(request, apps_id):
    return HttpResponse("You're looking at question %s." % apps_id)

# Added on 100117
def Anu(request):
#    return HttpResponse("Anu you are under testing")
    apps_list = Apps.objects.all()
    for apps in apps_list:
       queryset = str(apps.applicationname)
    context = {
          "queryset": queryset}
    return render(request, 'sanjayapp/anu.html', context)

def Neelam(request):
    return HttpResponse("Hello Bibi you dont need to take tension feel happy ")

def Yuvi(request):
    musician_list = Musician.objects.all()
    context = { "musician_list": musician_list}
    return render(request, 'sanjayapp/Yuvi.html', context)

def album(request):
    album_list = Album.objects.all()
    context = { "album_list": album_list}
    return render(request, 'sanjayapp/album.html', context)

# Adde on 170117

def components(request):
    album_list = Album.objects.all()
    context = { "album_list": album_list}
    return render(request, 'sanjayapp/components.html', context)

def aboutus(request):
    apps_list = Apps.objects.all()
    for apps in apps_list:
       queryset = str(apps.applicationname)
    context = {
          "queryset": queryset}
    return render(request, 'sanjayapp/aboutus.html', context)



def community(request):
    apps_list = Apps.objects.all()
    for apps in apps_list:
       queryset = str(apps.applicationname)
    context = {
          "queryset": queryset}
    return render(request, 'sanjayapp/community.html', context)


def contactus(request):
    apps_list = Apps.objects.all()
    for apps in apps_list:
       queryset = str(apps.applicationname)
    context = {
          "queryset": queryset}
    return render(request, 'sanjayapp/contactus.html', context)



def signup(request):
    apps_list = Apps.objects.all()
    for apps in apps_list:
       queryset = str(apps.applicationname)
    context = {
          "queryset": queryset}
    return render(request, 'sanjayapp/signup.html', context)


def login(request):
    apps_list = Apps.objects.all()
    for apps in apps_list:
       queryset = str(apps.applicationname)
    context = {
          "queryset": queryset}
    return render(request, 'sanjayapp/login.html', context)
