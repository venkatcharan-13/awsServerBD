from django.db import models

# Create your models here.

genderSelection=[("Male","Male"),("Female","Female")]
bloodgroupSelection=[
    ('A +','A +'),
    ('A -','A -'),
    ('B +','B +'),
    ('B -','B -'),
    ('AB +','AB +'),
    ('AB -','AB -'),
    ('O +','O +'),
    ('O -','O -'),
]
class bloodDonateData(models.Model):
    def __str__(self):
        return str(self.blood_group)
    sl_no=models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField( blank=True, null=True )
    email_id = models.EmailField(max_length=50, blank=True, null=True )
    age = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=100,choices=genderSelection, default='Female')
    blood_group = models.CharField(max_length=100,choices=bloodgroupSelection, default='AB +')
    address = models.TextField(blank=True, null=True)
    upload_file = models.CharField(max_length=200 ,blank=True, null=True)
    