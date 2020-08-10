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


@login_required
def avalista_cadastra(request):
    avalistas = Avalista.objects.all()
    testes    = Teste.objects.all()
    form1 = AvalistaForm()
    form2 = TesteForm()
    data = {'avalistas': avalistas, 'testes': testes,'form1': form1, 'form2': form2} 
    return render(request, 'avalista_form.html', data)


def avalista_novo(request):
    form1 = AvalistaForm(request.POST or None)
    form2 = TesteForm(request.POST or None)

    if form1.is_valid() and form2.is_valid():
        form1.save()
        form2.save()
    return redirect('avalista:avalista_list')


# def avalista_add(request):
#     form_avalista = AvalistaForm()
#     form_teste = TesteForm()
#     if request.method == 'POST':
#         if form_avalista.is_valid():
#             form_avalista.save()
#         if form_teste.is_valid():
#             form_teste.save()
#     return render(request, 'avalista_form.html', {'form1': form_avalista, 'form2': form_teste})