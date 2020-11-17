from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.utils import timezone
from django.urls import reverse

from .models import Question, Option



def home(request):

    q_set = Question.objects.filter(date__month=timezone.now().month)

    template = loader.get_template('polls/index.html')
    return HttpResponse(template.render({'questions': q_set}))



def show_poll(request, poll_num):

    question = Question.objects.get(pk=poll_num)

    return render(request,
                  'polls/poll_details.html',
                  {'question': question})


def vote_poll(request, poll_num):
    option_txt = request.POST['how_tall']
    q = Question.objects.get(pk=poll_num)
    option = q.option_set.get(text__exact=option_txt)
    option.votes += 1
    option.save()

    return HttpResponseRedirect(reverse('polls:details', args=(q.id,)))
