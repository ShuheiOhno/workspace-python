from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import CreateView #クラスベース
from django.urls import reverse_lazy


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

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'context': 'not login'})
    return render(request, 'login.html', {'context': 'get'})

# @login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object': object})

def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk) #get_object_or_404でもOK
    object.good += 1
    object.save()
    return redirect('list')

#現実的ではない
def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    print(username)
    if username in object.readtext:
        return redirect('list')
    else:
        object.read += 1
        object.readtext += object.readtext + ' ' + username
        object.save()
        return redirect('list')
    
# クラスベース
class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'sns_image')
    success_url = reverse_lazy('list')