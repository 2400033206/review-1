from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Counsellor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    counsellor = models.ForeignKey(Counsellor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Completed', 'Completed'),
        ],
        default='Pending'
    )

    def __str__(self):
        return f"{self.student.name} - {self.counsellor.name}"