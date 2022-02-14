from django.http import HttpResponse
from random import choice
from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        for_rand = ['<li>Установить python</li>', '<li>Установить django</li>', '<li>Запустить сервер</li>',
           '<li>Порадоваться результату</li>']
        return HttpResponse('<ul>'
                            f'{choice(for_rand)}'
                            f'{choice(for_rand)}'
                            f'{choice(for_rand)}'
                            f'{choice(for_rand)}'
                            '</ul>')
