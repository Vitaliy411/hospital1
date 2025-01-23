from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    speciality = models.ForeignKey(Specialization, on_delete=models.CASCADE, null=True)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (PLANNED, PLANNED),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED)
    ]
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    visit_date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.doctor.full_name} - {self.patient.full_name} - {self.visit_date_time}"