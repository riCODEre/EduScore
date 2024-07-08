from django import forms
from .models import *
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    class Meta:
        fields = [
            "first_name",
            "last_name",
            "username",
            "password"
            "Department",
            "BatchNumber",
            "Gender"
        ]

class UserLoginForm(forms.Form):
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]


class TeacherEvalForm(forms.ModelForm):
    class Meta:
        model = EvaluationTB
        fields = [
            "UserID",
            "TeacherID",
            "CourseID",
            "Year",
            "Term",
            "ClassModality",
            "OverallProfRate",
            "ProfDifficulty",
            "RetakeProf",
            "BigSkyUsageRate",
            "ProfAttendance",
            "GradeReceived",

        ]

class EvalTagForm(forms.ModelForm):
    class Meta:
        model = Evaluation_TagTB
        fields = [
            "EvaluationID",
            "TagID"
        ]

class SearchForm(forms.Form):
    class Meta:
        fields = [
            "searchRec",
            "typeRec"
        ]
class SortEvalsForm(forms.Form):
    class Meta:
        fields = [
            "Type",
            "Arrange"
        ]