from django.contrib import admin
from .models import Registration,Movie_Data
# Register your models here.
from import_export.admin import ImportExportModelAdmin

admin.site.register(Registration)
@admin.register(Movie_Data)
class movie_data(ImportExportModelAdmin):
    pass