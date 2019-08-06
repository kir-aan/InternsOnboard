from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns=[
    path('post/', views.post, name="internship-Post"),
    path('', views.internshipListAPIView.as_view(), name=""),
]