from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# def index(request):
#     return HttpResponse("Work!")

# def february(request):
#     return HttpResponse("Fabruary")


monthly_challenges = {
    "january": "this is 1月",
    "february": "this is 2月",
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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_chanllenge_by_number(request, month):
    months = list(monthly_challenges.keys()) #list() ほかのデータ型をリスト型に変換

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported.")
    
 


def test():
    return "fff"