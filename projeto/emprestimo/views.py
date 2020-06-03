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
    

class EmprestimoPromissoria(UpdateView):
    model=Emprestimo
    template_name='emprestimo_promissoria.html'
    form_class=EmprestimoForm


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





# def Idioma(request):
#     form_idioma = IdiomaForm()
#     form_ling = LinguagemForm()
#     return render(request, 'curriculo/idioma.html', {'form1': form_idioma, 'form2': form_ling})


# class NegotiationGroupMultifacetedView(TemplateView):
#     ### TemplateResponseMixin
#     template_name = 'offers/offer_detail.html'

#     ### ContextMixin 
#     def get_context_data(self, **kwargs):
#         """ Adds extra content to our template """
#         context = super(NegotiationGroupDetailView, self).get_context_data(**kwargs)

#         ...

#         context['negotiation_bid_form'] = NegotiationBidForm(
#             prefix='NegotiationBidForm', 
#             ...
#             # Multiple 'submit' button paths should be handled in form's .save()/clean()
#             data = self.request.POST if bool(set(['NegotiationBidForm-submit-counter-bid',
#                                               'NegotiationBidForm-submit-approve-bid',
#                                               'NegotiationBidForm-submit-decline-further-bids']).intersection(
#                                                     self.request.POST)) else None,
#             )
#         context['offer_attachment_form'] = NegotiationAttachmentForm(
#             prefix='NegotiationAttachment', 
#             ...
#             data = self.request.POST if 'NegotiationAttachment-submit' in self.request.POST else None,
#             files = self.request.FILES if 'NegotiationAttachment-submit' in self.request.POST else None
#             )
#         context['offer_contact_form'] = NegotiationContactForm()
#         return context

#     ### NegotiationGroupDetailView 
#     def post(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)

#         if context['negotiation_bid_form'].is_valid():
#             instance = context['negotiation_bid_form'].save()
#             messages.success(request, 'Your offer bid #{0} has been submitted.'.format(instance.pk))
#         elif context['offer_attachment_form'].is_valid():
#             instance = context['offer_attachment_form'].save()
#             messages.success(request, 'Your offer attachment #{0} has been submitted.'.format(instance.pk))
#                 # advise of any errors

#         else 
#             messages.error('Error(s) encountered during form processing, please review below and re-submit')

#         return self.render_to_response(context)