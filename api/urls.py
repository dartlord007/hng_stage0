from django.urls import path
from .views import get_info
from api import views

urlpatterns = [
    # path('api/', get_info, name='get_info'),
     path("", views.get_info, name="get_info"),
]