from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Students

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Студенты", 'url_name': 'students'},
        {'title': "Преподаватели", 'url_name': 'teachers'},
        {'title': "Войти", 'url_name': 'login'}]
# def index(request):
#     return HttpResponse('Страница приложения students')
def index(request):
    students = Students.objects.all()
    context = {
        'students': students,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'students/index.html', context=context)


def groups(request, group):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Страница приложения students.<h1>\
                        </h1><h2>{group}<h2>')

def about(request):
    return render(request, 'students/about.html', {'menu': menu, 'title': 'О сайте'})

def students(request):
    return HttpResponse("Студенты")

def teachers(request):
    return HttpResponse("Преподователи")

def login(request):
    return HttpResponse("Авторизация")











