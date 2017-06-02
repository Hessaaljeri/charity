from django.conf.urls import include, url
from django.contrib import admin
from app import views

from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # home page
    # url(r'^$','app.views.home'),
    # url(r'^home/$','app.views.home'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^home/$', TemplateView.as_view(template_name='index.html'), name='home'),

    #registration (redux)
    url(r'^accounts/', include('registration.backends.default.urls')),

    #charitties
    url(r'^list/$', 'app.views.charity_list', name='list'),
    url(r'^detail/(?P<pk>.+)/$', 'app.views.charity_detail', name='detail'),

    url(r'^select/$', TemplateView.as_view(template_name='select.html'), name='select'),

    #navbar
    url(r'^contact/$', 'app.views.email_submission'),
    url(r'^aboutus/$', TemplateView.as_view(template_name='aboutus.html'), name='aboutus'),
    url(r'^contactus/$', TemplateView.as_view(template_name='contact.html'), name='contactus'),

   
    #bookings
     url(r'^appointment/create/$', views.appointment_create, name='appointment_create',),

    url(r'^appointment/list/$', views.AppointmentList.as_view(), name='appointment_list',),

    url(r'^appointment/(?P<appointment_id>\d+)/$', views.AppoinmentDetail, name='appointment_details'),

    url(r'^appointment/(?P<pk>\d+)/edit/$', views.AppointmentEdit.as_view(), name='appointment_edit',),

]
