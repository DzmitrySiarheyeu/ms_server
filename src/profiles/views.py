from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import UserProf
from .serializers import GetUserProfSerializer, GetUserProfPublicSerializer


class UserProfPublic(ModelViewSet):
    queryset = UserProf.objects.all()
    serializer_class = GetUserProfPublicSerializer
    permission_classes = [permissions.AllowAny]

class UserProfView(ModelViewSet):
    serializer_class = GetUserProfSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProf.objects.filter(id=self.request.user.id)
    