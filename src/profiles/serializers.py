from token import EXCLAMATION
from rest_framework import serializers

from .models import UserProf

class GetUserProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProf
        exclude = ("password", "last_login", "is_active", "is_staff", "is_superuser")


class GetUserProfPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProf
        exclude = ("email", "phone","password", "last_login", "is_active", "is_staff", "is_superuser")