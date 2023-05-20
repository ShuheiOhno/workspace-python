from django.urls import path, include
from .views import TodoList, TodoDetail

urlpatterns = [
    path('list/', TodoList.as_view()), #クラスの場合、as_view()を付ける
    path('detail/<int:pk>', TodoDetail.as_view()),
]
