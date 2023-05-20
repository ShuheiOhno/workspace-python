from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'), #クラスの場合、as_view()を付ける
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
]
