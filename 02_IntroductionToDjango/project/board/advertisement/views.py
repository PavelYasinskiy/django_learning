from django.shortcuts import render



def advertisement_list(request,*args,**kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})

def first_page_list(request,*args,**kwargs):
    return render(request, 'advertisement/first_page_list.html', {})

def second_page_list(request,*args,**kwargs):
    return render(request, 'advertisement/second_page_list.html', {})

def third_page_list(request,*args,**kwargs):
    return render(request, 'advertisement/third_page_list.html', {})

def fourth_page_list(request,*args,**kwargs):
    return render(request, 'advertisement/fourth_page_list.html', {})

def fifth_page_list(request,*args,**kwargs):
    return render(request, 'advertisement/fifth_page_list.html', {})


