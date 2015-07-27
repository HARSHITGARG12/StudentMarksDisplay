from django.contrib import admin

# Register your models here.

from django.contrib import admin
from stud.models import *

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',     {'fields': ['Name']}),
        ('Physics', {'fields': ['Physics']}),
          ('Chemistry', {'fields': ['Chemistry']}),
            ('Mathematics', {'fields': ['Mathematics']}),
    ]

admin.site.register(Student, StudentAdmin)
