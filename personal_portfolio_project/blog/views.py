from django.shortcuts import render


def blog_page(request):
    return render(request, 'blog/blog_main.html')
