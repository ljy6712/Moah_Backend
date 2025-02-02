from django.shortcuts import get_object_or_404, render, redirect

from todo.forms import TodoBaseForm


from .models import Todo

from django.contrib.auth.decorators import login_required

def index(request):
    todo_list = Todo.objects.all()
    context ={
        'todo_list': todo_list
    }
    return render(request, 'main.html', context)

# Create your views here.
def todo_list_view(request):
    #todo_list = Todo.objects.all()
    todo_list = Todo.objects.filter(writer = request.user)
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todo/moahtodo.html', context)

@login_required
def todo_create_view(request):
    if request.method == 'GET':
        return render(request, 'todo/moahtodo.html', {'form': TodoBaseForm()})
    else:
        #image = request.FILES.get('image')
        content = request.POST.get('content')
        Todo.objects.create(
            #image = image,
            content = content,
            #writer = request.user
        )
        #return redirect('todo/moahtodo.html')