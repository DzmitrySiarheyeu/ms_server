# Generated by Django 5.1 on 2024-08-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprof_department_userprof_division_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprof',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=100, null=True, verbose_name='Пол'),
        ),
    ]
