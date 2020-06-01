from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.http import HttpResponse
from .models import Emprestimo, EmprestimoPagamento
from .forms import EmprestimoForm, EmprestimoPagamentoForm



def emprestimo_list(request):    
    template_name='emprestimo_list.html'  
    objects=Emprestimo.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)


class EmprestimoImpress(UpdateView):
    model=Emprestimo
    template_name='emprestimo_impress.html'
    form_class=EmprestimoForm

# def emprestimo_impress(request, pk):    
#     template_name='emprestimo_impress.html'  
#     obj=Emprestimo.objects.get(pk=pk)
#     context={'object': obj}
#     return render(request, template_name, context)


def emprestimo_detail(request, pk):
    template_name='emprestimo_detail.html'
    obj=Emprestimo.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


class EmprestimoCreate(CreateView):
    model=Emprestimo
    template_name='emprestimo_form.html'
    form_class=EmprestimoForm
    

class EmprestimoUpdate(UpdateView):
    model=Emprestimo
    template_name='emprestimo_form.html'
    form_class=EmprestimoForm    
        


def emprestimo_pagamento_add(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    form = EmprestimoPagamentoForm()
    # pagamentos = emprestimo.emprestimo_set.all()
    context = {'emprestimo': emprestimo, 'form': form}
    return render(request, 'emprestimo_pagamento_add.html', context)

    

def emprestimo_pagamento(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    form = EmprestimoPagamentoForm(request.POST or None)
    if form.is_valid():
        emprestimopagamento = form.save(commit=False)
        emprestimopagamento.emprestimo = emprestimo
        emprestimopagamento.save()        
    return redirect('emprestimo:emprestimo_detail', pk)
   
   

def emprestimo_pagamento_list(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    form = EmprestimoPagamentoForm()
    emprestimos = emprestimo.emprestimopagamento_set.all()
    context = {'emprestimo': emprestimo, 'form': form, 'emprestimos': emprestimos } 
    return render(request, 'emprestimo_pagamento_list.html', context)


