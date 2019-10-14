from django.conf.urls import url
from django.urls import path, include
from home import views

app_name='home'

urlpatterns = [
    path('home/', views.home, name='name'),
    path('register/', views.register, name='register')
]
