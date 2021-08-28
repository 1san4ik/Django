from django.shortcuts import render, redirect
from django.http import HttpResponse


def second_render(request):
    return render(request, 'second_app/second_render.html')


def second_redirect(request):
    return redirect('second_render', permanent=False)


def httpresponse(request):
    return HttpResponse('<h2>second_app используя функцию HttpResponse</h2>'
                        '<br><a class="me-3 py-2 text-dark text-decoration-none" '
                        'href="/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"><b>На'
                        'главную =></b></font></font></a>''<br><h3>Задание урока №2</h3>'
                        '''Подключите second_app в проект, создайте несколько url-адресов, привяжите к ним свои <br>
                        функции обработчики, которые будут использовать внутри себя разные методы ответов: render, <br>
                        redirect, HttpResponse.''')
