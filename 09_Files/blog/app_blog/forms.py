from django import forms
from app_blog.models import Profile, Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class BlogForm(forms.Form):
    blog_photo = forms.ImageField(label=u"Фото блога",
                                  widget=forms.ClearableFileInput(attrs={'multiple': True}))
    blog_text = forms.CharField(label=u'Текст блога')

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(help_text='Имя')
    second_name = forms.CharField(help_text="Фамилия")
    about = forms.CharField(help_text="О себе")
    avatar = forms.ImageField(help_text="Аватар пользователя")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'second_name', 'about', 'avatar', 'password1', 'password2')


class UserEditForm(UserChangeForm):
    first_name = forms.CharField(help_text='Имя')

    class Meta:
        model = User
        fields = ('username', 'first_name')

class ProfileEditForm(forms.ModelForm):
    second_name = forms.CharField(help_text="Фамилия")
    about = forms.CharField(help_text="О себе")
    avatar = forms.ImageField(help_text="Аватар пользователя")


    class Meta:
        model = Profile
        fields = ('second_name', 'about', 'avatar')

class UploadBlogFileForm(forms.Form):
    file = forms.FileField()