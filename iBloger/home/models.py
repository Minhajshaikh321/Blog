from unicodedata import name
from django.db import models

# Create your models here.
#database-->excel workbook
#models in django--->table--->sheet
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=240)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return ' Message from ' +  self.name + ' - ' + self.email
