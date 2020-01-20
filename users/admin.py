from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms.models import Room


class user_RoomAdmin(admin.StackedInline):

    model = Room
    extra = 0


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    inlines = [
        user_RoomAdmin,
    ]

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "langauge",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
        "count_rooms",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthday",
                    "langauge",
                    "superhost",
                )
            },
        ),
    )

    def count_rooms(self, object):
        return object.rooms.count()
