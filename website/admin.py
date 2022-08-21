from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import *
# Register your models here.
class curstomsusers(admin.ModelAdmin):
    list_display = ('user_type','user_type_data')
admin.site.register(CustomUser,curstomsusers)
class userDB(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Location,userDB)
class special(admin.ModelAdmin):
    list_display = ['speciality']
admin.site.register(speciality,special)
class doctor(admin.ModelAdmin):
    list_display = ('id','doctor','doctor_images','username','email', 'first_name','last_name', 'phoneNumber','Gender','Date_of_Birth',
                        'Biography', 'clinic_name', 'clinic_address', 'clinic_images','Address_line1','Address_line2', 'City',
                        'State_Provice', 'Country','Postal_code',
                        'Pricing',
                        'Services',
                        'Specialiazation',
                        'Degree',
                        'College_Institute',
                        'Year_of_Completion',
                        'Hospital_Name',
                        'From',
                        'To',
                        'Designation',
                        'Awards',
                        'Year',
                        'Memberships',
                        'Registrations','consultation_fees',
                        'Year_of_Registeration')
admin.site.register(doctor_profile,doctor)
class patient(admin.ModelAdmin):
    list_display = ('id',
                    'patient',
                    'patient_images',
                    'first_name',
                    'last_name',
                    'Date_of_Birth',
                    'Blood_Group',
                    'email',
                    'phoneNumber',
                    'Address',
                    'City',
                    'State',
                    'zip_code',
                    'Country',)
admin.site.register(patient_profile,patient)
class booking(admin.ModelAdmin):
    list_display = ('id',
                    'appointment_doctor_id',
                    'appointment_patient_id',
                    'from_time',
                    'to_time',
                    'date',
                    'Payment_card',
                    'card_number',
                    'expire_month',
                    'expire_year',
                    'Cvv',
                    'amount_paid',
                    'status')
admin.site.register(appointment_booking,booking)
class timetable(admin.ModelAdmin):
    list_display = ('id','timetable_doctor_id','doctor_from_time','doctor_to_time','doctor_date')
admin.site.register(doctor_timetable,timetable)

class recom(admin.ModelAdmin):
    list_display = ('id',
        'doctorratingid',
                    'patientratingid',
                    'stars',
                    'recomend',
                    'title',
                    'description')
admin.site.register(Rating,recom)