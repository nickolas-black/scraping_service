from django.contrib import admin
from .models import City, Vacancy, Language


admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
