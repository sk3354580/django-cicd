from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, StreamingHttpResponse
from .models import *
from . EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.views.decorators import gzip
# Create your views her
import cv2
from django.shortcuts import render, redirect, HttpResponse



def addbilling(request):
    return render(request, 'add-billing.html')


def addprescription(request):
    return render(request, 'add-prescription.html')


def appointments(request):
    return render(request, 'appointments.html')


def blankpage(request):
    return render(request, 'blank-page.html')


def booking(request):
    return render(request, 'booking.html')


def bookings(request, bid):
    bid = bid
    bookingProFile = doctor_profile.objects.get(id=bid)
    return render(request, 'bookings.html', {'bookingProfile': bookingProFile})


@login_required(login_url='/websitelogin')
def bookingsuccess(request, bid):
    appointmentbooking = appointment_booking.objects.all()
    bookingProFile = doctor_profile.objects.get(id=bid)
    bookingdone = {
        'ftime': ftime,
        'ttime': ttime,
        'datet': datet,
        'bookingProFile': bookingProFile,
        'appointmentbooking': appointmentbooking,
    }
    return render(request, 'booking-success.html', bookingdone)


def calender(request):
    return render(request, 'calendar.html')


def changepassword(request):
    return render(request, 'change-password.html')


def chat(request):
    return render(request, 'chat.html')


def chatdoctor(request):
    return render(request, 'chat-doctor.html')

@login_required(login_url='/websitelogin')
def checkout(request,bid):

    if request.method == 'POST':
        global ftime
        ftime = request.POST['ftime']
        global ttime
        ttime = request.POST['ttime']
        global datet
        datet = request.POST['dates']
        return redirect('checkouts', bid=bid)
    else:
        return render(request, 'checkout.html')


def checkouts(request, bid):
    patienid = request.user.id
    patientbookingid = patient_profile.objects.get(patient=patienid)
    bookingProFile = doctor_profile.objects.get(id=bid)
    total = bookingProFile.consultation_fees + 60
    print(bookingProFile.id)
    timetable = {
        'ftime': ftime,
        'ttime': ttime,
        'datet': datet,
        'bookingProFile': bookingProFile,
        'total': total,
        'bid': bid,
    }
    if request.method == 'POST':
        from_time = ftime
        to_time = ttime
        datec = datet

        Payment_card = request.POST['nameoncard']
        global card_number
        card_number = request.POST['cardnumber']
        expire_month = request.POST['expirymonth']
        expire_year = request.POST['expiryyear']
        Cvv = request.POST['cvv']
        amount = request.POST['amount']
        # doctor_name = bookingProFile.username
        card = appointment_booking(
            appointment_doctor_id = bookingProFile,
            appointment_patient_id = patientbookingid,
            from_time=from_time,
            to_time=to_time,
            date=datec,
            Payment_card=Payment_card,
            card_number=card_number,
            expire_month=expire_month,
            expire_year=expire_year,
            Cvv=Cvv,
            amount_paid=amount,

            # Doctor_name=doctor_name
        )
        card.save()
        return redirect('bookingsuccess', bid=bid)
    else:
        return render(request, 'checkout.html', timetable)


def components(request):
    return render(request, 'components.html')


def doctorchangepassword(request):
    return render(request, 'doctor-change-password.html')

@login_required(login_url='/websitelogin')
def doctordashboard(request):
    sel_doc = doctor_profile.objects.get(doctor=request.user)
    allappointments = appointment_booking.objects.filter(appointment_doctor_id=sel_doc)
    all_count = allappointments.count()
    return render(request, 'doctor-dashboard.html',{'appoints':allappointments,'all_count':all_count})


def doctorprofile(request, id):
    DOctorProFile = doctor_profile.objects.get(id=id)
    return render(request, 'doctor-profile.html', {'DOctorProFile': DOctorProFile,'rid':id})


