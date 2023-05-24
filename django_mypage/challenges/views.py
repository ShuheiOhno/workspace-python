from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
# def index(request):
#     return HttpResponse("Work!")

# def february(request):
#     return HttpResponse("Fabruary")

monthly_challenges = {
    "january": "1",
    "february": "2",
    "march": "3",
    "april": "4",
    "may": "5",
    "june": "6",
    "july": "7",
    "august": "8",
    "september": "9",
    "october": "10",
    "november": "11",
    "december": "12",
}

def monthly_chanllenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported.")
    
 


def test():
    return "fff"