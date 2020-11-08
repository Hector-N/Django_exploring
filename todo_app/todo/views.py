# from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task


# output template and list of tasks
def output(request):

    all_my_tasks = Task.objects.all()
    template = loader.get_template('todo/index.html')
    context = {'all_tasks': all_my_tasks}

    return HttpResponse(template.render(context, request))


# handler of form text input
def add_task(request):

    c = request.POST['new_task_from_form']
    new_task = Task(task_text=c)
    new_task.save()

    # return HttpResponseRedirect('/todo/')
    return HttpResponseRedirect('/todo/index.html')


# handler of form delete button
def delete_task(request, task_id):

    task_to_delete = Task.objects.get(id=task_id)
    task_to_delete.delete()

    # return HttpResponseRedirect('/todo/')
    return HttpResponseRedirect('/todo/index.html')
