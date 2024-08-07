from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

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
    department_search,
    employee_create_view, 
    employee_list_view,
    login_view,
    logout_view,
    mypage_view,
    last_view,
)

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)


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
    path('employee/', employee_list_view, name='employee_list'),
    path('employee/new/', employee_create_view, name='employee_create'), 
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
    path('department/', views.department_index, name='department_index'),
    path('department/search/', views.department_search, name='department_search'),
    path('employee/veterans/', views.veteran_employees, name='veteran_employees'),
    path('employee/search/', views.search_employees_by_name, name='search_employees_by_name'),
    path('login/', login_view, name='login'),
    path('mypage/', mypage_view, name='mypage'),
    path('logout/', logout_view, name='logout'),
    path('last/', last_view, name='last'),
    path('home/', home_view, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
     path('', include(router.urls)),
]

