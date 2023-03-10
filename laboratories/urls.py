from django.urls import path
from .views import home, delete, edit


urlpatterns = [
    path('', home, name='laboratories'),
    path('delete/<int:id>', delete, name='delete_lab'),
    path('edit/<int:id>', edit, name='edit_lab')
]