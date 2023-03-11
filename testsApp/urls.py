from django.urls import path
from .views import index, fill_fields, completed_tests, uncompleted_tests

urlpatterns = [
    path('', index, name="tests"),
    path('fill-fields/<int:test_id>', fill_fields, name='fill_fields'),
    path('completed/', completed_tests, name="completed_tests"),
    path('uncompleted/', uncompleted_tests, name="uncompleted_tests")
]