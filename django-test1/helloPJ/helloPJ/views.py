from django.http import HttpResponse
from django.views.generic import TemplateView

# 関数ベース
def hellofunction(request):
    returnedObj = HttpResponse('<h1>hello world!</h1>')
    return returnedObj

# クラスベース
class HelloWorldClass(TemplateView):
    template_name = 'hello.html'