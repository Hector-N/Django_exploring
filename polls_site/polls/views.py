from django.shortcuts import render, get_object_or_404
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

    question = get_object_or_404(Question, pk=poll_num)

    return render(request,
                  'polls/details.html', {'question': question})


def vote_poll(request, poll_num):

    try:
        option_id = request.POST['choice']
    except KeyError:
        error = True

        # return HttpResponse('fucking idiot')
        return render(request,
                      'polls/details.html',
                      {'question': Question.objects.get(pk=poll_num), 'error_message':error})
    else:
        # q = Question.objects.get(pk=poll_num)
        # option = q.option_set.get(pk=option_id)
        option = Option.objects.get(pk=option_id)
        option.votes += 1
        option.save()

        return HttpResponseRedirect(reverse('polls:results',
                                            args=(poll_num,)))


def show_results(request, poll_num):

    question = get_object_or_404(Question, pk=poll_num)

    return render(request, 'polls/results.html', {'question': question})



