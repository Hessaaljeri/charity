from django.db import models
from geoposition.fields import GeopositionField

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