from django.db import models 
from django import forms

from django.forms.fields import Field




class EmailForm(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.EmailField()
	message = forms.CharField()