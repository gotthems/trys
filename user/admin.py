from django.contrib import admin

from user.models import User
from user.models import Interest

admin.site.register(User)
admin.site.register(Interest)