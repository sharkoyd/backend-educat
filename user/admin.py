from django.contrib import admin
from .models import Profile,VerificationCode

# Register your models here.
admin.site.register(Profile)
admin.site.register(VerificationCode)
