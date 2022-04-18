from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):

	return render(request, 'PortafolioApp/inicio.html')


def perfil(request):

	return render(request, 'PortafolioApp/perfil.html')

def contactame(request):

	return render(request, 'PortafolioApp/contactame.html')


def acerca_de(request):

	return render(request, 'PortafolioApp/acercade.html')