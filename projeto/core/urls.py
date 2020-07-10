from django.urls import path
from projeto.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('cliente_select/', v.cliente_select, name='cliente_select'),
]
