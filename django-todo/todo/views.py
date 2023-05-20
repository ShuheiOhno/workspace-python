from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel #保存するモデルを指定
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list') #保存後の遷移先 urls.pyのpathの第二引数に、name='list'を指定