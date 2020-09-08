from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
   
#from base.models import Task 
#from . models import *
from .models import Task_todo
from .forms import *

def index(request):
    tasks= Task_todo.objects.all()
    form = Task_todoForm()
    if request.method=='POST':
        form = Task_todoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
   # context={'tasks':tasks}
    return render(request, 'base/list.html', {'task':tasks, 'form':form})


def update(request,pk):
    update = Task_todo.objects.get(id=pk)
    tasks = Task_todoForm(instance=update)

    if request.method== 'POST':
        form = Task_todoForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'base/update_todo.html',{'tasks':tasks})

def delete(request,pk):
    dele =Task_todo.objects.get(id=pk)

    if request.method=='POST':
        dele.delete()
        return redirect('/')
    return render(request,'base/delete_todo.html',{'dele':dele})