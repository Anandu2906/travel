from django.urls import path
from . import views
urlpatterns = [
    path('', views.demo, name='demo'),
   # path('oper/', views.operation, name='addition'),
]