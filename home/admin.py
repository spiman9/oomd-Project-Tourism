from django.contrib import admin
from .models import contactus
from .models import India , Dubai , Singapore

# Register your models here.
admin.site.register(India)
admin.site.register(Dubai)
admin.site.register(Singapore)
admin.site.register(contactus)
