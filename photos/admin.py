from django.contrib import admin
from .models import Location, Album, Photo


admin.site.register(Location),
admin.site.register(Album),
admin.site.register(Photo)

