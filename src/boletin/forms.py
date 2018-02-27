from django import forms

from .models import Registered

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registered
		fields = ['name','email']

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		#domain, extension = proveeder.split(".")
		if ".edu" not in proveeder :
			raise forms.ValidationError("You have to use .edu extension ")
		return email

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)