from http.client import HTTPResponse
from django.shortcuts import render

from django.http.response import HttpResponse

# Create your views here.

def greeting(request):
    return HttpResponse('Hi Sairam')

def wordList(request):
    return HttpResponse('returning a list of words')