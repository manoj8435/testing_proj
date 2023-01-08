from django.urls import path
from .views import *
urlpatterns = [
    path('show/',show),
    path("shows/", ShowView.as_view(), name="class-based-view")
]
