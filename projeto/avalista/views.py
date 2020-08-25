from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Avalista
from .forms import AvalistaForm

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


@login_required
def avalista_cadastra(request):
    avalistas = Avalista.objects.all()    
    form = AvalistaForm()    
    data = {'avalistas': avalistas,'form': form} 
    return render(request, 'avalista_form.html', data)

@login_required
def avalista_add(request):
    form = AvalistaForm(request.POST or None)   
    if form.is_valid():
        form.save()        
    return redirect('cliente_cnpj:cliente_cnpj_cadastra')


# def avalista_add(request):
#     form_avalista = AvalistaForm()
#     form_teste = TesteForm()
#     if request.method == 'POST':
#         if form_avalista.is_valid():
#             form_avalista.save()
#         if form_teste.is_valid():
#             form_teste.save()
#     return render(request, 'avalista_form.html', {'form1': form_avalista, 'form2': form_teste})