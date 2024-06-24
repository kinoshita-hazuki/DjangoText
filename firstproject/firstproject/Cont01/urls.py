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
    update_employee,
    delete_employee,
    new_employee,
    create_employee,
    edit_employee,
    department_detail,
    department_list,
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
    path('employees/new/', new_employee, name='new_employee'), 
    path('employee/', employee_index, name='employee_index'),
    path('update/', update_employee, name='update_employee'),
    path('delete/', delete_employee, name='delete_employee'),  
    path('employees/create/', create_employee, name='create_employee'), 
    path('init/', init_employees, name='init_employees'),
    path('employees/', employee_index, name='employee_list'),
    path('employees/edit/<int:no>/', edit_employee, name='edit_employee'),
    path('employees/update/<int:no>/', update_employee, name='update_employee'),
    path('employees/delete/<int:no>/', delete_employee, name='delete_employee'),
    path('departments/', department_list, name='department_list'),
    path('departments/<int:no>/', department_detail, name='department_detail'),
    path('init/', views.init_view, name='init'),

]
