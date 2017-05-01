from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from app.models import *
from app.forms import EmailForm

from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt

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
		contact_message = "%s: %s via %s"%(
				fullname,  
				message, 
				email,)

		send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
		# return HttpResponseRedirect('/thankyou/')
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


def charity_detail(request, pk):  
  charity = Charity.objects.get(pk=pk)
  context = {}
  context['charity'] = charity
  return render_to_response('charity_detail.html', context, context_instance=RequestContext(request))


 #  def home(request):
 #  	context = {}
	# charities = Charity.objects.all()
	# context['charities'] = charities
	# return render_to_response('index.html', context, context_instance=RequestContext(request))