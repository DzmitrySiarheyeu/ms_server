from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.GetUserProfView.as_view({'get': 'retrieve'}))
    # path('<int:pk>/', views.GetUserProfView.as_view({'get': 'retrieve'}))
]
