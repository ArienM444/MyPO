from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    verbose_name = "Имена"
    list_display = ('name', 'surname', 'gender',)


admin.site.register(Person, PersonAdmin)

# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#
#     list_display = ('name', 'surname', 'gender')
