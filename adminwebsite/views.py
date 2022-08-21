from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from website.models import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from website.EmailBackEnd import EmailBackEnd
from website.models import CustomUser
from django.urls import reverse
from website.models import speciality
from django.contrib.auth.decorators import login_required

@login_required(login_url='/adminlogin')
def admine(request):
    allPatients = patient_profile.objects.all()
    allDoctors = doctor_profile.objects.all()
    allappointments = appointment_booking.objects.all()
    countappointment = appointment_booking.objects.all().count()
    countdoctor = doctor_profile.objects.all().count()
    countpatient = patient_profile.objects.all().count()
    context = {'countpatient': countpatient,
               'countdoctor': countdoctor,
               'countappointment':countappointment,
               'allDoctors': allDoctors,
               'allappointments':allappointments,
               'allPatients':allPatients}

    return render(request,'admin.html',context)
def appointment_list(request):
    allappointments = appointment_booking.objects.all()
    return render(request,'appointment-list.html',{'allappointments':allappointments})
def blank_pagew(request):
    return render(request,'blank-pagew.html')
def componentsw(request):
    return render(request,'componentsw.html')
def data_tables(request):
    return render(request,'data-tables.html')
def doctor_list(request):
    doctorList = doctor_profile.objects.all()
    return render(request,'doctor-list.html', {'doctorList': doctorList})
def error_404(request):
    return render(request,'error-404.html')
def error_500(request):
    return render(request,'error-500.html')
def forgot_passwordw(request):
    return render(request,'forgot-passwordw.html')
def form_basic_inputs(request):
    return render(request,'form-basic-inputs.html')
def form_horizontal(request):
    return render(request,'form-horizontal.html')
def form_input_groups(request):
    return render(request,'form-input-groups.html')
def form_mask(request):
    return render(request,'form-mask.html')
def form_validation(request):
    return render(request,'form-validation.html')
def form_vertical(request):
    return render(request,'form-vertical.html')
def invoice_report(request):
    return render(request,'invoice-report.html')
def invoice(request):
    return render(request,'invoice.html')
def lock_screen(request):
    return render(request,'lock-screen.html')
# def loginw(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
#         if user is not None:
#             auth.login(request,user)
#             return redirect(admine)
#         else:
#             return render (request,'loginw.html', {'error':'Username or password is incorrect!'})
#     else:
#         return render(request,'loginw.html')
def loginw(request):
    return render(request,'loginw.html')

def adminlogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        print(user)
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return redirect(admine)
                # return HttpResponse("thi is admin")
            elif user.user_type=="2":
                return HttpResponse('you are a doctor you are not authorized to enter admin panel')
            else:
                return HttpResponse('you belongs to  patient section .you are not authorized to enter admin panel')
        else:

            return redirect(loginw)

@login_required(login_url='/adminlogin')
def patient_list(request):
    patientList = patient_profile.objects.all()
    return render(request,'patient-list.html' ,{'patientList':patientList})
def profilew(request,id):
    ProFileW = doctor_profile.objects.get(id=id)
    return render(request, 'profilew.html', {'ProFileW': ProFileW})
def patientProfileshow(request,id):
    patientProfileshow = patient_profile.objects.get(id=id)
    return render(request, 'patientprofilew.html', {'patientProfileshow': patientProfileshow})
def reviewsw(request):
    return render(request,'reviewsw.html')
def settings(request):
    return render(request,'settings.html')
def specialities(request):
    special = speciality.objects.all()
    return render(request,'specialities.html',{'special':special})
def specialities_delete(request, id):
    spe = speciality.objects.get(id=id)
    spe.delete()
    return HttpResponseRedirect(reverse('specialities'))
def add_specialities(request):
    if request.method == 'POST':
        specials = request.POST['specials']
        spec = speciality(
            speciality=specials
        )
        spec.save()
        return redirect(specialities)
    else:
        return HttpResponse('values are not added')

def table_basic(request):
    return render(request,'table-basic.html')
def transactions_list(request):
    return render(request,'transactions-list.html')
def registerw(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=1)
        user.save()
        return HttpResponse('admin singup successffull!!!')
    else:
        return render(request,'registerw.html')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('loginw'))

def doctor_delete(request, id):
    a = doctor_profile.objects.get(id=id)
    print(a.doctor)
    userselected  = CustomUser.objects.get(id=a.doctor.id)
    print(a,userselected)
    userselected.delete()

    return HttpResponseRedirect(reverse('doctor_list'))
def patient_delete(request, id):
    pat = patient_profile.objects.get(id=id)
    pat.delete()
    return HttpResponseRedirect(reverse('patient_list'))

