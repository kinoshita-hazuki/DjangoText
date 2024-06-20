from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.views import View

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

def update_employee(request):
    if request.method == 'POST':
        no = request.POST.get('no')
        name = request.POST.get('name')
        salary = request.POST.get('salary')

        employee = get_object_or_404(Employee, no=no)
        employee.name = name
        employee.salary = salary
        employee.save()

        return render(request, 'employee/save.html', {'employee': employee})
    return HttpResponse("Invalid request", status=400)

def delete_employee(request):
    if request.method == 'POST':
        no = request.POST.get('no')
        employee = get_object_or_404(Employee, no=no)
        employee.delete()
        return redirect('/employee/')
    return HttpResponse("Invalid request", status=400)