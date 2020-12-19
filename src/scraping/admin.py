from django.contrib import admin
from .models import City, Vacancy, Language, Error


admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
admin.site.register(Error)