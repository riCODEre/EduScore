# Generated by Django 5.0.6 on 2024-06-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalSys', '0005_rename_teacher_course_teacher_coursetb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationtb',
            name='GradeReceived',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
