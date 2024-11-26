from django.contrib import admin

# Register your models here.
from .models import KPI, AssetKPI

admin.site.register(KPI)
admin.site.register(AssetKPI)
