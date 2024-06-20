from django.contrib import admin
from django.urls import path
from . import views
from Cont01.views import (
    EmployeeController,
    home_view, 
    hello_view, 
    input_view, 
    form_view,
    foobar_view,
    init_employees,
    employee_index,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('hello/', hello_view, name='hello'),
    path('sample/input/', input_view, name='input'),
    path('sample/form/', form_view, name='form'),
    path('foobar/', views.foobar_view, name='foobar'), 
    path('employees/', EmployeeController.as_view(), name='employee_list'),
    path('employees/<int:no>/', EmployeeController.as_view(), name='employee_detail'),
    path('init/', init_employees, name='init_employees'),
    path('employee/', employee_index, name='employee_index'),
]
