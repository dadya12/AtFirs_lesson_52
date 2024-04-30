from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Tasks

def task_page(request):
    tasks = Tasks.objects.all()
    return render(request, 'task_page.html', {'tasks': tasks})

def home(request):
    return render(request, 'home.html')

def task_create(request):
    if request.method == 'GET':
        return render(request, 'task_create.html')
    elif request.method == "POST":
        Tasks.objects.create(
            description=request.POST['description'],
            status=request.POST['status'],
            date_done=request.POST['date_done']
        )
        return HttpResponseRedirect('/')