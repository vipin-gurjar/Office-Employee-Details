from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q


# Create your views here

def index(requests):
    return render(requests,'index.html')

def all_emp(requests):
    emps=Employee.objects.all()
    context={
    'emps': emps
    }
    return render(requests,'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

def remove_emp(requests, emp_id=0):
    if emp_id:
        try:
            emp_remove_to_be = Employee.objects.get(id=emp_id)
            emp_remove_to_be.delete()
            return HttpResponse("Employee to Removed Successfully")
        except:
            return HttpResponse("Please inter The Valid Employee id")


    
    emps=Employee.objects.all()
    context={
        'emps': emps
    }
   
    return render(requests,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)
    elif request.method=='GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')



