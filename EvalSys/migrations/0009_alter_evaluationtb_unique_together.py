# Generated by Django 5.0.6 on 2024-06-30 05:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EvalSys', '0008_evaluationtb_userid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='evaluationtb',
            unique_together={('UserID', 'TeacherID', 'CourseID')},
        ),
    ]
