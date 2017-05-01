from django.db import models 
from django import forms

from django.forms.fields import Field




class EmailForm(forms.Form):
	fullname = forms.CharField(max_length=255)
	email = forms.EmailField()
	subject = forms.CharField(max_length=255)
	message = forms.CharField()