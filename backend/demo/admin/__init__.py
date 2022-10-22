from django.contrib import admin
from demo.models import (
    Project,
    Image
)
from .project import ProjectAdmin

admin.site.register(Project,ProjectAdmin)
admin.site.register(Image)