from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Cliente_cnpj
from projeto.avalista.models import Avalista
from .forms import Cliente_cnpjForm
from projeto.avalista.forms import AvalistaForm

@login_required
def cliente_cnpj_list(request):
    template_name='cliente_cnpj_list.html'
    objects=Cliente_cnpj.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)
    


@login_required
def cliente_cnpj_cadastra(request):
    cnpjs = Cliente_cnpj.objects.all()
    avalistas = Avalista.objects.all()
    form1 = Cliente_cnpjForm()
    form2 = AvalistaForm()
    data = {'cnpjs': cnpjs, 'avalistas': avalistas,'form1': form1, 'form2': form2} 
    return render(request, 'cliente_cnpj_form.html', data)


@login_required
def cliente_cnpj_add(request): 
    form1=Cliente_cnpjForm(request.POST or None)
    form2=AvalistaForm(request.POST or None)
    if form1.is_valid() and form2.is_valid():
        form1.save()
        form2.save()  
    
    return redirect('cliente_cnpj:cliente_cnpj_list')


# class Add_Emp(CreateView):
#     model = NewEmployee
#     form_class = NewEmpForm

#     def form_valid(self, form):
#         employee = form.save()  # save form
#         return redirect('newemp-rev', pk=employee.pk)
    

# @login_required
# def cliente_cnpj_add(request):
#     avalista = get_object_or_404(Avalista, pk=pk)
#     form1=Cliente_cnpjForm(request.POST or None)
#     form2=AvalistaForm(request.POST or None)
#     if form1.is_valid() and form2.is_valid():
#         form1.save()
#         form2.save()
#         AvalistaForm = form2.save(commit=False)
#         AvalistaForm = avalista
#         AvalistaForm.save()
#     return redirect('cliente_cnpj:cliente_cnpj_list')

#     def form_valid(self, form2):
#         obj = form2.save(commit=False)
#         obj.fiador = self.request
#         return super(cliente_cnpj_add, self).form_valid(form2)


@login_required
def cliente_cnpj_detail(request, pk):
    template_name='cliente_cnpj_detail.html'
    obj=Cliente_cnpj.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)
    # template_name='cliente_cnpj_form.html'
    # form_class=Cliente_cnpjForm
    # form1 = AvalistaForm(request.POST or None)
    # form2 = TesteForm(request.POST or None)


@login_required
def cliente_cnpjupdate(request, pk):
    data = {}
    cliente_cnpj = Cliente_cnpj.objects.get(pk=pk)
    form1 = Cliente_cnpjForm(request.POST or None, instance=cliente_cnpj)
    data['cliente_cnpj'] = cliente_cnpj
    data['form1'] = form1

    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
            return redirect('cliente_cnpj:cliente_cnpj_list')
        else:
            # messages.error(request, 'Dados inválidos')
            return render(request, 'cliente_cnpj_form.html', data)  
    else:
        return render(request, 'cliente_cnpj_form.html', data)  


# class Cliente_cnpjUpdate(UpdateView):
#     model=Cliente_cnpj   
#     model1=Avalista   
#     template_name='cliente_cnpj_form.html'
#     form_class = Cliente_cnpjForm


class Cliente_cnpjDelete(DeleteView):
    model=Cliente_cnpj
    template_name ='cliente_cnpj_delete.html'    
    success_url = reverse_lazy('cliente_cnpj:cliente_cnpj_list')