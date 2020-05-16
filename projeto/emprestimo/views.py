from django.shortcuts import render, resolve_url
from django.views.generic import CreateView, UpdateView
from .models import Emprestimo
from .forms import EmprestimoForm



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
    




