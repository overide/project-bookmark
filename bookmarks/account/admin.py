from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','date_of_birth','photo',)
	list_filter = ('date_of_birth',)
	raw_id_fields = ('user',)

admin.site.register(Profile, ProfileAdmin)
