from django.contrib import admin
from app_users.models import UserProfileInfo, Contact
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Contact)