import os
from datetime import datetime, time
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse

# Create your views here.

def index_views(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"<h1>Выбирите Раздел</h1>"
                        f"<a href={reverse('time')}>Узнать текущее время</a>"
                        f"<br>"
                        f"<a href={reverse('workdir')}>Содержимое рабочей директории</a>")

def time_views(request: HttpRequest) -> HttpResponse:
    time_now = datetime.now().time()
    return HttpResponse(f"<h1>Текущее время: {time_now}</h2><br><a href={reverse('index')}>Вернутся на главную страницу</a>")

def workdir_views(request: HttpRequest) -> HttpResponse:
    out_command = os.popen('pwd').read()
    work_dir = os.popen('ls').read().strip()
    dir = work_dir.split('\n')
    dir_new = ', '.join(dir)
    return HttpResponse(f"<h1>Рабочий католог: {out_command}</h1>"
                        f"<h1>Содержимое каталога: {dir_new}</h1>"
                        f"<br>" 
                        f"<a href={reverse('index')}>Вернутся на главную страницу</a>")