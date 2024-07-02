from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required


def landing(request):
    user = request.user
    PastTeacher = EvaluationTB.objects.filter(UserID=user.id)
    return render(request, 'landing.html', {'PastTeacher': PastTeacher})

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

def UserLogin(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #add below update on lastlogin
                user.last_login = datetime.today()
                user.save()
                return redirect('landing')
            else:
                return render(request, 'UserLogin.html', {})
        else:
            return render(request, 'UserLogin.html', {})
    else:
        return render(request, 'UserLogin.html', {})

def UserLogout(request):
    logout(request)
    return redirect('landing')

@login_required(login_url='UserLogin')
def ReadAllTeachers(request):

    allTeachers = TeacherTB.objects.all()
    return render(request, 'all_teacher.html', {'allTeachers': allTeachers})

@login_required(login_url='UserLogin')
def EvaluateTeacher(request, teacher_id):
    user = request.user
    TeacherRec = TeacherTB.objects.get(pk=teacher_id)
    TCRecs = Teacher_CourseTB.objects.filter(TeacherID=teacher_id)
    if request.method == 'POST':
        form = TeacherEvalForm(request.POST)
        if form.is_valid():
            form.save()
            EvalRec = EvaluationTB.objects.get(UserID=user.id, TeacherID=teacher_id, CourseID=request.POST['CourseID'])
            return redirect('EvalTag', EvalID=EvalRec.id)
        else:
            return render(request, 'evaluate_teacher.html', {'t': TeacherRec, 'TC': TCRecs, 'forms': form})
    else:
        return render(request, 'evaluate_teacher.html', {'t': TeacherRec, 'TC': TCRecs, 'user': user})

@login_required(login_url='UserLogin')
def EvaluateTags(request, EvalID):
    TagRecs = TagTB.objects.filter(isHidden=False)
    if request.method == "POST":
        form = EvalTagForm(request.POST)
        if form.is_valid():
            EvalID = request.POST['EvaluationID']
            TagID = request.POST['TagID']
            isRecExist = Evaluation_TagTB.objects.filter(EvaluationID=EvalID, TagID=TagID).exists()
            if not isRecExist:
                form.save()
                return render(request, 'eval_tags.html', {'TR': TagRecs, 'EvalID': EvalID})
            else:
                return render(request, 'eval_tags.html', {'TR': TagRecs, 'EvalID': EvalID})
        else:
            return render(request, 'eval_tags.html', {'TR': TagRecs, 'EvalID': EvalID})
    else:
        return render(request, 'eval_tags.html', {'TR': TagRecs, 'EvalID': EvalID})

@login_required(login_url='UserLogin')
def SearchProf(request):
    user = request.user
    PastTeacher = EvaluationTB.objects.filter(UserID=user.id)
    return render(request, 'searchPage.html', {'PastTeacher': PastTeacher})