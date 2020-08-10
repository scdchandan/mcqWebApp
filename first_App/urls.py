from django.urls import path
from first_App import views

app_name = 'first_App'

urlpatterns=[
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'user_login'),
    path('css_quiz/<str:pk>/', views.css_quiz, name = 'css_quiz'),
    path('create_css_quiz/', views.create_css_quiz, name = 'create_css_quiz'),
    path('html_quiz/<str:pk>/', views.html_quiz, name = 'html_quiz'),
    path('create_html_quiz/', views.create_html_quiz, name = 'create_html_quiz'),
    path('nodejs_quiz/<str:pk>/', views.nodejs_quiz, name = 'nodejs_quiz'),
    path('create_nodejs_quiz/', views.create_nodejs_quiz, name = 'create_nodejs_quiz'),
    path('javascript_quiz/<str:pk>/', views.javascript_quiz, name = 'javascript_quiz'),
    path('create_javascript_quiz/', views.create_javascript_quiz, name = 'create_javascript_quiz'),
    path('python_quiz/<str:pk>/', views.python_quiz, name = 'python_quiz'),
    path('create_python_quiz/', views.create_python_quiz, name = 'create_python_quiz'),
    path('takeaquiz/', views.takeaquiz, name = 'takeaquiz'),
    path('myscores/<str:username>/', views.myscores, name = 'myscores'),


]
