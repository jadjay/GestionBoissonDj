from django import forms
from django.core import validators
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

from django.core.exceptions import ValidationError

def validate_otherfield(value,fieldvalue,msg):
    if value != fieldvalue :
        raise ValidationError(msg)

# http://www.b-list.org/weblog/2006/sep/02/django-tips-user-registration/
class NewConsommateursForm(forms.Form):
        username = forms.CharField()
        email = forms.CharField(required=True,)
        password1 = forms.CharField(widget=forms.PasswordInput)
        password2 = forms.CharField(widget=forms.PasswordInput)
#, validators=[
#									validate_otherfield('password2','password1','Passwords must match.')
#								]
#			)

	logger.error("prout");
	
	def isValidUsername(self, field_data, all_data):
		try:
			User.objects.get(username=field_data)
		except User.DoesNotExist:
			return
		raise validators.ValidationError('The username "%s" is already taken.' % field_data)
	
	def save(self, new_data):
		u = User.objects.create_user(
			new_data['username'],
			new_data['email'],
			new_data['password1']
			)
		u.is_active = False
		u.save()
		return u

class ConsommateursForm(forms.Form):
	username = forms.CharField()
	email = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput)
