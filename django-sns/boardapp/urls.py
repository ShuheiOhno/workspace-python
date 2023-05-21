from django.urls import path, include
from .views import rendertest ,signupfunc, loginfunc

urlpatterns = [
    # テスト用
    path('rendertest/', rendertest),

    path('signup/', signupfunc),
    path('login/', loginfunc)

]
