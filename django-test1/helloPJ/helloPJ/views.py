from pathlib import Path
from django.http import HttpResponse
from django.views.generic import TemplateView

# 関数ベース
def hellofunction(request):
    returnedObj = HttpResponse('<h1>hello world!</h1>')
    return returnedObj

# クラスベース
class HelloWorldClass(TemplateView):
    template_name = 'hello.html'

# 確認用
def checkview(request):
    print('##################')
    print(Path()) #.
    print(Path(__file__)) #このファイルのパス
    print(Path(__file__).resolve()) #このファイルの絶対パス
    print(Path(__file__).resolve().parent) #このファイルの一つ上のフォルダ
    print(Path(__file__).resolve().parent.parent) #BASE_DIRと同じ
    return HttpResponse('')