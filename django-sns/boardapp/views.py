from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

# テスト用
def rendertest(request):
    return render(request, 'test.html', {'some':100})

# Create your views here.
def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザは登録されています'})
    return render(request, 'signup.html', {})