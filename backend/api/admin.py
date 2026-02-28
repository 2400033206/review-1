from django.contrib import admin
from .models import Student, Counsellor, Appointment

admin.site.register(Student)
admin.site.register(Counsellor)
admin.site.register(Appointment)