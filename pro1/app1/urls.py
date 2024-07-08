from django.urls import path
from .views import *
urlpatterns = [
    path("hv/", homeview),
    path('pv/', pview)
]