from django.shortcuts import render
from webapp.models import Tasks

def home_page(request):
    tasks = Tasks.objects.all()
    return render(request, 'home_page.html', {'tasks': tasks})
