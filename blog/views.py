from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
# Create your views here.



def post_list(request):
    post = Post.published.all()
    
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    context = {
        'posts': posts,
        }
    return render(request, 'blog/post/list.html', context)



def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day) 
    context = {
        'post': post
        }
    return render(request, 'blog/post/detail.html', context)




