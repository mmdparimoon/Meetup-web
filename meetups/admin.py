from django.contrib import admin
from .models import Location, Meetup, Participant

# Register your models here.

class Admin(admin.ModelAdmin):
    list_display=('title','data','location')
    list_filter=('location',)
    prepopulated_fields={'slug':('title', 'location')}
    
    
admin.site.register(Meetup, Admin) 
admin.site.register(Location)
admin.site.register(Participant)
