from django.contrib import admin
from user_management.models import Profile, Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Profile)

class AccountAdmin(UserAdmin):
    list_display=('email','username','date_joined','last_login','is_admin','is_staff')
    search_fields=('email','username')
    readonly_fields=('date_joined','last_login')
    fieldsets=()
    filter_horizontal=()
    list_filter=()

admin.site.register(Account, AccountAdmin)