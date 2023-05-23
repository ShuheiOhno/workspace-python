from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# def index(request):
#     return HttpResponse("Work!")

# def february(request):
#     return HttpResponse("Fabruary")

def monthly_challenge(request, month):
    challenge_text = None
    print(request)
    if month == "january":
        challenge_text = "january"
    elif month == "february":
        challenge_text = "february"
        print('aaa')
    elif month == "march":
        challenge_text = "march"
    else:
        return HttpResponseNotFound("This month is not supported.")

    return HttpResponse(challenge_text)


def test():
    return "fff"