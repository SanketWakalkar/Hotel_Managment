from django.http import HttpResponse
from django.shortcuts import render

import datetime

def home(request):
    isActive=True
    if request.method=='POST':
        check=request.POST.get("check")
        print(check)
        if check is not None: isActive=False
        else: isActive=True

    date=datetime.datetime.now()
    name="ReviwWithSanket"
    list_of_programs=[
        'Write a PhotoReview which is your fav',
        'Review a Best Moment',
        'Best Couple Photo',
        'Best Group Photo'

    ]
    Client={
        'Client_name':"Sameer",
        'Client_college':"NCI",
        'Client_city':"Dublin"
    }

    print("test function is called from view")
    # return HttpResponse("<h1>Hello this is index page</h1>")
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'Client_data':Client
    }
    return render(request,"home.html",data)

def about(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1>This is Services Page</h1>")
    return render(request,"services.html",{})
