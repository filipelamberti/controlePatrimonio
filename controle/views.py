from django.shortcuts import render
from controle.forms import PatrimonioForm
from controle.models import Controle

def index(request):
    form = PatrimonioForm()
    return render(request, 'index.html', {'form': form})

def validar(request):
	if request.method == 'POST':
		form = PatrimonioForm(request.POST)

		if form.is_valid():
			form.save()
	
			controle = Controle.objects.all().order_by('nome')

			return render(request,'validar.html',{'form':form,'controle':controle})
		else:
		    return render(request,'index.html',{'form':form})

# Create your views here.
