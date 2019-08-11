from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns=[
    path('post/', views.post, name="internship-Post"),
    path('application/', views.applications, name="internship-applications"),
    path('accept/',views.accept,name="internship-accept"),
    path('delete/',views.deleteInternship,name="internship-delete"),
    path('api/posts/', views.internshipListAPIView.as_view(), name="api-view"),
]