from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from app.models import *
from app.forms import EmailForm, AppointmentForm
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView
from django.contrib import messages
# from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required


# Create your views here.
@csrf_exempt
def email_submission(request):
    print "email_submission"
    form = EmailForm(request.POST or None)
    print form
    if form.is_valid():
        print "form is valid"
        fullname = form.cleaned_data.get('fullname')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER

        to_email = [from_email, 'haljeri@icloud.com']
        contact_message = "%s: %s via %s" % (
            fullname,
            message,
            email,)

        send_mail(subject, contact_message, from_email,
                  to_email, fail_silently=False)
    context = {
        "form": form,
    }

    print "email sent"
    return HttpResponseRedirect('/home/')


def charity_list(request):
    context = {}
    charities = Charity.objects.all()
    context['charities'] = charities

    return render(request, 'charity_list.html', context)

@login_required
def charity_detail(request, pk):
    charity = Charity.objects.get(pk=pk)
    context = {}
    context['charity'] = charity
    return render_to_response('charity_detail.html', context, context_instance=RequestContext(request))


def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank You, Appointment was successfully created')
            return redirect('home')
    else:
        form = AppointmentForm
    return render(
        request,
        'take_appointment.html',
        {
            'form': form,
        })

# @staff_member_required
class AppointmentList(ListView):
    model = Appointment
    template_name = "appointment_list.html"
    context_object_name = "appointments"



def AppoinmentDetail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    # messages.success(request, 'Thanks for the Donation %s' % appointment.name)
    return render(request,
                  'appointment_details.html',
                  {
                      'appointment': appointment,
                  })

class AppointmentEdit(UpdateView):
    model = Appointment
    fields = ('name', 'date_time', 'Location', 'email', 'phone', 'note')
    template_name = 'appointment_edit.html'
    context_object_name = 'appointment'
