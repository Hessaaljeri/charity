from django.db import models
from geoposition.fields import GeopositionField
from django.core.urlresolvers import reverse


# Create your models here.


class Charity(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Email = models.EmailField('email address', max_length=255, unique=True)
    Phone = models.CharField(max_length=8, null=True, blank=True)
    Fax = models.CharField(max_length=8, null=True, blank=True)
    Logo = models.ImageField(upload_to='')
    Location = GeopositionField()
    AboutUs = models.TextField(max_length=1000, null=False, blank=False)
    Website = models.URLField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return "%s" % self.Name


class Appointment(models.Model):
    name = models.CharField(max_length=120)
    date_time = models.DateTimeField()
    phone = models.CharField(max_length=20, blank=True, default="")
    email = models.EmailField()
    Location = GeopositionField()
    note = models.TextField(default="")
    approved = models.NullBooleanField(null=True, blank=True)
    charity = models.ForeignKey(Charity)

    def get_absolute_url(self):
        return reverse('home')
