from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
# from app_news.forms import UserForm
from django.views import View
# from app_news.models import User
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse

from app_news.models import News, Comments
from app_news.forms import NewsForm, CommentsForm

class NewsFormView(View):
    def get(self, request):
        news_form = NewsForm()

        return render(request, 'app_news/news_add.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news/')
        return render(request, 'app_news/news_add.html', context={'news_form': news_form})



class CommentsFormView(SingleObjectMixin, FormView):
    template_name = 'app_news/news_detail.html'
    form_class = CommentsForm
    model = News

    def post(self, request, *args, **kwargs):
        comments_form = CommentsForm(request.POST)
        if comments_form.is_valid():
            Comments.objects.create(**comments_form.cleaned_data)
            return HttpResponseRedirect('./')
        return render(request, 'app_news/news_detail.html', context={'comments_form': comments_form})

    def get_success_url(self):
        return reverse('news-detail', kwargs={'pk': self.object.pk})


class NewsEditFormView(View):
    def get(self, request, new_id):
        news = News.objects.get(id=new_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/edit.html', context={'news_form': news_form,
                                                              'new_id': new_id})

    def post(self, request, new_id):
        news = News.objects.get(id=new_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
        return render(request, 'app_news/edit.html', context={'news_form': news_form,
                                                              'new_id': new_id})


class NewsView(View):

    def get(self, request, *args, **kwargs):
        view = NewsDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentsFormView.as_view()
        return view(request, *args, **kwargs)

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = "news_list"
    queryset = News.objects.all().order_by()



class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentsForm()
        return context





# class UserFormView(View):
#
#     def get(self, request):
#         user_form = UserForm()
#         return render(request, 'profiles/register.html', context={'user_form': user_form})
#
#     def post(self, request):
#         user_form = UserForm(request.POST)
#         if user_form.is_valid():
#             User.objects.create(**user_form.cleaned_data)
#             return HttpResponseRedirect('/profiles/1/edit')
#         return render(request, 'profiles/register.html', context={'user_form': user_form})
#
#
# class UserEditFormView(View):
#     def get(self, request, profile_id):
#         user = User.objects.get(id=profile_id)
#         user_form = UserForm(instance=user)
#         return render(request, 'profiles/edit.html', context={'user_form': user_form,
#                                                               'profile_id': profile_id})
#
#     def post(self, request, profile_id):
#         user = User.objects.get(id=profile_id)
#         user_form = UserForm(request.POST, instance=user)
#
#         if user_form.is_valid():
#             user.save()
#         return render(request, 'profiles/edit.html', context={'user_form': user_form,
#                                                               'profile_id': profile_id})
