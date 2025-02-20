from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect,reverse
from api.models import Technician
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.db.models import Q

# Create your views here.
def home_view(request):
    #return HttpResponseRedirect('afterlogin')
    return render(request,'site/index.html')

from api import models
import requests
#admin dashboard
# @login_required(login_url='adminlogin')
# @user_passes_test(is_admin)
def admin_dashboard_view(request):
    #for both table in admin dashboard
    Technician = f'http://127.0.0.1:8000/api/technicians/'
    
    response = requests.get(Technician)
    
    data = response.json()
    TotalTechnicians = data['TotalTechnicians']
    print(TotalTechnicians)
    #Technician=models.Technician.objects.all().order_by('-id')
    Customer=models.Customer.objects.all().order_by('-id')
    #for three cards
    techniciancount=models.Technician.objects.all().filter(status=True).count()
    pendingtechniciancount=models.Technician.objects.all().filter(status=False).count()

    customercount=models.Customer.objects.all().filter(status=True).count()
    pendingcustomercount=models.Customer.objects.all().filter(status=False).count()

    appointmentcount=models.Appointment.objects.all().filter(status=True).count()
    pendingappointmentcount=models.Appointment.objects.all().filter(status=False).count()
    mydict={
    #'Technician':Technician,
    'TotalTechnicians':TotalTechnicians,
    'Customer':Customer,
    'techniciancount':techniciancount,
    'pendingtechniciancount':pendingtechniciancount,
    'customercount':customercount,
    'pendingcustomercount':pendingcustomercount,
    'appointmentcount':appointmentcount,
    'pendingappointmentcount':pendingappointmentcount,
    }
    return render(request,'adminn/dashboard.html',context=mydict)