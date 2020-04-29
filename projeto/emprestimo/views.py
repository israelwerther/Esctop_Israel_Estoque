from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from .models import Emprestimo, EmprestimoItens
from .forms import EmprestimoForm, EmprestimoItensForm


def emprestimo_entrada_list(request):
    tamplate_name='emprestimo_entrada_list.html'
    objects = Emprestimo.objects.filter(movimento='r')
    context = {'object_list': objects}
    return render(request, tamplate_name, context)


def emprestimo_entrada_detail(request, pk):
    tamplate_name='emprestimo_entrada_detail.html'
    obj = Emprestimo.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, tamplate_name, context)


def emprestimo_entrada_add(request):
    tamplate_name = 'emprestimo_entrada_form.html'    
    emprestimo_form = Emprestimo()
    item_emprestimo_formset = inlineformset_factory(
        Emprestimo,
        EmprestimoItens,
        form = EmprestimoItensForm,
        extra = 0,
        min_num = 1,
        validate_min = True,
    )
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo_form, prefix='main')
        formset = item_emprestimo_formset(
            request.POST,
            instance = emprestimo_form, 
            prefix = 'emprestimo'
        )
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            url = 'emprestimo:emprestimo_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))         
    else: #case ele esteja vazio
        form = EmprestimoForm(instance=emprestimo_form, prefix='main')
        formset = item_emprestimo_formset(instance=emprestimo_form, prefix='emprestimo')           
    context = {'form': form, 'formset': formset}
    return render(request, tamplate_name, context)

