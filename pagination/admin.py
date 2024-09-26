from django.contrib import admin
from .models import Person

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
   list_display=['id','name','p_id','address','contact']