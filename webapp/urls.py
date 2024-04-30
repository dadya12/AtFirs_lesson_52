from django.urls import path
from webapp.views import home, task_page

urlpatterns = [
    path('', home, name='home'),
    path('task_page/', task_page, name='task_page')
]