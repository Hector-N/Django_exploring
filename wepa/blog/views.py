from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.template import loader
from .models import Post, Tag, Comment


def latest_feed(request):
    return render(request, 'blog/index.html',
                  context={'say_hi_to': 'Pythonistas',
                           'posts': Post.objects.all(),
                           })


def post_details(request, post_id):
    # refactor with 'get_object_or_404()'
    # https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/#django.shortcuts.get_object_or_404
    # post = get_object_or_404(Post, pk=post_id)
    try:
        post = Post.objects.get(pk=post_id)
    except (Post.DoesNotExist):
        raise Http404("Page doesn't exists")

    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)



def tag_filter(request, tag_id):
    # tag = Tag.objects.get(pk=tag_id)
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = Post.objects.all().filter(tags__id=tag_id)
    context = {'tag': tag,
               'posts': posts}

    return render(request, 'blog/index.html', context)


# def year_archive(request):
#     return HttpResponse('YEAR ARCHIVE')
#
#
# def month_archive(request):
#     return HttpResponse('MONTH ARCHIVE')
