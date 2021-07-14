from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField(null=True)
    special=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Patient(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=12)
    mobile=models.IntegerField(null=True)
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Appoinment(models.Model):
    id=models.IntegerField(primary_key=True)
    # doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    # patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.CharField(max_length=50)
    patient=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return self.doctor+"--"+self.patient