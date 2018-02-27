from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registered

# Create your views here.
def index(request):
	form = RegModelForm(request.POST or None)
	title = ""
	if request.user.is_authenticated():
		title = "Welcome %s" %(request.user)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print instance
		#form_data = form.cleaned_data
		#email = form_data.get('email')
		#name = form_data.get('name')
		#obj = Registered.objects.create(email = email, name = name)
	context = {
		"form" : form,
		"title": title,
	}
	return render(request, "index.html", context)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data
	context = {
		"form": form,

	}
	return render(request, "contact.html", context)