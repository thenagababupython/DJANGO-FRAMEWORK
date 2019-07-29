from django.shortcuts import render
from .forms import EmpForm
from .models import EmpData
from django.http.response import HttpResponse


# Create your views here.
def emp_view(request):
    if request.method=="POST":
        eform=EmpForm(request.POST)
        if eform.is_valid():
            name1=request.POST.get('name')
            email1=request.POST.get('email')
            salary1=request.POST.get('salary')
            location1=request.POST.get('location')
            data=EmpData(name=name1,email=email1,salary=salary1,location=location1)
            data.save()
            eform=EmpForm()
            return render(request,'emp_data.html',{'abcd':eform})
        else:
            return HttpResponse('invalid data')
    else:
        eform=EmpForm()
        return render(request,'emp_data.html',{'abcd':eform})

def Fetchingdata(request):
    edata=EmpData.objects.all()
    return render(request,'emp_data_display.html',{'edata':edata})