from django.urls import path
from projeto.cliente import views as v

app_name='cliente' 

urlpatterns = [
    path('', v.cliente_list, name='cliente_list'),
    path('<int:pk>/', v.cliente_detail, name='cliente_detail'),
    path('add/', v.ClienteCreate.as_view(), name='cliente_add'),
    path('<int:pk>/edit/', v.ClienteUpdate.as_view(), name='cliente_edit'),
    path('<int:pk>/delete/', v.ClienteDelete.as_view(), name='cliente_delete'),
]
