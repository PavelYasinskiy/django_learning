from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Выведение из запоя',
        'Услуги экскаватора-погрузчика, гидромолота, ямобура'
    ]
    advertisements_1 = [
        'Помогу даром',
        'Асфальтоукладчик',
        'Python-разработчик на час'
    ]
    advertisements_2 = [
        'Отладка кода по фото',
        'Бесплатные курсы по программированию для поваров',
        'Обмен камаза на заусенцы'
    ]

    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements,
                                                                      'advertisements_1': advertisements_1,
                                                                      'advertisements_2': advertisements_2})


# def about_lst(request, *args, **kwargs):
#     abouts = [["Бесплатные объявления", 'Бесплатные объявления в вашем городе!']]
#     return render(request, 'advertisements/about_list.html', {'abouts': abouts})


# def contact_lst(request, *args, **kwargs):
#     contacts = [["8-800-708-19-45", 'sales@company.com']]
#     return render(request, 'advertisements/contact_list.html', {'contacts': contacts})


def regions_lst(request, *args, **kwargs):
    regions = ["Москва", 'Московская область', "республика Алтай", 'Вологодская область']
    return render(request, 'advertisements/regions_list.html', {'regions': regions})


def categories_lst(request, *args, **kwargs):
    categories = ["личные вещи", 'транспорт', 'хобби и отдых']
    return render(request, 'advertisements/categories_list.html', {'categories': categories})

class Regions(View):
    def get(self, request):
        reg = ["Москва", 'Московская область', "республика Алтай", 'Вологодская область']
        return render(request, 'advertisements/region.html', {'reg': reg})

    def post(self, request):
        reg = ["Успешно создан"]
        return render(request, 'advertisements/region.html', {'reg': reg})


class Advertisements(View):
    get_count = [0]
    post_count = [0]
    def get(self, request):
        advert = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Помогу даром',
            'Асфальтоукладчик',
            'Python-разработчик на час',
            'Отладка кода по фото',
            'Бесплатные курсы по программированию для поваров',
            'Обмен камаза на заусенцы'
        ]
        self.get_count[0] += 1
        return render(request, 'advertisements/advertisements_cbv.html', {'advert': advert,
                                                                          'count': self.get_count})

    def post(self, request):
        advert = ["Запрос на создание новой записи успешно выполнен."]
        self.post_count[0] += 1
        return render(request, 'advertisements/region.html', {'advert': advert,
                                                              'count': self.post_count})


class Contacts(TemplateView):
    template_name = 'advertisements/contact_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["address"] = "Москва, Новослободская набережная, 3 стр.2"
        context["phone"] = "8(913)6543211"
        context["mail"] = "shop@shopper.com"
        return context


class About(TemplateView):
    template_name = 'advertisements/about_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Бесплатные объявления"
        context["description"] = 'Бесплатные объявления в вашем городе!'
        context["title"] = "Бесплатные объявления"
        return context

class MainMenu(View):

    def get(self, request):
        categories = ["личные вещи", 'транспорт', 'хобби и отдых']
        reg = ["Москва", 'Московская область', "республика Алтай", 'Вологодская область']
        return render(request, 'advertisements/advertisement_list.html', {'categories': categories,
                                                                          'reg': reg})

#
# Создайте главную страницу по адресу /. Нужно использовать представление-класс.
#
# метод get должен возвращать html форму,
# на которой должны быть представлены следующие элементы:
# выбора категории из списка, выбор региона из списка,
# текстовое поле для ввода названия объявления и кнопка “Найти”.
# (Значения для выбора нужно передавать из представления)
#
