from django.urls import path
from projeto.emprestimo import views as v

app_name='emprestimo' 

urlpatterns = [
    path('', v.emprestimo_list, name='emprestimo_list'),
    path('<int:pk>/', v.emprestimo_detail, name='emprestimo_detail'),
    path('add/', v.EmprestimoCreate.as_view(), name='emprestimo_add'),
    # path('<int:pk>/edit/', v.ClienteUpdate.as_view(), name='cliente_edit'),
]