from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm   # yangi user qo‘shishda foydalaniladigan forma
    form = CustomUserChangeForm         # mavjud userni o‘zgartirish uchun forma
    model = CustomUser

    list_display = [
        "email",
        "username",
        "name",
        "is_staff",
    ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("name",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "name", "password1", "password2"),
        }),
    )

# CustomUser ni admin panelga ro‘yxatdan o‘tkazish
admin.site.register(CustomUser, CustomUserAdmin)
