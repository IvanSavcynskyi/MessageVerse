from django.contrib import admin

# Register your models here.
# messages/admin.py
from .models import Message

admin.site.register(Message)
