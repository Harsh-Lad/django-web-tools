from django.urls import path
from urlShortner import views

urlpatterns = [
    path('', views.index),
    path('url_shortner/',views.urlShortner),
    path('generate_qr/',views.generate_qr),
    path('phoneInfo/',views.phoneInfo),
    path('randJokes/',views.randJokes),
    path('news/',views.news),


    
]
