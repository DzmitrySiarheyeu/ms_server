from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.UserProfView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.UserProfPublic.as_view({'get': 'retrieve'})),
]
