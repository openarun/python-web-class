from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(requests):
    body = "<html><body><h1>Hello this is poll</h1></body></html>"
    return HttpResponse(body)