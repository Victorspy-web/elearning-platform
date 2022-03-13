from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileUpdateForm, RegistrationForm
from .models import CustomUser


class MyUserAdmin(UserAdmin):
	add_form = RegistrationForm
	form = ProfileUpdateForm
	model = CustomUser
	list_display = ['username', 'is_staff', 'is_active']


admin.site.register(CustomUser, MyUserAdmin)
