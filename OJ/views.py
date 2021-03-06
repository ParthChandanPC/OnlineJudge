from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
import requests
from .models import Submissions,Problem,TestCases,User
from django.views.decorators.csrf import csrf_protect


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return render(request, 'login.html')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'registration.html', {'form': form})
def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def home(request):
    data = Problem.objects.all()
    return render(request,'home.html',{'data':data})
@login_required(login_url='login')
def problem_view(request,id):
    data = Problem.objects.get(id=id)
    return render(request,'problem_view.html',{'data':data,'User':User}) 


@login_required(login_url='login')
def ide(request,problem_id):
    user_id = request.user.id
    problem = Problem.objects.get(id=problem_id)
    user = User.objects.get(id=user_id)
    return render(request,'ide.html',{'problem_id':problem_id,'user_id':user_id})

@login_required(login_url='login')
def submissions(request,id):
    problem = Problem.objects.get(id=id)
    sub = Submissions.objects.filter(problem=problem)
    return render(request,'submissions.html',{'data':sub,'problem_id':id})
