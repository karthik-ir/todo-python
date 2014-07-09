from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
from taskapp.models import task
from taskapp.form import UserForm, TaskForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    notdone_task_list = task.objects.filter(status=False).order_by('-due_date')
    done_task_list = task.objects.filter(status=True).order_by('-due_date')
    return render_to_response('index.html', {'notdone_tasks_list': notdone_task_list, 'done_tasks_list': notdone_task_list})

def new_task(request):   
    context = RequestContext(request)

    if request.method == 'POST':
        task_form = TaskForm(data=request.POST)
        if task_form.is_valid() :
            task = task_form.save()
            task.save()
            return HttpResponseRedirect('/tasks')
    
    else:
        task_form = TaskForm()
    return render_to_response(
            'task_add.html',
            {'task_form': task_form}, context)

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/tasks')
    else:
        user_form = UserForm()
        task_form = TaskForm()
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered, 'task_form': task_form}, context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
                login(request, user)
                return HttpResponseRedirect('/tasks')
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {}, context)
