from django.urls import path
from .views import index, fill_fields

urlpatterns = [
    path('', index, name="tests"),
    path('fill-fields/<int:test_id>', fill_fields, name='fill_fields')
]