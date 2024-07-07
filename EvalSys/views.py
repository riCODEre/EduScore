from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.db.models import Subquery
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        # //another model
        Department = request.POST['Department']
        BatchNumber = request.POST['BatchNumber']
        Gender = request.POST['Gender']
        if form.is_valid():
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
            else:
                return render(request, 'registerUser.html', {'exists': "User already exists."})
        else:
            return render(request, 'registerUser.html', {
                'forms': form,
                'fname': first_name,
                'lname': last_name,
                'uname': username,
                'pword': password,
                'dept': Department,
                'batch': BatchNumber,
                'gender': Gender
            })
    else:
        return render(request, 'registerUser.html')


def UserLogin(request):
    logout(request)
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
                return redirect('SearchProf')
            else:
                return render(request, 'UserLogin.html', {
                    'uname': request.POST['username'],
                    'pword': request.POST['password'],
                    'forms': form,
                    'exists': "User does not exist"
                })
        else:
            return render(request, 'UserLogin.html', {
                'uname': request.POST['username'],
                'pword': request.POST['password'],
                'forms': form
            })
    else:
        return render(request, 'UserLogin.html', {})


def UserLogout(request):
    logout(request)
    return redirect('landing')


@login_required(login_url='UserLogin')
def EvaluateTeacher(request, teacher_id):
    user = request.user
    EvalRecs = EvaluationTB.objects.filter(TeacherID=teacher_id, UserID=user.id)
    TCRecs = (Teacher_CourseTB.objects.filter(TeacherID=teacher_id)
              .exclude(CourseID__in=Subquery(EvalRecs.values('CourseID_id'))))
    TeacherRec = TeacherTB.objects.get(pk=teacher_id)

    if request.method == 'POST':
        form = TeacherEvalForm(request.POST)
        if form.is_valid():
            form.save()
            EvalRec = EvaluationTB.objects.get(UserID=user.id, TeacherID=teacher_id, CourseID=request.POST['CourseID'])
            return redirect('EvalTag', EvalID=EvalRec.id)
        else:
            return render(request, 'evaluate_teacher.html', {
                't': TeacherRec,
                'TC': TCRecs,
                'forms': form,
                'user': user.id,
                'CourseID': request.POST['CourseID'],
                'Year': request.POST['Year'],
                'Term': request.POST['Term'],
                'ClassModality': request.POST['ClassModality'],
                'OverallProfRate': request.POST['OverallProfRate'],
                'ProfDifficulty': request.POST['ProfDifficulty'],
                'RetakeProf': request.POST['RetakeProf'],
                'BigSkyUsageRate': request.POST['BigSkyUsageRate'],
                'ProfAttendance': request.POST['ProfAttendance'],
                'GradeReceived': request.POST['GradeReceived']
            })
    else:
        return render(request, 'evaluate_teacher.html', {'t': TeacherRec, 'TC': TCRecs, 'user': user})


@login_required(login_url='UserLogin')
def EvaluateTags(request, EvalID):
    user = request.user
    EvalRec = EvaluationTB.objects.get(pk=EvalID)
    if user.id == EvalRec.UserID.id:
        hasEval = Evaluation_TagTB.objects.filter(EvaluationID=EvalID)
        noEval = TagTB.objects.filter(isHidden=False).exclude(id__in=Subquery(hasEval.values('TagID_id')))
        if request.method == "POST":
            form = EvalTagForm(request.POST)
            EvalID = request.POST['EvaluationID']
            TagID = request.POST['TagID']
            try:
                RecDel = Evaluation_TagTB.objects.get(EvaluationID=EvalID, TagID=TagID)
                RecDel.delete()
                return redirect('EvalTag', EvalID)
            except:
                pass
            if form.is_valid():
                form.save()
                return redirect('EvalTag', EvalID)
            else:
                return render(request, 'eval_tags.html',
                              {'hasEval': hasEval, 'noEval': noEval, 'EvalID': EvalID,
                               'TeacherID': EvalRec.TeacherID.id, 'forms': form})
        else:
            return render(request, 'eval_tags.html',
                          {'hasEval': hasEval, 'noEval': noEval, 'EvalID': EvalID, 'TeacherID': EvalRec.TeacherID.id})
    else:
        return redirect('SearchProf')


