from django.urls import path
from .views import clients, client_by_id

urlpatterns = [
    path('', clients, name='clients'),
    path('<int:id>/', client_by_id, name="client")
]