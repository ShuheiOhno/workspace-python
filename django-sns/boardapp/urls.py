from django.urls import path, include
from .views import rendertest ,signupfunc, loginfunc, listfunc

urlpatterns = [
    # テスト用
    path('rendertest/', rendertest),

    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc ,name='list'),
]
