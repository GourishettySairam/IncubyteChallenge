from django.conf.urls import url, include
from numpy import delete
from .views import wordList, updateWord, deleteWord, createWord
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^list/$', csrf_exempt(wordList), name='all-word-list'),
    url(r'^updateWord/(?P<pk>[\d]+)/$', csrf_exempt(updateWord), name='update-word'),
    url(r'^createWord/$', csrf_exempt(createWord), name='create-word'),
    url(r'^deleteWord/(?P<pk>[\d]+)/$', csrf_exempt(deleteWord), name='delete-word')
]