from django.urls import path
from projeto.cliente import views as v

app_name='cliente' 

urlpatterns = [
    path('', v.cliente_list, name='cliente_list'),
    path('<int:pk>/', v.cliente_detail, name='cliente_detail'),
    path('add/', v.cliente_add, name='cliente_add'),
]
