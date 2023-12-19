from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'name_of_doctor', 'tin_no', 'hospital_name', 'mobile_no', 'email_address')
