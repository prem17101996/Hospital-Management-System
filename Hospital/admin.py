from django.contrib import admin
from Hospital.models import Doctor,Patient,Appoinment
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinment)