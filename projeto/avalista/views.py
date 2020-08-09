from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Avalista, Teste
from .forms import AvalistaForm, TesteForm

@login_required
def avalista_list(request):
    template_name='avalista_list.html'
    objects=Avalista.objects.all()    
    context={'object_list': objects}
    return render(request, template_name, context)

# class AvalistaCreate(CreateView):
#     model=Avalista 
#     template_name = 'avalista_form.html'
#     form_class=AvalistaForm    
#     success_url = reverse_lazy('avalista:avalista_list')

def avalista_add(request):
    form_avalista = AvalistaForm()
    form_teste = TesteForm()
    return render(request, 'avalista_form.html', {'form1': form_avalista, 'form2': form_teste})