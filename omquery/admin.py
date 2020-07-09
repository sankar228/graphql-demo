from django.contrib import admin

# Register your models here.
from .models import CellOM, EnbOM, NimsTmus

admin.site.register(CellOM)
admin.site.register(EnbOM)
admin.site.register(NimsTmus)