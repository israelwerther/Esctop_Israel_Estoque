from django.urls import path, include
from projeto.emprestimo import views as v
# from .views import emprestimo_pagamento

app_name='emprestimo' 

urlpatterns = [
    path('', v.emprestimo_list, name='emprestimo_list'),
    path('<int:pk>/impress/', v.EmprestimoImpress.as_view(), name='emprestimo_impress'),
    path('<int:pk>/', v.emprestimo_detail, name='emprestimo_detail'),
    path('add/', v.EmprestimoCreate.as_view(), name='emprestimo_add'),
    path('<int:pk>/edit/', v.EmprestimoUpdate.as_view(), name='emprestimo_edit'),    
    
    path('<int:pk>/pagamento_add/', v.emprestimo_pagamento_add, name='emprestimo_pagamento_add'),
    path('<int:pk>/pagamento/', v.emprestimo_pagamento, name='emprestimo_pagamento'),
]