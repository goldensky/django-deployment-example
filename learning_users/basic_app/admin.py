from django.contrib import admin
from .models import User, UserProfileInfo

from .forms import UserForm, UserProfileInfoForm

# Register your models here.


admin.site.register(UserProfileInfo)