from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import Registered

class AdminRegistered(admin.ModelAdmin):
	list_display = ["email", "name", "timestamp"]
	form = RegModelForm
	#list_display_links = ["name"]
	list_filter = ["timestamp"]
	list_editable = ["name"]
	search_fields = ["email","name"]
	#class Meta:
	#	model = Registered

admin.site.register(Registered, AdminRegistered)