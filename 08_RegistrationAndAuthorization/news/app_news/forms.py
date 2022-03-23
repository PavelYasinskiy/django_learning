from django import forms
from app_news.models import News, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        exclude = ['active_flag']


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['username', 'text_comment']


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(help_text='Имя')
    phone_number = forms.CharField(help_text='Номер телефона')
    city = forms.CharField(help_text='Город')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'phone_number', 'city', 'password1', 'password2')


# Создайте новостной сайт, у которого должны быть следующие возможности:
# регистрация пользователя;

# хранение дополнительных данных о пользователе:
# телефон, город, флаг верификации, количество опубликованных новостей.
# Реализуйте это через расширение модели профиля.

# аутентификация пользователя;
# просмотр данных аккаунта;
# пользователи должны быть разделены на три группы:
# (обычные пользователи, верифицированные пользователи и модераторы);
# возможность создания новостей.
# Должно быть доступно только верифицированным пользователям
# (для верификация необходимо решение модератора, необходимо добавить ему для этого дополнительное разрешение);
#
# публикация новости возможна только после одобрения модератором
# (необходимо добавить ему для этого дополнительное разрешение);
#
# реализуйте возможность добавления комментария к новости
# (должны выводиться под текстом новости, если комментарий оставляет
# аутентифицированный пользователь, то в шаблоне выводить имя);
#
# возможность указать тег для новости и затем фильтровать список новостей по нему и по дате создания.