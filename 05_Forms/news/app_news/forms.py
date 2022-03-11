from django import forms
# from app_news.models import User
from app_news.models import News, Comments
# import datetime
# from django.core.exceptions import ValidationError

class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = '__all__'


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = '__all__'


# class UserForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = '__all__'


    # username = forms.CharField()
    # password = forms.CharField()
    # first_name = forms.CharField()
    # second_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()
    # birthday = forms.DateField()
    #
    # def clean_birthday(self):
    #     data = self.cleaned_data['birthday']
    #     today = datetime.date.today()
    #     year_delta = (today - data).days / 365
    #     if year_delta < 18:
    #         raise ValidationError('Вы моложе 18! Позовите родителей!')
    #     return data
    #
    # def clean(self):
    #     cleaned_data = super(UserForm, self).clean()
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')
    #     if first_name == 'Иван' and last_name == 'Иванов':
    #         msg = 'Прикалываться нельзя'
    #         self.add_error('first_name', msg)
    #         self.add_error('last_name', msg)