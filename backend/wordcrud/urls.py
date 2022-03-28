from django.conf.urls import url, include
from .views import wordList

urlpatterns = [
    url(r'^list/$', wordList, name='all-word-list'),
]