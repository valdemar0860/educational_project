from django.contrib import admin

# Register your models here.
# from django.contrib.admin import register

from home.models import Student


class StudentAdmin(admin.ModelAdmin):
    # pass
    list_display = ('name', 'age', 'auto')
    fields = ('name', 'age')

    def auto(self, object):
        return f'Hello {object.name}'


# register(StudentAdmin)
admin.site.register(Student, StudentAdmin)