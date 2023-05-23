from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Work!")

def february(request):
    return HttpResponse("Fabruary")