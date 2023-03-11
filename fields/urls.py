from django.urls import path
from .views import index,fields_by_lab_id, remove

urlpatterns = [
    path('', index, name='fields'),
    path('lab/<int:lab_id>', fields_by_lab_id, name='fields_by_lab'),
    path('remove/<int:id>', remove, name='remove_field')
]