def doctorprofilesettings(request):
    allDoctors = doctor_profile.objects.all()
    special = speciality.objects.all
    results = Location.objects.all

    if request.method == 'POST':
        doctor = request.user
        doctor_images = request.FILES['image']
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        phone_number = request.POST['mnumber']
        date_of_birth = request.POST['dob']
        gender = request.POST['special']
        biography = request.POST['biography']
        clinic_name = request.POST['clinicname']
        clinic_address = request.POST['clinicadress']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        postalcode = request.POST['postalcode']
        services = request.POST['services']
        specialist = request.POST['specialist']
        degree = request.POST['degree']
        college = request.POST['college']
        yoc = request.POST['yoc']
        hospitalname = request.POST['hospitalname']
        froms = request.POST['froms']
        to = request.POST['to']
        designation = request.POST['designation']
        awards = request.POST['awards']
        year = request.POST['year']
        memberships = request.POST['memberships']
        registrations = request.POST['registrations']
        registrationyear = request.POST['registrationyear']
        clinic_images = request.FILES['clinicimage']
        consultation_fees = request.POST['consultationfees']
        doc_present = doctor_profile.objects.get(doctor = request.user)
        print(doc_present)

        if (doc_present):

            doc_present.first_name = firstname
            # doc_present.doctor = request.user
            # doc_present.username = username,
            # doc_present.doctor = doctor,
            doc_present.doctor_images = doctor_images
            doc_present.first_name = firstname
            doc_present.last_name = lastname
            doc_present.Biography = biography
            doc_present.clinic_name = clinic_name
            doc_present.clinic_address = clinic_address
            doc_present.Address_line1 = address1
            doc_present.Address_line2 = address2
            doc_present.City = city
            doc_present.State_Provice = state
            doc_present.Country = country
            doc_present.Services = services
            doc_present.Specialiazation = specialist
            doc_present.Degree = degree
            doc_present.College_Institute = college
            doc_present.Hospital_Name = hospitalname
            doc_present.Designation = designation
            doc_present.Awards = awards
            doc_present.Memberships = memberships
            doc_present.Registrations = registrations
            # doc_present.Date_of_Birth = date_of_birth
            # doc_present.Year_of_Completion = yoc
            # doc_present.From = froms
            # doc_present.To = to
            # doc_present.Year = year
            # doc_present.Year_of_Registeration = registrationyear
            doc_present.email = email
            doc_present.clinic_images = clinic_images
            doc_present.Postal_code = postalcode
            # doc_present.phoneNumber = phone_number,
            # doc_present.Gender = gender
            doc_present.consultation_fees = consultation_fees
            doc_present.save()
            return redirect(doctordashboard)
        else:
            b = doctor_profile(username=username,
                           doctor = doctor,
                           doctor_images=doctor_images,
                           first_name=firstname,
                           last_name=lastname,
                           Biography=biography,
                           clinic_name=clinic_name,
                           clinic_address=clinic_address,
                           Address_line1=address1,
                           Address_line2=address2,
                           City=city,
                           State_Provice=state,
                           Country=country,
                           Services=services,
                           Specialiazation=specialist,
                           Degree=degree,
                           College_Institute=college,
                           Hospital_Name=hospitalname,
                           Designation=designation,
                           Awards=awards,
                           Memberships=memberships,
                           Registrations=registrations,
                           Date_of_Birth=date_of_birth,
                           Year_of_Completion=yoc,
                           From=froms,
                           To=to,
                           Year=year,
                           Year_of_Registeration=registrationyear,
                           email=email,
                           clinic_images=clinic_images,
                           Postal_code=postalcode,
                           phoneNumber=phone_number,
                           Gender=gender,
                           consultation_fees=consultation_fees)
            b.save()
        return redirect('doctordashboard')
    else:
        return render(request, 'doctor-profile-settings.html', {"speciality": special, 'allDoctors': allDoctors,'location':results})


def doctorregister(request):
    return render(request, 'doctor-register.html')


def editbilling(request):
    return render(request, 'edit-billing.html')


def editprescription(request):
    return render(request, 'edit-prescription.html')


def favourites(request):
    return render(request, 'favourites.html')


def forgotpassword(request):
    return render(request, 'forgot-password.html')
from django.db.models import Q
def index(request):
    allDoctors = doctor_profile.objects.all()
    results = Location.objects.all
    special = speciality.objects.all
    if request.method == "POST":
        filteredlocation = request.POST['flocation']
        filteredspecial = request.POST['fspecial']
        query = doctor_profile.objects.filter(Q(Specialiazation=filteredspecial) | Q(clinic_address=filteredlocation))
        # query = doctor_profile.objects.filter(Specialiazation=filteredspecial, clinic_address=filteredlocation)
        querycounts = query.count()
        fdata = {'filteredquery': query,
                 'filteredlocation':filteredlocation,
                 'filteredspecial':filteredspecial,
                 'querycounts':querycounts,
                 }
        return render(request,'searchs.html',fdata)
    else:
        return render(request, "index.html", {"location": results, "speciality": special, 'allDoctors': allDoctors})

def invoiceview(request, bid):
    patienid = request.user.id
    patientbookingid = patient_profile.objects.get(patient=patienid)
    appointmentbooking = appointment_booking.objects.all()
    bookingProFile = doctor_profile.objects.get(id=bid)
    total = bookingProFile.consultation_fees + 60
    print(card_number)
    ls = card_number
    print(ls)
    lists = ls[-1:-5:-1]
    r3 = lists[3]
    r2 = lists[2]
    r1 = lists[1]
    r0 = lists[0]
    print(r3, r2, r1, r0)
    invoicedone = {
        'datet': datet,
        'bookingProFile': bookingProFile,
        'total': total,
        'patientbookingid': patientbookingid,
        'card_number': card_number,
        'r3': r3,
        'r2': r2,
        'r1': r1,
        'r0': r0,
        'appointmentbooking': appointmentbooking,

    }
    return render(request, 'invoice-view.html', invoicedone)


def invoices(request):
    return render(request, 'invoices.html')
def patientslogin(request,bid):

    return render(request,'patientslogin.html',{'bid':bid})
def patientlogins(request,bid):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))

        if user!=None:
            print(user)
            login(request,user)
            if user.user_type=="3":
                return redirect('bookings',bid = bid)
            else:
                return HttpResponse('invalid credientials!!')
        else:

            return HttpResponse("error")

