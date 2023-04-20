from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import * 
from app.models import *

def insert_topic(request):
    TOF=Topicforms()
    d={'TOF':TOF}
    if request.method=='POST':
        TFD=Topicforms(request.POST)
        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WOF=Webpageform()
    d={'WOF':WOF}
    if request.method=='POST':
        WFD=Webpageform(request.POST)
        if WFD.is_valid():
            topic_name=WFD.cleaned_data['topic_name']
            name=WFD.cleaned_data['name']
            url=WFD.cleaned_data['url']
            email=WFD.cleaned_data['email']
            TO=Topic.objects.get(topic_name=topic_name)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
            WO.save()
            WQS=Webpage.objects.all()
            d1={'WQS':WQS}
            return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    AOF=Accessrecordform()
    d={'AOF':AOF}
    if request.method=='POST':
        AFD=Accessrecordform(request.POST)
        if AFD.is_valid():
            name=AFD.cleaned_data['name']
            author=AFD.cleaned_data['author']
            date=AFD.cleaned_data['date']
            WO=Webpage.objects.get(name=name)
            WO.save()
            AO=Accessrecord.objects.get_or_create(name=WO,author=author,date=date)[0]
            AO.save()
            AQS=Accessrecord.objects.all()
            d1={'AQS':AQS}
            return render(request,'display_aeccessrecord.html',d1)
    return render(request,'insert_aeccessrecord.html',d)
