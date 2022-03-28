from http.client import HTTPResponse
from django.shortcuts import render

from django.http.response import HttpResponse
from .models import Words
from django.core import serializers

import json

# Create your views here.

def greeting(request):
    return HttpResponse('Hi Sairam')

def wordList(request):
    if request.method == 'GET':
        print('get request received')
    tmpJson = serializers.serialize("json", Words.objects.all())
    tmpObj = json.loads(tmpJson)
    return HttpResponse(json.dumps(tmpObj))

def updateWord(request, pk):
    if(request.method == "PUT"):
        print(Words.objects.get(pk=pk))
        temp = Words.objects.get(pk=pk)

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['word']
        print(content)
        temp.word = content
        temp.save()
        tmpJson = serializers.serialize("json", Words.objects.all())
        tmpObj = json.loads(tmpJson)
        return HttpResponse(json.dumps(tmpObj))

def createWord(request):
    return HttpResponse('word created')

def deleteWord(request, pk):
    return HttpResponse('word deleted')