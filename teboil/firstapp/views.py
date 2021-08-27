from django.http import HttpResponse


def hellodjango(request):
    return HttpResponse('<h2>Hello Django!</h2><br><a class="me-3 py-2 text-dark text-decoration-none" '
                        'href="/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"><b>На '
                        'главную =></b></font></font></a>''<br><h3>Задание урока №1</h3>'
                        '''Создайте модуль firstapp, добавьте в него файл urls.py, создайте
                        urlpattern, подключите к этому url адресу функцию обработчик hellodjango,<br>
                        реализуйте функцию hellodjango, чтобы она с помощью метода HttpResponse
                        выводила в браузер фразу "Hello Django!".''')
