from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp

def emp_home(request):

    emps=Emp.objects.all()
    return render(request, "emp/home.html",{
        'emps':emps
    })

def add_emp(request):
    if request.method=="POST":
        
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_Phone=request.POST.get("emp_Phone")
        emp_Address=request.POST.get("emp_Address")
        emp_Working=request.POST.get("emp_Working")
        emp_department=request.POST.get("emp_department")

        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.Phone=emp_Phone
        e.address=emp_Address
        e.department=emp_department
        if emp_Working is None:
            e.working=False
        else:
            e.Working=True

        e.save()



        return redirect("/emp/home/")
    return render(request, "emp/add_emp.html",{})

def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request, "emp/update_emp.html",{
        'emp':emp
    })

def do_Update_emp(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_Phone=request.POST.get("emp_Phone")
        emp_Address=request.POST.get("emp_Address")
        emp_Working=request.POST.get("emp_Working")
        emp_department=request.POST.get("emp_department")

        print(request.POST.get("emp_name"))
        print(request.POST.get("emp_department"))
        e=Emp.objects.get(pk=emp_id)

        e.name=emp_name
        e.emp_id=emp_id_temp
        e.Phone=emp_Phone
        e.address=emp_Address
        e.department=emp_department
        if emp_Working is None:
            e.working=False
        else:
            e.Working=True

        
        e.save()

    return redirect("/emp/home/")