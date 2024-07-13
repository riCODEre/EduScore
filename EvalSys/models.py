from datetime import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class AddUserTB(models.Model):
    eval_user = models.OneToOneField(User, on_delete=models.CASCADE)
    Department = models.CharField(max_length=100, null=False, blank=False)
    BatchNumber = models.IntegerField(null=False, blank=False)
    Gender = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.eval_user.username} | {self.BatchNumber}'

class TagTB(models.Model):
    TagName = models.CharField(max_length=100, null=False, blank=False)
    isHidden = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f'{self.pk} | {self.TagName} | {self.isHidden}'

class CourseTB(models.Model):
    CourseCode = models.CharField(unique=True, max_length=50, null=False, blank=False)
    CourseName = models.CharField(max_length=100, null=False, blank=False)
    Description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.CourseCode}'

class TeacherTB(models.Model):
    FirstName = models.CharField(max_length=100, null=False, blank=False)
    LastName = models.CharField(max_length=100, null=False, blank=False)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=100, null=True, blank=True, default="Unknown")
    EmpStatus = models.CharField(max_length=50, null=True, blank=True, default="Unknown")

    def __str__(self):
        return f'{self.LastName}, {self.FirstName} | {self.Department}'

class EvaluationTB(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    TeacherID = models.ForeignKey(TeacherTB, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(CourseTB, on_delete=models.CASCADE)
    Year = models.CharField(max_length=50, null=False, blank=False)
    Term = models.IntegerField(null=False, blank=False)
    ClassModality = models.CharField(max_length=50, null=False, blank=False)
    OverallProfRate = models.FloatField(null=False, blank=False)
    ProfDifficulty = models.FloatField(null=False, blank=False)
    RetakeProf = models.BooleanField(null=False, blank=False)
    BigSkyUsageRate = models.FloatField(null=False, blank=False)
    ProfAttendance = models.FloatField(null=False, blank=False)
    GradeReceived = models.FloatField(null=True, blank=True)
    DateAdded = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('UserID', 'TeacherID', 'CourseID')

    def __str__(self):
        return f'{self.TeacherID.LastName} | {self.OverallProfRate}'

# following are join tables

class Evaluation_TagTB(models.Model):
    EvaluationID = models.ForeignKey(EvaluationTB, on_delete=models.CASCADE)
    TagID = models.ForeignKey(TagTB, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('EvaluationID', 'TagID')

    def __str__(self):
        return (f'{self.EvaluationID.UserID.username} | {self.EvaluationID.TeacherID.LastName} '
                f'| {self.EvaluationID.CourseID.CourseCode} | {self.TagID.TagName}')

class Teacher_CourseTB(models.Model):
    TeacherID = models.ForeignKey(TeacherTB, on_delete=models.CASCADE)
    CourseID = models.ForeignKey(CourseTB, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('TeacherID', 'CourseID')

    def __str__(self):
        return f'{self.TeacherID.LastName}, {self.TeacherID.FirstName} | {self.CourseID.CourseCode}'

class Teacher_BookmarkTB(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    TeacherID = models.ForeignKey(TeacherTB, on_delete=models.CASCADE)
    DateAdded = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('TeacherID', 'UserID')

    def __str__(self):
        return f'{self.TeacherID.LastName}, {self.TeacherID.FirstName} | {self.UserID.last_name}'


