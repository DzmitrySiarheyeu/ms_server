from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .models import UserProf
from .serializers import GetUserProfSerializer

class GetUserProfView(ModelViewSet):
    queryset = UserProf.objects.all()
    serializer_class = GetUserProfSerializer
    permission_classes = [permissions.AllowAny]

class UpdateUserProfView(ModelViewSet):
    queryset = UserProf.objects.all()
    serializer_class = GetUserProfSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProf.objects.filter(id=self.request.user.id)
    