from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.



class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'


def post_list(request):
    post = Post.published.all()
    send_mail('efgefedsDSF', 'DFGNFDBSDAADFGFDDS','imowww1234@gmail.com', ['imowww@yandex.ru'], fail_silently=False)
    paginator = Paginator(post, 2)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1) 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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



def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})