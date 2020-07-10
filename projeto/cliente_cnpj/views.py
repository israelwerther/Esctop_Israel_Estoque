from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Cliente_cnpj
from .forms import Cliente_cnpjForm

@login_required
def cliente_cnpj_list(request):
    template_name='cliente_cnpj_list.html'
    objects=Cliente_cnpj.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)


@login_required
def cliente_cnpj_detail(request, pk):
    template_name='cliente_cnpj_detail.html'
    obj=Cliente.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)