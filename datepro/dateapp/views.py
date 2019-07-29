from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
import datetime as dt
date1=dt.datetime.now()


def datetime(request):
    return HttpResponse("<h1> the current time and date is {} </h1>".format(date1))