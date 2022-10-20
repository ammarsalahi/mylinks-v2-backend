from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    search_fields=('username','email')
    list_display=['username','email','first_name','last_name','last_login']
    list_filter=['last_login']
