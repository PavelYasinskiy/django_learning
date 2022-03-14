from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views import View
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
        f = NewsForm(request.POST)
        new_article = f.save()
        return HttpResponseRedirect('/news/')


class NewsEditFormView(View):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/edit.html', context={'news_form': news_form,
                                                              'new_id': pk})

    def post(self, request, pk):
        news = News.objects.get(id=pk)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
        return render(request, 'app_news/edit.html', context={'news_form': news_form,
                                                              'new_id': pk})


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

    def post(self, request, pk):
        print("Что тут происходит", request.POST, "а вот что")
        form = CommentsForm(request.POST)
        new_comment = form.save(commit=False)
        new_comment.article = self.get_object()
        new_comment.save()
        return HttpResponseRedirect(f'/news/{pk}/')

