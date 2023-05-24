from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.
# def index(request):
#     return HttpResponse("Work!")

# def february(request):
#     return HttpResponse("Fabruary")

monthly_challenges = {
    "january": "1月",
    "february": "2月",
    "march": "3月",
    "april": "4月",
    "may": "5月",
    "june": "6月",
    "july": "7月",
    "august": "8月",
    "september": "9月",
    "october": "10月",
    "november": "11月",
    "december": "12月",
}

def monthly_chanllenge_by_number(request, month):
    months = list(monthly_challenges.keys()) #list() ほかのデータ型をリスト型に変換

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        print(challenge_text)
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported.")
    
 


def test():
    return "fff"