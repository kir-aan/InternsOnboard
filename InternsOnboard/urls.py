from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from userRegister import views as user_views
from django.conf import settings
from studentPortal import views as student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.register,name="Register"),
    path('register/', user_views.register,name="Register"),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='userRegister/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userRegister/logout.html'), name='logout'),
    path('', include('InternsOnboardMain.urls')),
    path('', include('coordinatorPortal.urls')),
    path('api/posts/', include('coordinatorPortal.urls')),
    path('apply/',student_views.apply,name='student-apply')
]
