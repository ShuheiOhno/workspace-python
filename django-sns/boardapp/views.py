from django.shortcuts import render

# テスト用
def rendertest(request):
    return render(request, 'test.html', {'some':100})

# Create your views here.
def signupfunc(request):
    return render(request, 'signup.html', {})