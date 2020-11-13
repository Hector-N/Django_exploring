from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.template import loader
from django.urls import reverse
from .models import Post, Tag, Comment


def feed(request, year=None, month=None):

    if year and month:
        posts = Post.objects.filter(date__year=year).filter(date__month=month)
    elif year:
        posts = Post.objects.filter(date__year=year)
    else:
        posts = Post.objects.all()

    return render(request, 'blog/index.html',
                  context={'posts': posts,
                           'all_comments': False,
                           })


def post_details(request, post_id):
    # refactor with 'get_object_or_404()'
    # https://docs.djangoproject.com/en/3.1/topics/http/shortcuts/#django.shortcuts.get_object_or_404
    # post = get_object_or_404(Post, pk=post_id)
    try:
        # post = Post.objects.get(pk=post_id)
        post_in_list = Post.objects.filter(pk=post_id)
    except (Post.DoesNotExist):
        raise Http404("Page doesn't exists")

    context = {'posts': post_in_list,
               'all_comments': True,
               'specific': True}

    return render(request, 'blog/index.html', context)


def add_comment(request, post_id):
    cont = request.POST
    comment = cont['new_comment']
    author = cont['author']
    post_to_comment = Post.objects.get(pk=post_id)
    if author:
        comment = Comment(text=comment, author=author, post=post_to_comment)
    else:
        comment = Comment(text=comment, post=post_to_comment)

    comment.save()

    return HttpResponseRedirect(reverse('post_details', args=(post_id,)))


def tag_filter(request, tag_id):
    # tag = Tag.objects.get(pk=tag_id)
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = Post.objects.all().filter(tags__id=tag_id)
    context = {'search_tag': tag,
               'posts': posts,
               'all_comments': False}

    return render(request, 'blog/index.html', context)
