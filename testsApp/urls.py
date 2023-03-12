from django.urls import path
from .views import index, fill_fields, completed_tests, uncompleted_tests, save_uncompleted_test, send_pdf, new_test, store_new_test

urlpatterns = [
    path('', index, name="tests"),
    path('fill-fields/<int:test_id>', fill_fields, name='fill_fields'),
    path('completed/', completed_tests, name="completed_tests"),
    path('uncompleted/', uncompleted_tests, name="uncompleted_tests"),
    path('store_fiels/<int:test_id>', save_uncompleted_test, name='save_uncompleted_test'),
    path('pdf/<int:test_id>', send_pdf, name='send_pdf'),
    path('new/', new_test, name='new_test'),
    path('store-new-test/', store_new_test, name='store_new_test')
]