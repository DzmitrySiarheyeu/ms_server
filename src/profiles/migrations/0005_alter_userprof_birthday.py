# Generated by Django 5.1 on 2024-09-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprof_birthday_alter_userprof_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprof',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
    ]
