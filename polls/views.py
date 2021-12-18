from django.http import HttpResponse

# Create your views here.
# 이 뷰를 호출하려면 이와 연결된 url이 있어야한다. (같은 디렉토리내의 urls.py를 이용하자)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index")