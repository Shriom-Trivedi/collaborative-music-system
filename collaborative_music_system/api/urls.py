from django.urls import path
from .views import main

# If we get URL that is blank and nothing have on it the call the main function /views.
urlpatterns = [
    path('home', main),
    path('', main)
]