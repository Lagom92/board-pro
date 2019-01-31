from django.contrib import admin
from .models import Board,Comment
# Register your models here.

class BoardModelAdmin(admin.ModelAdmin):
    readonly_field = ('time',)
    
admin.site.register(Board,BoardModelAdmin)
admin.site.register(Comment)

