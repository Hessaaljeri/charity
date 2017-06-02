from django.contrib import admin
from app.models import Charity, Appointment

# Register your models here.


class AppointmentAdmin(admin. ModelAdmin):
    list_display = ('name', 'date_time', 'phone',
                    'charity')


admin.site.register(Charity)
admin.site.register(Appointment, AppointmentAdmin)
