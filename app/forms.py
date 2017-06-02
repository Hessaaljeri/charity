from django.db import models
from django import forms
from django.forms.fields import Field
from .models import Appointment
from datetimewidget.widgets import DateTimeWidget


class EmailForm(forms.Form):
    fullname = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField()


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            'autoclose': True,
            'showMeridian': True
        }
        widgets = {
            'approved': forms.HiddenInput,
            'date_time': DateTimeWidget(options=dateTimeOptions,
                                        usel10n=True, bootstrap_version=3)
        }
