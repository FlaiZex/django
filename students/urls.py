from django.contrib.auth import login
from django.urls import path

from .views import index, groups, about, teachers, students

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('students/', students, name='students'),
    path('teachers/', teachers, name='teachers'),
    path('groups/', groups, name='groups'),
    path('login', login, name='login'),
    path('groups/<slug:group>/', groups),
    path('about/', about),
]