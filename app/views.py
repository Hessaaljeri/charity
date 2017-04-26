from django.shortcuts import render, render_to_response
from django.template import RequestContext
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
		name = form.cleaned_data.get('name')
		email = form.cleaned_data.get('email')
		message = form.cleaned_data.get('message')
		recipients = [email]

		# send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
		send_mail(name, ('From: %s - Message: %s' % (email, message)), email, ['cbaproject30@gmail.com'], fail_silently=True)
		# return HttpResponseRedirect('/thankyou/')
	context = {
		"form": form,
	}


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