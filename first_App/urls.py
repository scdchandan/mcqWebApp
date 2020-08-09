from django.urls import path
from first_App import views

app_name = 'first_App'

urlpatterns=[
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'user_login'),
    path('css_quiz/', views.css_quiz, name = 'css_quiz'),
    path('html_quiz/', views.html_quiz, name = 'html_quiz'),
    path('nodejs_quiz/', views.nodejs_quiz, name = 'nodejs_quiz'),
    path('javascript_quiz/', views.javascript_quiz, name = 'javascript_quiz'),
    path('python_quiz/', views.python_quiz, name = 'python_quiz'),
    
]
