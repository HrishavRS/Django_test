from django.urls import path
from . import views

# URLConfig
urlpatterns = [
    path('hello/',views.testing_hello)
]