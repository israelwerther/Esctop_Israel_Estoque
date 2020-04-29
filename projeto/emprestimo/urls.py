from django.urls import path
from projeto.emprestimo import views as v

app_name='emprestimo' 

urlpatterns = [
    path('', v.emprestimo_entrada_list, name='emprestimo_entrada_list'),
    path('<int:pk>/', v.emprestimo_entrada_detail, name='emprestimo_entrada_detail'),
    # path('add/', v.ClienteCreate.as_view(), name='cliente_add'),
    # path('<int:pk>/edit/', v.ClienteUpdate.as_view(), name='cliente_edit'),
]