from django.db import models

# Create your models here.
class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    dob = models.DateField()
    age = models.IntegerField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.pid}--{self.name}--{self.email}--{self.dob}--{self.age}--{self.city}"