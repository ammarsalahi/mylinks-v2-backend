from django.contrib import admin

class ProjectAdmin(admin.ModelAdmin):
    list_display=('title','url','created_at','updated_at')
    list_filter=('created_at','updated_at')
    search_fields=('title','url')