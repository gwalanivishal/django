from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):


	username = forms.CharField(max_length=250, label=_("username"))
	email = forms.CharField(max_length=250, label=_("email address"))
	password1 = forms.CharField(max_length=30, label=_("password"))
	password2 = forms.CharField(max_length=30, label=_("password again"))


	def check_username(self):
		try:
			user = User.objects.get(username__iexact=self.check_username['username'])
		except User.DoesNotExist:
			return self.check_username['username']
		raise forms.ValidaionError("the username already exists")

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))
		return self.cleaned_data		
