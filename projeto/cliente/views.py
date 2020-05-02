from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm



def cliente_list(request):
    template_name='cliente_list.html'
    objects=Cliente.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)


def cliente_detail(request, pk):
    template_name='cliente_detail.html'
    obj=Cliente.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)


# def cliente_add(request):
#     template_name='cliente_form.html'
#     return render(request, template_name)


class ClienteCreate(CreateView):
    model=Cliente
    template_name='cliente_form.html'
    form_class=ClienteForm
    
    
class ClienteUpdate(UpdateView):
    model=Cliente
    template_name='cliente_form.html'
    form_class=ClienteForm
    

class ClienteDelete(DeleteView):
    model=Cliente
    template_name='cliente_delete.html'    
    success_url = reverse_lazy('cliente:cliente_list')
    
    