from _csv import reader

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.views import LoginView, LogoutView
from app_blog.forms import RegisterForm, UserEditForm, ProfileEditForm, BlogForm, UploadBlogFileForm
from app_blog.models import Profile, Blog, BlogImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.core.files.base import ContentFile

def profile_detail_view(request):
    return render(request, 'app_blog/profile_detail.html')

class UserLoginView(LoginView):
    template_name = 'app_blog/login.html'

class UserLogoutView(LogoutView):
    template_name = 'app_blog/logout.html'

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            second_name = form.cleaned_data.get('second_name')
            about = form.cleaned_data.get('about')
            avatar = form.cleaned_data.get('avatar')
            Profile.objects.create(
                user=user,
                second_name=second_name,
                about=about,
                avatar=avatar,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile_page')
    else:
        form = RegisterForm()
    return render(request, 'app_blog/register.html', {'form': form})

def profile_user_edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль успешно изменён')
            return redirect('/profile_page')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'app_blog/profile_edit.html', {'user_form': user_form, 'profile_form': profile_form})

def blog_add(request):
    if request.method == 'GET':
        form = BlogForm()
        return render(request, 'app_blog/blog_add.html', {'form': form})
    elif request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = Blog.objects.create(author=request.user,
                                           blog_text=form.cleaned_data['blog_text'])
            for f in request.FILES.getlist('blog_photo'):
                data = f.read()
                photo = BlogImage(to_blog=blog)
                photo.blog_photo.save(f.name, ContentFile(data))
                photo.save()
            return redirect('/blog')
        else:
            return render(request, 'app_blog/blog_add.html', {'form': form})

class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'
    context_object_name = "blog_list"


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogImage.objects.filter(to_blog_id=self.object.pk).all()
        print(BlogImage.objects.filter(to_blog_id=self.object.pk).all())
        return context

def update_blog(request):
    if request.method == 'POST':
        form = UploadBlogFileForm(request.POST, request.FILES)
        if form.is_valid():
            update_file = form.cleaned_data['file'].read()
            update_blog = update_file.decode('utf-8').split('\n')
            csv_reader = reader(update_blog, delimiter=';')
            for row in csv_reader:
                print(row)
                Blog.objects.create(
                    blog_text=row[0],
                    public_date=row[1],
                    author=request.user
                )

            return redirect('/blog')
    else:
        form = UploadBlogFileForm()
    return render(request, 'app_blog/upload_to_blog.html', {'form': form})