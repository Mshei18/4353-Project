from django.contrib import admin
from .models import Todo, ClientProfile

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'address1')

# Register your models here.

admin.site.register(Todo, TodoAdmin)
admin.site.register(ClientProfile, ProfileAdmin)