from django.urls import  path
from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('courses', views.courses, name='courses'),
    path('reports', views.reports, name='reports'),
]