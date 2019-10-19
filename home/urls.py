from django.conf.urls import url
from django.urls import path, include
from home import views

app_name='home'

urlpatterns = [
    path('home/', views.home, name='name'),
    path('register/', views.register, name='register'),
    path('excel/', views.generate_excel, name='excel'),
    path('slogan/', views.slogan, name='slogan')
]
