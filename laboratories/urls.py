from django.urls import path
from .views import home, delete, edit, store,new_lab, store_lab


urlpatterns = [
    path('', home, name='laboratories'),
    path('delete/<int:id>', delete, name='delete_lab'),
    path('edit/<int:id>', edit, name='edit_lab'),
    path('update/<int:id>', store, name='store_lab'),
    path('new/', new_lab, name='new_lab'),
    path('store/',store_lab, name='store_lab')
]