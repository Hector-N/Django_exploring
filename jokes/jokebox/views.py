from django.shortcuts import render
from .models import Joke
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# from django.template import loader


def joke_page(request):

    content = request.POST

    # if joke is passed in form
    if content:
        if content['new_joke_f']:

            # prepare to send random joke
            random_joke = Joke.random_joke()
            random_joke_text = random_joke.joke_text
            random_joke_author = random_joke.author
            context = {'send_back': True,
                       'random_joke': random_joke_text,
                       'random_joke_author': random_joke_author}

            # save new joke
            new_joke_text = content['new_joke_f']
            new_joke_author = content['joke_author_f']
            new_joke_obj = Joke(joke_text=new_joke_text, author=new_joke_author)
            new_joke_obj.save()

            # send random joke
            return render(request, 'jokebox/index.html', context)

        else:
            return render(request, 'jokebox/index.html')

    # return page without joke
    else:
        return render(request, 'jokebox/index.html')
