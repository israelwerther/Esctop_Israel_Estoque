from django.urls import path
from projeto.cliente import views as v

app_name='cliente'

urlpatterns = [
    path('', v.cliente_list, name='cliente_list'),
]
