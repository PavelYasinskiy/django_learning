from django.http import HttpResponse
from random import shuffle
from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        for_rand = ['<li>Установить python</li>', '<li>Установить django</li>', '<li>Запустить сервер</li>',
           '<li>Порадоваться результату</li>']
        for_rand = shuffle(for_rand)
        return HttpResponse('<ul>'
                            f'<li>{for_rand[0]}</li>'
                            f'<li>{for_rand[1]}</li>'
                            f'<li>{for_rand[2]}</li>'
                            f'<li>{for_rand[3]}</li>'
                            '</ul>')
