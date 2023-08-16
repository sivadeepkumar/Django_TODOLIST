from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    search_query = request.GET.get('search', '')
    tasks = Task.objects.filter(title__icontains=search_query)
    return render(request,'task.html',{'tasks':tasks})


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task')
    return render(request, 'create.html')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task')


def linestrike(request,id):
    task = Task.objects.get(id = id)
    if task.completed == True:
        task.completed = False
    else:
        task.completed = True 
    task.save()
    return redirect('task')
    


