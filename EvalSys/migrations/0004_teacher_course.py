# Generated by Django 5.0.6 on 2024-06-29 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalSys', '0003_rename_user_evaluation_user_evaluationtb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvalSys.coursetb')),
                ('TeacherID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EvalSys.teachertb')),
            ],
        ),
    ]
