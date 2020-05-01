from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Emprestimo
from .forms import EmprestimoForm



def emprestimo_list(request):    
    template_name='emprestimo_list.html'  
    objects=Emprestimo.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)

