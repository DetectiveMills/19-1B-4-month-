from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

# def about(request):
#     text = 'Всем привет, меня зовут гений 123. Я работаю в сети магазинов камею.'
#     return HttpResponse(text)

def index(request):
    return render(request, 'index.html')

def about(request):
    text = {
        "title": 'Этот сайт был сделан чисто ради теста. Тут собраны топ 10 самых популярных цитат из фильма "Бойцовский клуб". Приятного чтения!'
    }
    return render(request, 'about.html', text)


