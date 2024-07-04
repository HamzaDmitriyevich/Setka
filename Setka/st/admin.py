
from django.contrib import admin 
from .models import Setka 
  
# Register your models here. 
 
@admin.register(Setka) 
class SetkaAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in Setka._meta.get_fields()]

