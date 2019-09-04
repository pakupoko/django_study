from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    msg = '쉬바 저 망할것 같아요 어떡하죠? 내 인생'
    return render(request, 'home/index.html', {'message':msg, 'createDate':now})