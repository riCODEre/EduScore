# Generated by Django 5.0.6 on 2024-07-07 09:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalSys', '0015_teacher_bookmarktb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationtb',
            name='DateAdded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='teacher_bookmarktb',
            name='DateAdded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
