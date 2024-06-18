from django.contrib import admin
from .models import UserProfile, ContactMessage

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  
    list_filter = ('email',) 

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message') 
    list_filter = ('name',) 

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
