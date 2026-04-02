from django.contrib import admin
from .models import Course


admin.site.site_header = "Control Room"
admin.site.site_title = "Control Room"
admin.site.index_title = "Manage your platform"
admin.site.register(Course)

