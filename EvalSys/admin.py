from django.contrib import admin
from .models import *

admin.site.register(AddUserTB)
admin.site.register(TagTB)
admin.site.register(CourseTB)
admin.site.register(TeacherTB)
admin.site.register(EvaluationTB)
admin.site.register(Evaluation_TagTB)
admin.site.register(Teacher_CourseTB)
admin.site.register(Teacher_BookmarkTB)

