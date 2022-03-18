from django import forms
from app_news.models import News, Comments


class NewsForm(forms.ModelForm):


    class Meta:
        model = News
        fields = '__all__'


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['username', 'text_comment']



