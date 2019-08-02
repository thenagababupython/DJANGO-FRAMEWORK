from django.shortcuts import render
from .models import EnquiryData
from .forms import EnquiryForm
from django.http.response import HttpResponse

# Create your views here.

def Enquiry_View(request):
    if request.method=='POST':
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            skills=eform.cleaned_data.get('skills')
            locations=eform.cleaned_data.get('location')
            gender=eform.cleaned_data.get('gender')
            date=eform.cleaned_data.get('date')

            data=EnquiryData(
                name=name,
                email=email,
                mobile=mobile,
                skills=skills,
                locations=locations,
                gender=gender,
                date=date
            )
            data.save()
            eform=EnquiryForm()
            return  render(request,'enquiryform.html',{'eform':eform})
        else:
            return HttpResponse('inavlid data')
    else:
        eform=EnquiryForm()
        return render(request,'enquiryform.html',{'eform':eform})

def Fectching_data_display(request):
    edata=EnquiryData.objects.all()
    return render(request,'enquiry_data_display.html',{'edata':edata})
