from django.urls import path
from .views import index,fields_by_lab_id, remove, edit_field, store, store_by_edit_lab

urlpatterns = [
    path('', index, name='fields'),
    path('lab/<int:lab_id>', fields_by_lab_id, name='fields_by_lab'),
    path('remove/<int:id>', remove, name='remove_field'),
    path('edit/<int:id>', edit_field, name='update_field'),
    path('store/<int:id>', store, name='store_field'),
    path('store_by_lab/<int:lab_id>', store_by_edit_lab, name='store_by_edit_lab')
]