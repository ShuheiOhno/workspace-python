from django.urls import path, include
from .views import rendertest ,signupfunc

urlpatterns = [
    # テスト用
    path('rendertest/', rendertest),

    path('signup/', signupfunc),

]