def websitelogin(request):
    if request.method =="POST":
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            print(user)
            login(request,user)
            if user.user_type=="2":
                return redirect(doctorprofilesettings)
            elif user.user_type=="3":
                return redirect(patientprofilesettings)
            else:
                return render(request,'login.html',{ "errors": "you are not authorized for admin panel!!"})
        else:
            return render(request,'login.html',{'errors':'Invalid username and/or password.'})
    else:
        return render(request,'login.html')
from django.contrib import auth
def logouts(request):

    auth.logout(request)
    return render(request,'login.html')

def mypatients(request):
    return render(request, 'my-patients.html')


def patientdashboard(request):
    sel_pat = patient_profile.objects.get(patient=request.user)
    allpatients = appointment_booking.objects.filter(appointment_patient_id=sel_pat)
    return render(request, 'patient-dashboard.html',{'appoints':allpatients})

def patientprofilesettings(request):
    if request.method == 'POST':
        patient = request.user
        patient_images = request.FILES['pimage']
        first_name = request.POST['pfname']
        last_name = request.POST['plname']
        phoneNumber = request.POST['pmnumber']
        Date_of_Birth = request.POST['pdob']
        Blood_Group = request.POST['blood']
        email = request.POST['pemail']
        Address = request.POST['paddress']
        City = request.POST['pcity']
        State = request.POST['pstate']
        zip_code = request.POST['pzipcode']
        Country = request.POST['pcountry']
        z = patient_profile(
            patient = patient,
            patient_images=patient_images,
            first_name=first_name,
            last_name=last_name,
            phoneNumber=phoneNumber,
            Date_of_Birth=Date_of_Birth,
            Blood_Group= Blood_Group,
            email=email,
            Address=Address,
            City=City,
            State=State,
            zip_code=zip_code,
            Country=Country
        )
        z.save()
        return redirect(patientdashboard)
    else:
        return render(request, 'profile-settings.html')


def privacypolicy(request):
    return render(request, 'privacy-policy.html')


    return render(request, 'doctor-profile.html', {'DOctorProFile': DOctorProFile})
def patientprofile(request,id):
    sel_pat = patient_profile.objects.get(id=id)
    print(sel_pat.id)
    allpatientsp = appointment_booking.objects.filter(appointment_patient_id=sel_pat)
    print(allpatientsp)
    PatientProFile = patient_profile.objects.get(id=id)
    return render(request, 'patient-profile.html',{'PatientProFile':PatientProFile,'appoints': allpatientsp})


def register(request):
    return render(request,'register.html')
def register_doctor(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=CustomUser.objects.create_user(username=username,password=password,email=email,user_type=2)

        user.save()

        return redirect(websitelogin)
    else:
        return render(request,'doctor-register.html')


def register_patient(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = CustomUser.objects.create_user(username=username, password=password, email=email, user_type=3)
        user.save()
        return redirect(websitelogin)
    else:
        return render(request,'register.html')
    ##################doctor reviews################
# def reviews(request,rid):
#     rpatientid = request.user.id
#     patientreviewid = patient_profile.objects.get(patient=rpatientid)
#     drid = doctor_profile.objects.get(id=rid)
#     if request.method == "POST":
#          doctorratingid = drid
#          patientratingid = patientreviewid
#          stars = request.POST['rating']
#          titles = request.POST['titles']
#          description = request.POST['reviews']
#          r = Rating(
#          doctorratingid=doctorratingid,
#              patientratingid=patientratingid,
#              stars=stars,
#              title=titles,
#              description=description,
#             )
#          r.save()
#          return redirect(doctorprofile)
#     else:
#         return render(request, 'doctor-profile.html', {'rid': rid})

def recomend(request,sid,str):
    recomend_id = Rating.objects.get(id=sid)
    recomend_id.recomend = str
    recomend_id.save()
    return HttpResponse('successful')

def scheduletimings(request):
    return render(request, 'schedule-timings.html')
def stats(request,id,str):
    doc_id = appointment_booking.objects.get(id=id)
    doc_id.status = str
    doc_id.save()
    return redirect(doctordashboard)

def search(request):
    allDoctors = doctor_profile.objects.all()

    return render(request, 'search.html', {'allDoctors': allDoctors})
# Apply filtering with multiple fields
# queryset = Employee.objects.filter(department='HR', email='ali@gmail.com')

def socialmedia(request):
    return render(request, 'social-media.html')


def termcondition(request):
    return render(request, 'term-condition.html')


def voicecall(request):
    return render(request, 'voice-call.html')


def videocall(request, id):
    DOctorProFile = doctor_profile.objects.get(id=id)
    return render(request, "video-call.html", {'DOctorProFile': DOctorProFile})


def capframe():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        ret, encodedframe = cv2.imencode(".jpeg", frame)
        encodedframe = encodedframe.tobytes()
        yield b'--frame\r\n' + b'Content-Type:image/jpeg\r\n\r\n' + encodedframe + b'\r\n'


@gzip.gzip_page
def feed(request):
    return StreamingHttpResponse(capframe(), content_type="multipart/x-mixed-replace; boundary=frame")




