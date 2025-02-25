from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form =   CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                'fields': ("username", "email", "password1", "password2"),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)