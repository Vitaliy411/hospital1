from django.contrib import admin

from .models import Specialization, Visit, Patient, Service, Schedule, Doctor

admin.site.register(Specialization)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Schedule)
admin.site.register(Doctor)