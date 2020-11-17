from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render({"context": 'Hello!'}))



def show_poll(request, poll_num):
    return render(request, 'polls/poll_details.html', {'context': 'boo!'})


def vote_poll(request, poll_num):
    return HttpResponse(f"voting on poll number {poll_num}")



