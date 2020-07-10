from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def cliente_select(request):
    return render(request, 'cliente_select.html')


