from http.client import HTTPResponse
from django.shortcuts import render, get_object_or_404

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
    return HttpResponse(json.dumps({'data': "invalid method"}), status=405)

def updateWord(request, pk):
    if(request.method == "PUT"):
        # print(Words.objects.get(pk=pk))
        try:
            temp = get_object_or_404(Words, pk=pk)
        except:
            return HttpResponse(status=404)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['word']
        print(content)
        temp.word = content
        temp.save()
        tmpJson = serializers.serialize("json", Words.objects.all())
        tmpObj = json.loads(tmpJson)
        return HttpResponse(json.dumps(tmpObj))
    return HttpResponse(json.dumps({'data': "invalid method"}), status=405)

def createWord(request):
    if(request.method == "POST"):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['word']

        Words.objects.create(word=content)
        tmpJson = serializers.serialize("json", Words.objects.all())
        tmpObj = json.loads(tmpJson)
        return HttpResponse(json.dumps(tmpObj))
        # return HttpResponse('word created')
    return HttpResponse(json.dumps({'data': "invalid method"}), status=405)

def deleteWord(request, pk):
    return HttpResponse('word deleted')