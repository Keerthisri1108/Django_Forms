from django.contrib import admin
from Base.models import Unemployment
# Register your models here.
class UnemploymentAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Unemployment,UnemploymentAdmin)
