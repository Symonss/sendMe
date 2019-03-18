from django.contrib import admin

from .models import (User,Employer, RegionalAdmin)
# we register our objects here(these are the tables)
admin.site.register(Employer)
admin.site.register(RegionalAdmin)
admin.site.register(User)
