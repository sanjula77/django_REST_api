from django.db import models

# Create your models here.
class Employe(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)
    emp_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.emp_name} {self.emp_id}"
