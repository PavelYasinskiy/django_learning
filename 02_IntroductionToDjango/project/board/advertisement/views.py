from django.shortcuts import render
from .models import Board
from django.views.generic import ListView

def advertisement_list(request,*args,**kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})

def first_page_list(request,*args,**kwargs):
    data = Board.objects.all()
    return render(request, 'advertisement/first_page_list.html', {'data': data})

# data = Book.objects.all()
#     return render(request, 'home_page.html', {'data': data})
