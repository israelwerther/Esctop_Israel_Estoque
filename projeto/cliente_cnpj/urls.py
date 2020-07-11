from django.contrib.auth.decorators import login_required
from django.urls import path
from projeto.cliente_cnpj import views as v

app_name='cliente_cnpj' 

urlpatterns = [
    path('', v.cliente_cnpj_list, name='cliente_cnpj_list'),   
    path('<int:pk>/', v.cliente_cnpj_detail, name='cliente_cnpj_detail'),
    path('add/', login_required(v.Cliente_CnpjCreate.as_view()), name='cliente_cnpj_add'),
]