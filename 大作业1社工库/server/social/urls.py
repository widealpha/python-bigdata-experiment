from django.urls import path

from . import views

urlpatterns = [
    path('searchPeople', views.search_people, name='searchPeople'),
]
