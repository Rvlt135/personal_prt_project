from django.shortcuts import render
from .models import BlogContet

def blog_page(request):
    blog_content = BlogContet.objects.all()
    return render(request, 'blog/blog_main.html', {'blogContent': blog_content})
