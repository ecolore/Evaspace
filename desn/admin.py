from django.contrib import admin
from .models import Collection

@admin.register(Collection)

class RequestDemoAdmin(admin.ModelAdmin):

  list_display = [field.name for field in Collection._meta.get_fields()]