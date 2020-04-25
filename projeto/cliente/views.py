from django.shortcuts import render
from .models import Cliente

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