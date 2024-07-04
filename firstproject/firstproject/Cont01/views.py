from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Department
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserBean
from django.core.paginator import Paginator


def home_view(request):
    return render(request, 'home.html')

def hello_view(request):
    context = {'greeting': 'こんにちは、SpringMVC!'}
    return render(request, 'hello.html', context)

def input_view(request):
    return render(request, 'input.html')

def form_view(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        address = request.POST.get('address')
        userlen = len(user)
        addrlen = len(address)
        context = {
            'user': user,
            'userlen': userlen,
            'address': address,
            'addrlen': addrlen,
        }
        return render(request, 'form.html', context)
    return HttpResponse("Invalid request")

def foobar_view(request):
    return render(request, 'foobar.html')

class EmployeeController(View):
    def get(self, request, no=None):
        if no:
            employee = get_object_or_404(Employee, no=no)
            data = {
                'no': employee.no,
                'name': employee.name,
                'salary': employee.salary,
            }
            return JsonResponse(data)
        else:
            employees = Employee.objects.all()
            data = list(employees.values('no', 'name', 'salary'))
            return JsonResponse(data, safe=False)

    def post(self, request):
        # 新しい社員の追加処理をここに記述
        pass

    def put(self, request, no):
        # 社員情報の更新処理をここに記述
        pass

    def delete(self, request, no):
        # 社員情報の削除処理をここに記述
        pass

def init_employees(request):
    Employee.objects.all().delete()
    Employee.objects.create(no=1234, name="田中", salary=540000)
    Employee.objects.create(no=2345, name="山田", salary=380000)
    Employee.objects.create(no=3456, name="鈴木", salary=250000)
    return redirect('/employees/')

def employee_index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})

# def update_employee(request):
#     if request.method == 'POST':
#         no = request.POST.get('no')
#         name = request.POST.get('name')
#         salary = request.POST.get('salary')

#         employee = get_object_or_404(Employee, no=no)
#         employee.name = name
#         employee.salary = salary
#         employee.save()

#         return render(request, 'employee/save.html', {'employee': employee})
#     return HttpResponse("Invalid request", status=400)

# def delete_employee(request):
#     if request.method == 'POST':
#         no = request.POST.get('no')
#         employee = get_object_or_404(Employee, no=no)
#         employee.delete()
#         return redirect('/employee/')
#     return HttpResponse("Invalid request", status=400)

def new_employee(request):
    return render(request, 'employee/new.html')

def create_employee(request):
    if request.method == 'POST':
        no = request.POST.get('no')
        name = request.POST.get('name')
        salary = request.POST.get('salary')

        employee = Employee(no=no, name=name, salary=salary)
        employee.save()

        return render(request, 'employee/save.html', {'employee': employee})
    return HttpResponse("Invalid request", status=400)

def employee_index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})

def edit_employee(request, no):
    employee = get_object_or_404(Employee, pk=no)
    return render(request, 'employee/edit.html', {'employee': employee})

def update_employee(request, no):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, pk=no)
        employee.name = request.POST.get('name')
        employee.salary = request.POST.get('salary')
        employee.save()
        return redirect('employee_list')
    return HttpResponse("Invalid request", status=400)

def delete_employee(request, no):
    employee = get_object_or_404(Employee, pk=no)
    employee.delete()
    return redirect('employee_list')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_detail(request, no):
    department = get_object_or_404(Department, pk=no)
    return render(request, 'department_detail.html', {'department': department})

def init_view(request):
    Employee.objects.all().delete()
    Department.objects.all().delete()

    dept1 = Department.objects.create(no=101, name='総務部')
    dept2 = Department.objects.create(no=201, name='経理部')
    dept3 = Department.objects.create(no=301, name='技術部')

    Employee.objects.create(no=1234, name='田中', salary=540000, department=dept1)
    Employee.objects.create(no=2345, name='山田', salary=380000, department=dept3)
    Employee.objects.create(no=3456, name='鈴木', salary=250000, department=dept2)
    Employee.objects.create(no=4567, name='山本', salary=290000, department=dept2)
    Employee.objects.create(no=5678, name='木村', salary=470000, department=dept3)
    Employee.objects.create(no=6789, name='村田', salary=330000, department=dept1)

    return redirect('/employee/')

def department_index(request):
    context = {'dept': Department()}
    return render(request, 'department/index.html', context)

def department_search(request):
    no = request.GET.get('no')
    dept = get_object_or_404(Department, no=no)
    context = {'dept': dept}
    return render(request, 'department/index.html', context)

def veteran_employees(request):
    veterans = Employee.objects.find_veteran()
    return render(request, 'employee/veterans.html', {'employees': veterans})

def search_employees_by_name(request):
    name = request.GET.get('name', '')
    employees = Employee.objects.find_by_name_like_prefix(name)
    return render(request, 'employee/search.html', {'employees': employees})

def new_employee_form(request):
    form = EmployeeForm()
    return render(request, 'employee/new.html', {'form': form})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.department = Department.objects.get(no=emp.dept_no)
            emp.save()
            return redirect('employee_list')
        else:
            return render(request, 'employee/new.html', {'form': form})
    else:
        form = EmployeeForm()
        return render(request, 'employee/new.html', {'form': form})

def edit_employee_form(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    form = EmployeeForm(instance=employee)
    return render(request, 'employee/edit.html', {'form': form})


def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee/edit.html', {'form': form})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee.delete()
    return redirect('employee_list')

def employee_create_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/new.html', {'form': form})

def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user_bean = UserBean(id=user.id, name=user.username)
                request.session['user_bean'] = {'id': user_bean.id, 'name': user_bean.name}
                return redirect('mypage')
    else:
        form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form})

@login_required
def mypage_view(request):
    user_bean_data = request.session.get('user_bean')
    if user_bean_data:
        user_bean = UserBean(id=user_bean_data['id'], name=user_bean_data['name'])
        return render(request, 'login/mypage.html', {'user_bean': user_bean})
    return redirect('login')

def logout_view(request):
    logout(request)
    return render(request, 'login/next.html')

def last_view(request):
    return render(request, 'login/last.html')

def employee_list(request):
    employee_list = Employee.objects.all()
    paginator = Paginator(employee_list, 10)  # 1ページに表示するアイテム数を設定

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee/list.html', {'page_obj': page_obj})