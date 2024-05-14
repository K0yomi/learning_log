from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
	"""Регистрирует нового пользователя."""
	if request.method != 'POST':
		"""Выводит пустую форму регистрации."""
		form = UserCreationForm()
	else:
		#Обработка заполненной формы
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#Выполнение входа и перенаправление на домашнюю страницу.
			login(request, new_user)
			return redirect('learning_logs:index')
	
	#Вывести пустую или недействительную форму.
	context = {'form': form}
	return render(request, 'users/registration/register.html', context)

@login_required
def log_out(request):
	"""Выходим с аккаунта."""
	logout(request)
	return render(request, 'users/registration/logged_out.html')