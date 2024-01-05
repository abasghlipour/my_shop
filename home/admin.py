from django.contrib import admin
from .models import Skill, Person
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class PersonInline(admin.StackedInline):
    model = Person
    can_delete = False


class ExtendedUserAdmin(UserAdmin):
    inlines = (PersonInline,)


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
admin.site.register(Skill)
