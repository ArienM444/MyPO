from django.contrib import admin
from .models import Person
from datetime import datetime

#
# class PersonAdmin(admin.ModelAdmin):
#     verbose_name = "Имена"
#     list_display = ('name', 'surname', 'gender',)


# admin.site.register(Person, PersonAdmin)

a = datetime.now()


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    def age(self, other):
        return a.year - other.date_of_birth

    list_display = ('name', 'surname', 'gender', 'age')
