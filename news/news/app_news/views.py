from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from app_news.models import News, Comments, Profile
from app_news.forms import NewsForm, CommentsForm, RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin

class NewsFormView(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/news_add.html', context={'news_form': news_form})

    def post(self, request):
        f = NewsForm(request.POST)
        new_article = f.save()
        return HttpResponseRedirect('/news/')


class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'app_news.add_news'
    model = News
    fields = ['title', 'description', 'tag', 'active_flag']
    template_name = 'app_news/news_add.html'

    def get_success_url(self):
        return reverse_lazy('add')

    def post(self, request):
        form = NewsForm(request.POST)
        new_news = form.save(commit=False)
        if request.user.is_authenticated:
            new_news.author = request.user
        if request.user.has_perm('app.news.can_publish'):
            new_news.save()
        else:
            new_news.active_flag = False
            new_news.save()
        return HttpResponseRedirect(reverse('add'))

    # from = CommentsForm(request.POST)
    # new_comment = form.save(commit=False)
    # new_comment.article = self.get_object()
    # if request.user.is_authenticated:
    #     new_comment.user = request.user
    # new_comment.save()


class NewsModeratorUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_news.change_news'
    model = News
    fields = ['title', 'description', 'tag', 'active_flag']
    template_name_suffix = '_edit'

    def get_success_url(self):
        return reverse('news')

class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'app_news.change_news'
    model = News
    fields = ['title', 'description', 'tag']
    template_name_suffix = '_edit'

    def get_success_url(self):
        return reverse('news')



# class NewsEditFormView(View):
#     def get(self, request, pk):
#         news = News.objects.get(id=pk)
#         news_form = NewsForm(instance=news)
#         return render(request, 'app_news/edit.html', context={'news_form': news_form,
#                                                               'new_id': pk})
#
#     def post(self, request, pk):
#         news = News.objects.get(id=pk)
#         news_form = NewsForm(request.POST, instance=news)
#
#         if news_form.is_valid():
#             news.save()
#         return render(request, 'app_news/edit.html', context={'news_form': news_form,
#                                                               'new_id': pk})


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = "news_list"



class NewsDetailView(DetailView, User):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentsForm()
        return context

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        new_comment = form.save(commit=False)
        new_comment.article = self.get_object()
        if request.user.is_authenticated:
            new_comment.user = request.user
        new_comment.save()

        return HttpResponseRedirect(reverse('news-detail', args=[f'{pk}']))

class UserLoginView(LoginView):
    template_name = 'app_news/login.html'

class UserLogoutView(LogoutView):
    template_name = 'app_news/logout.html'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            city = form.cleaned_data.get('city')
            phone_number = form.cleaned_data.get('phone_number')
            Profile.objects.create(
                user=user,
                city=city,
                phone_number=phone_number
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile_page')
    else:
        form = RegisterForm()
    return render(request, 'app_news/register.html', {'form': form})


def profile_detail_view(request):
    return render(request, 'app_news/profile_detail.html')

def change_tags(request):
    if request.user.has_perm('tags.add_tag'):
        ...
    if request.user.has_perms(['tags.add_tag', 'tags.change_tag']):
        ...