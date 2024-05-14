"""Определяет схемы URL для learning_logs."""

from django.urls import path #импорт функции path, для связывания URL с представлениями.

from . import views #импорт модуля views.

app_name = 'learning_logs' 
#переменная, помогающая Django отличить этот файл urls.py от одноименных файлов в других приложениях в проекте.

urlpatterns = [ 
	#urlpatterns - переменная, представляющая собой список страниц, которые могут запрашиваться из приложения learning_logs.
	#Домашняя страница
	path('', views.index, name='index'),
	#Страница со списком всех тем.
	path('topics/', views.topics, name='topics'),
	#Страница с подробной информацией по отдельной теме
	path('topics/<int:topic_id>/', views.topic, name='topic'),
	#Страница для добавления новой темы
	path('new_topic/', views.new_topic, name='new_topic'),
	#Страница для добавления новой записей
	path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
	#Страница для редактирования записи
	path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]