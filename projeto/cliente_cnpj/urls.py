from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente_cnpj import views as v

app_name='cliente_cnpj' 

urlpatterns = [
    path('', v.cliente_cnpj_list, name='cliente_cnpj_list'),   
]