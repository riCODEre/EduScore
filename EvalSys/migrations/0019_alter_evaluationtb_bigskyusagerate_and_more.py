# Generated by Django 5.0.6 on 2024-07-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalSys', '0018_alter_evaluationtb_bigskyusagerate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationtb',
            name='BigSkyUsageRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='evaluationtb',
            name='GradeReceived',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='evaluationtb',
            name='OverallProfRate',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='evaluationtb',
            name='ProfAttendance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='evaluationtb',
            name='ProfDifficulty',
            field=models.FloatField(),
        ),
    ]
