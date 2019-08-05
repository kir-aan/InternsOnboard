from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="InternsOnboard-Home"),
    path('home/', views.home, name="InternsOnboard-Home"),
    path('about/', views.about, name="InternsOnboard-About"),
    
]