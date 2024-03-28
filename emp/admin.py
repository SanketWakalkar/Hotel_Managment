from django.contrib import admin
from .models import Emp
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','emp_id','Phone')
    list_editable=('working','emp_id')
    search_fields=('name','Phone')
    list_filter=('working',)
admin.site.register(Emp,EmpAdmin)