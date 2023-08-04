from django.contrib import admin
from .models import Cookies,Cakes,HealthyCookies

# Register your models here.

class CakesAdmin(admin.ModelAdmin):
    list_display = ("title", "price",)
    search_fields = ("title",)
    list_filter = ("title", "ingredients",)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Cakes, CakesAdmin)

class CookiesAdmin(admin.ModelAdmin):
    list_display = ("title", "price",)
    search_fields = ("title",)
    list_filter = ("title", "ingredients",)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(Cookies, CookiesAdmin)

class HealthyCookiesAdmin(admin.ModelAdmin):
    list_display = ("title", "price",)
    search_fields = ("title",)
    list_filter = ("title", "ingredients",)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(HealthyCookies, HealthyCookiesAdmin)