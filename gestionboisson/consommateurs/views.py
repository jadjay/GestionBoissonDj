import datetime, random, sha
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.mail import send_mail
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NewConsommateursForm
from .models import consommateurs
import logging

logger = logging.getLogger(__name__)


# Create your views here.

def index(request):
	return HttpResponse("Bienvenue en gestion consommateurs. Cliquez ici pour creer un user : <a href=/consommateurs/new>Nouveau</a>")

#def new(request):
#	if request.method == 'POST':
#		form = ConsommateursForm(request.POST)
#		if form.is_valid():
#			form.save()
#			return HttpResponseRedirect('/consommateurs/new')
#	else:
#		form = ConsommateursForm()
#
#	return render(request, 'consommateurs/new.html', {'form': form})
def new(request):
	if request.method == 'POST':
		form = UsersForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/consommateurs/new')
	else:
		form = UsersForm()

	return render(request, 'consommateurs/new.html', {'form': form})

def register(request):
#	if request.user.is_authenticated():
#		logger.error('AUTH!')
#		# They already have an account; don't let them register again
#		return render_to_response('register.html', {'has_account': True})
	if request.POST:
		form = NewConsommateursForm(request.POST)
		if form.is_valid:
			form.save()
			
			# Build the activation key for their account
			salt = sha.new(str(random.random())).hexdigest()[:5]
			activation_key = sha.new(salt+new_user.username).hexdigest()
			key_expires = datetime.datetime.today() + datetime.timedelta(2)
			
			# Create and save their profile
			new_profile = consommateurs(
					user=new_user,
					activation_key=activation_key,
					key_expires=key_expires)
			new_profile.save()
			
			# Send an email with the confirmation link																													  
			email_subject = 'Your new example.com account confirmation'
			email_body = "Hello, %s, and thanks for signing up for an \
example.com account!\n\nTo activate your account, click this link within 48 \
hours:\n\nhttp://127.0.0.1:8000/consommateurs/confirm/%s" % (new_user.username,new_profile.activation_key)
			send_mail(
				email_subject,
				email_body,
				'donotreply@gestionboissons.org',
				[new_user.email]
			)
			print email_body
			return render_to_response('register.html', {'created': True})
	else:
		logger.error('GET!')
		errors = new_data = {}
		form = NewConsommateursForm()
#forms.FormWrapper(manipulator, new_data, errors)
		return render_to_response('register.html', {'form': form})

def confirm(request, activation_key):
    if request.user.is_authenticated():
        return render_to_response('confirm.html', {'has_account': True})
    user_profile = get_object_or_404(UserProfile,
                                     activation_key=activation_key)
    if user_profile.key_expires < datetime.datetime.today():
        return render_to_response('confirm.html', {'expired': True})
    user_account = user_profile.user
    user_account.is_active = True
    user_account.save()
    return render_to_response('confirm.html', {'success': True})
