from django.urls import path, include
from .views import TodoList

urlpatterns = [
    path('list/', TodoList.as_view()), #クラスの場合、as_view()を付ける
]
