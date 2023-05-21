from django.urls import path, include
from .views import rendertest ,signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # テスト用
    path('rendertest/', rendertest),

    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc ,name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
