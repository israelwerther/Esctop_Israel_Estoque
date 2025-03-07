from django.contrib.auth.decorators import login_required
from django.urls import path, include
from projeto.emprestimo import views as v
# from .views import emprestimo_pagamento

app_name='emprestimo' 

urlpatterns = [
    path('', v.emprestimo_list, name='emprestimo_list'),
    path('add/', login_required(v.EmprestimoCreate.as_view()), name='emprestimo_add'),
    path('<int:pk>/delete/', login_required(v.EmprestimoDelete.as_view()), name='emprestimo_delete'),  
    
    
    path('<int:pk>/impress/', login_required(v.EmprestimoImpress.as_view()), name='emprestimo_impress'),
    path('<int:pk>/promissoria/', login_required(v.EmprestimoPromissoria.as_view()), name='emprestimo_promissoria'),
    path('<int:pk>/contrato/', login_required(v.EmprestimoContrato.as_view()), name='emprestimo_contrato'),
    path('<int:pk>/', v.emprestimo_detail, name='emprestimo_detail'),
    
    
    path('<int:pk>/edit/', login_required(v.EmprestimoUpdate.as_view()), name='emprestimo_edit'),  
    path('<int:pk>/pagamento_add/', v.emprestimo_pagamento_add, name='emprestimo_pagamento_add'),
    path('<int:pk>/pagamento/', v.emprestimo_pagamento, name='emprestimo_pagamento'),
    path('<int:pk>/pagamento_list/', v.emprestimo_pagamento_list, name='emprestimo_pagamento_list'),
]