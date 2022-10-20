from django.contrib import admin

class SocialMediaAdmin(admin.ModelAdmin):
    search_fields=('social_type','username')
    exclude=('user',)
