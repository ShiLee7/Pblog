from django.shortcuts import render

def index(request):
    return render(request, 'blog/articles/layoutart.html')

def st(request):
    return render(request, 'blog/st/layoutst.html')

def poems(request):
    return render(request, 'blog/poems/layoutp.html')