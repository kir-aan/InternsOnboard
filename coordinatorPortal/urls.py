from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from .views import internshipListAPIView,post,applications,deleteInternship,accept

urlpatterns=[
    path('post/', post, name="internship-Post"),
    path('application/', applications, name="internship-applications"),
    path('accept/',accept,name="internship-accept"),
    path('delete/',deleteInternship,name="internship-delete"),
    # path('internships/',internshipView.as_view()),
    path('api/internships/', internshipListAPIView.as_view(), name="api-view"),
]