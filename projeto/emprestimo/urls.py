from django.urls import path
from projeto.emprestimo import views as v

app_name='emprestimo' 

urlpatterns = [
    path('', v.emprestimo_list, name='emprestimo_list'),
    # path('<int:pk>/', v.cliente_detail, name='cliente_detail'),
    # path('add/', v.ClienteCreate.as_view(), name='cliente_add'),
    # path('<int:pk>/edit/', v.ClienteUpdate.as_view(), name='cliente_edit'),
]