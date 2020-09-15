from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
# it is a default view.
# please go to the samples folder for others view
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import logout as do_logout
def catalogue(request):
 	return  render(request, 'catalogue.html')

def panel(request):
 	return  render(request, 'panel-1.html')

def panel2(request):
 	return  render(request, 'panel-2.html')

def panel3(request):
 	return  render(request, 'panel-3.html')

def panel4(request):
 	return  render(request, 'panel-4.html')

def panel5(request):
 	return  render(request, 'panel-5.html')
def panel6(request):
 	return  render(request, 'panel-6.html')

def test(request):
 	return  render(request, 'test.html')

def login(request):
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']
		aux = User.objects.get(username=username)
		user = authenticate(username=aux.username, password=password)
		print(aux)
		print(user)
		if user:
			return redirect('index')
	else:
		return render(request, 'loguin.html')


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
