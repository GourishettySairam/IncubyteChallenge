from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404

from django.http.response import HttpResponse
from .models import Words
from django.core import serializers

import json

# Create your views here.

def returnWords():
    tmpJson = serializers.serialize("json", Words.objects.all())
    tmpObj = json.loads(tmpJson)
    return HttpResponse(json.dumps(tmpObj))

def wordList(request):
    if request.method == 'GET':
        return returnWords()
    return HttpResponse(json.dumps({'data': "invalid method"}), status=405)

def updateWord(request, pk):
    if(request.method == "PUT"):
        try:
            temp = get_object_or_404(Words, pk=pk)
        except:
            return HttpResponse(json.dumps({'data': 'data not present'}), status=404)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['word']
        temp.word = content
        temp.save()
        return returnWords()
    return HttpResponse(json.dumps({'data': "invalid method"}), status=405)

def createWord(request):
    if(request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['word']

        Words.objects.create(word=content)
        return returnWords()
    return HttpResponse(json.dumps({'data': "invalid method"}), status=405)

def deleteWord(request, pk):
    if(request.method == "DELETE"):
        temp = get_object_or_404(Words, pk=pk)
        temp.delete()
        return returnWords()
    return HttpResponse(json.dumps({'data': "invalid method"}), status=405)
