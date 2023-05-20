from django.http import HttpResponse

def hellofunction(request):
    returnedObj = HttpResponse('<h1>hello world!</h1>')
    return returnedObj