def SearchProf(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            searchRec = request.POST['searchRec']
            typeRec = request.POST['typeRec']
            if searchRec == '':
                return render(request, 'searchPage.html', {'forms': form})
            elif typeRec == "LName":
                TeacherRecs = TeacherTB.objects.filter(LastName__icontains=searchRec)
                return render(request, 'searchPage.html',
                              {'SearchResults': TeacherRecs, 'search': searchRec, 'type': typeRec})
            elif typeRec == "Subject":
                TeacherRecs = (TeacherTB.objects.filter(teacher_coursetb__CourseID__CourseCode__icontains=searchRec)
                               .distinct())
                return render(request, 'searchPage.html',
                              {'SearchResults': TeacherRecs, 'search': searchRec, 'type': typeRec})
            elif typeRec == "School":
                TeacherRecs = TeacherTB.objects.filter(Department__icontains=searchRec)
                return render(request, 'searchPage.html',
                              {'SearchResults': TeacherRecs, 'search': searchRec, 'type': typeRec})
            elif typeRec == "FName":
                TeacherRecs = TeacherTB.objects.filter(FirstName__icontains=searchRec)
                return render(request, 'searchPage.html',
                              {'SearchResults': TeacherRecs, 'search': searchRec, 'type': typeRec})
    else:
        return render(request, 'searchPage.html')


@login_required(login_url='UserLogin')
def TeacherInfo(request, teacher_id):
    user = request.user
    TeacherRec = TeacherTB.objects.get(pk=teacher_id)
    TCourseRecs = Teacher_CourseTB.objects.filter(TeacherID=teacher_id)
    EvalRecs = EvaluationTB.objects.filter(TeacherID=teacher_id, UserID=user.id)
    try:
        Teacher_BookmarkTB.objects.get(TeacherID=teacher_id, UserID=user.id)
        isMark = True
    except:
        isMark = False
    showAdd = False
    showEdit = False

    if len(EvalRecs) > 0: showEdit = True
    if len(TCourseRecs) != len(EvalRecs): showAdd = True

    return render(request, 'teacherInfo.html', {
        'prof': TeacherRec,
        'Courses': TCourseRecs,
        'Evals': EvalRecs,
        'showAdd': showAdd,
        'showEdit': showEdit,
        'Mark': isMark})


@login_required(login_url='UserLogin')
def EditTeacherEval(request, evalID):
    EvalRec = EvaluationTB.objects.get(pk=evalID)
    user = request.user
    if user.id == EvalRec.UserID.id:
        if request.method == 'POST':
            form = TeacherEvalForm(request.POST or None, instance=EvalRec)
            if form.is_valid():
                form.save()
                return redirect('EvalTag', EvalRec.id)
            else:
                return render(request, 'edit_eval.html', {'EvalRec': EvalRec, 'forms': form})
        else:
            return render(request, 'edit_eval.html', {'EvalRec': EvalRec})
    else:
        return redirect('SearchProf')


@login_required(login_url='UserLogin')
def DeleteEval(request, evalID):
    EvalRec = EvaluationTB.objects.get(pk=evalID)
    user = request.user
    if user.id == EvalRec.UserID.id:
        teacherID = EvalRec.TeacherID.id
        EvalRec.delete()
        return redirect('TeacherInfo', teacherID)
    else:
        return redirect('SearchProf')

@login_required(login_url='UserLogin')
def showBookmark(request):
    user = request.user
    MarkedProf = Teacher_BookmarkTB.objects.filter(UserID=user.id)
    return render(request, 'bookmark.html', {'ProfRecs': MarkedProf})

@login_required(login_url='UserLogin')
def ProfPage_AddBookmark(request, ProfID):
    user = request.user
    TeachRec = TeacherTB.objects.get(pk=ProfID)
    newBM = Teacher_BookmarkTB.objects.create(
        UserID=user,
        TeacherID=TeachRec
    )
    newBM.save()
    return redirect(TeacherInfo, ProfID)

def ProfPage_DelBookmark(request, ProfID):
    user = request.user
    BookMarkRec = Teacher_BookmarkTB.objects.get(UserID=user.id, TeacherID=ProfID)
    BookMarkRec.delete()
    return redirect(TeacherInfo, ProfID)
