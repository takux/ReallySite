from django.shortcuts import render
from blog.models import Article, Comment, Tag
from django.core.paginator import Paginator
from blog.forms import CommentForm

def index(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 2)
    page_number = request.GET.get('page')
    context = {
        'page_title': 'ブログ一覧',
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/blogs.html', context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST.get('like_count', None):
            obj.count += 1
            obj.save()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.article = obj
                comment.save()
    comments = Comment.objects.filter(article=obj)
    context = {
        'article': obj,
        'comments': comments
    }
    return render(request, 'blog/article.html', context)

def tags(request, slug):
    tag = Tag.objects.get(slug=slug)
    objs = tag.article_set.all()

    paginator = Paginator(objs, 10)
    page_number = request.GET.get('page')
    context = {
        'page_title': '記事一覧 #{}'.format(slug),
        'page_obj': paginator.get_page(page_number),
        'page_number': page_number,
    }
    return render(request, 'blog/blogs.html', context)






from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

@ensure_csrf_cookie
def like(request, pk):
    d = {"message": "error"}
    if request.method == 'POST':
        obj = Article.objects.get(pk=pk)
        obj.count += 1
        obj.save()
        d["message"] = "success"
    return JsonResponse(d)