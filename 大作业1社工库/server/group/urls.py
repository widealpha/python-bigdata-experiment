from django.urls import path

from . import views

urlpatterns = [
    path('qq', views.qq, name='qq'),
    path('qun', views.qun, name='qun'),
]
