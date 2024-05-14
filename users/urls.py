"""Определяет схемы URL для пользователей."""

from django.urls import path, include

from users import views

app_name = 'users'
urlpatterns = [
	#Включить URL авторизации по умолчанию.
	path('', include('django.contrib.auth.urls')),
	#СТраница регистрации.
	path('register/', views.register, name='register'),
	#
	path('logged_out', views.log_out, name='log_out'),
]