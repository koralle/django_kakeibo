from django.urls import path
from .views import BalanceList, DetailBalance, balance_edit, balance_delete

app_name = 'kakeibo'
urlpatterns = [
    path('list/', view = BalanceList.as_view(), name='balance_list'),
    path('detail/<int:pk>/', view = DetailBalance.as_view(), name='balance_detail'),
    path('add/', view = balance_edit, name='balance_add'),
    path('edit/<int:balance_id>/', view = balance_edit, name='balance_edit'),
    path('delete/<int:balance_id>/', view = balance_delete, name='balance_delete')
]