from django.urls import path
from .views import index,fields_by_lab_id

urlpatterns = [
    path('', index, name='fields'),
    path('lab/<int:lab_id>', fields_by_lab_id, name='fields_by_lab')
]