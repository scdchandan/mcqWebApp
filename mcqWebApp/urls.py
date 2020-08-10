"""mcqWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from first_App import views
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('first_App/', include('first_App.urls')),
    path('logout/', views.user_logout, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('home/', views.home, name='home'),
    path('stud_home/', views.stud_home, name='stud_home'),
    path('teacher_home/', views.teacher_home, name='teacher_home'),
    path('accounts/', include('allauth.urls')),
    path('submit_quiz/<str:category>/<str:pk>/<str:username>/', views.submit_quiz, name = 'submit_quiz'),
    path('create_quiz/<str:category>/<str:name>/', views.create_quiz, name = 'create_quiz'),
    path('available_quiz/<str:category>/<str:username>/', views.available_quiz, name = 'available_quiz'),

]
