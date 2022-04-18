from django.shortcuts import render
from PortafolioApp2.models import Portafolio

# Create your views here.


def portafolio(request):

	portafolio=Portafolio.objects.all()
	return render(request, 'portafolio/portafolio.html', {"portafolio":portafolio})