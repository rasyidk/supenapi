from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.coba, name='verify'),
    path('<str:id>/', views.coba , name='verify'),
]