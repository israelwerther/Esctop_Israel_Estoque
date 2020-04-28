from django.shortcuts import render
from .models import Emprestimo

def emprestimo_entrada_list(request):
    tamplate_name='emprestimo_entrada_list.html'
    objects = Emprestimo.objects.filter(movimento='r')
    context={'object_list': objects}
    return render(request, tamplate_name, context)

