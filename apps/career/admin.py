from django.contrib import admin

# Register your models here.
from .models import Career, Subject, Level, Quarter
from . import views

admin.site.register(Level)
admin.site.register(Quarter)
# admin.site.register(Career)
# admin.site.register(Subject)

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 5

@admin.register(Career)
class CareerModelAdmin(admin.ModelAdmin):
    list_display = ['id','level','name','is_active','principal']
    list_filter = ['level']
    fields = ['short_name','level']
    inlines = [SubjectInline]