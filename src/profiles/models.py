from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class UserProf(AbstractUser):
    GENDER = (("male", "Мужчина"), ("female", "Женщина"))

    middle_name = models.CharField(
        verbose_name=_("Отчество"), max_length=50, blank=True
    )
    first_login = models.DateTimeField(verbose_name=_("Первый вход"), blank=True,null=True)
    phone = models.CharField(verbose_name=_("Телефон"), max_length=14, blank=True)
    
    work_phone = models.CharField(verbose_name=_("Рабочий телефон"),max_length=14, blank=True, null=True)

    avatar = models.ImageField(
        verbose_name=_("Аватар"), upload_to="user/avatar/", blank=True, null=True
    )
    department = models.CharField(
        verbose_name=_("Отдел"), max_length=100, blank=True, null=True
    )
    division = models.CharField(
        verbose_name=_("Подразделение"), max_length=100, blank=True, null=True
    )
    gender = models.CharField(
        verbose_name=_("Пол"), max_length=100, choices=GENDER, blank=True, null=True
    )
    birthday = models.DateField(verbose_name=_("День рождения"), blank=True, null=True)

