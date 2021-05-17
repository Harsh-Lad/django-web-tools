from django.shortcuts import render, HttpResponse
import pyshorteners
import png
import pyqrcode
from PIL import Image
from .models import Images
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import json
from jokeapi import Jokes
from gnews import GNews



# Create your views here.

s = pyshorteners.Shortener()

def index(request):
    return render(request,'index.html')

def urlShortner(request):
    if request.method == "POST":
        url = request.POST.get('url')
        shortened_link = s.isgd.short(url)
        param = {'link':shortened_link}
        return render(request,'url.html',param)
    return render(request,'url.html')

def generate_qr(request):
    if request.method == "POST":
        url = request.POST.get('url')
        qr_url = Images(name=url)
        qr_url.save()
        image = True
        qr = Images.objects.filter(name__icontains=url).last()
        print(qr)
        param = {'image':image,'img':qr}
        return render(request,'qr.html',param)
    return render(request,'qr.html')

def phoneInfo(request):
    if request.method == "POST":
        number = request.POST.get('number')
        response = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key=84fb0b8e29e942368c4c2cbd0dbc695f&phone={number}")
        a = response.content
        content = response.json
        param = {'content':content}
        return render(request,'phoneInfo.html',param)
    return render(request,'phoneInfo.html')

def randJokes(request):
    if request.method == "POST":
        j = Jokes()
        joke = j.get_joke(category=['programming','pun','misc'])  
        present = True
        param = {'joke':joke,'present':present}
        return render(request, 'jokes.html',param)
    return render(request, 'jokes.html')

def news(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        google_news = GNews()
        json_resp = google_news.get_news(query)
        data = json_resp
        param = {'data':data}
        return render(request,'news.html', param)
    return render(request,'news.html')


    