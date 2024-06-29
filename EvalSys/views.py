from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import *

def landing(request):
    return render(request, 'landing.html', {})

def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            # //another model
            Department = request.POST['Department']
            BatchNumber = request.POST['BatchNumber']
            Gender = request.POST['Gender']

            userCheck = authenticate(request, username=username, password=password)
            if userCheck is None:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=username
                )
                user.save()

                addUser = AddUserTB.objects.create(
                    eval_user=user,
                    Department=Department,
                    BatchNumber=BatchNumber,
                    Gender=Gender
                )
                addUser.save()
                return redirect('landing')
            return render(request, 'registerUser.html')
    else:
        return render(request, 'registerUser.html')

def ReadAllTeachers(request):
    allTeachers = TeacherTB.objects.all
    return render(request, 'all_teacher.html', {'allTeachers': allTeachers})