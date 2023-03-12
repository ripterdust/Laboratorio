from django.urls import path
from .views import clients, client_by_id,delete, edit, store, history

urlpatterns = [
    path('', clients, name='clients'),
    path('<int:id>/', client_by_id, name="client"),
    path('delete/<int:id>', delete, name='remove_client' ),
    path('edit/<int:id>', edit, name='edit_client'),
    path('store/<int:id>', store, name='store_client'),
    path('history/<int:id>', history, name='patient_history')
]